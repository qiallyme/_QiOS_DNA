from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import shutil
import stat
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any

import markdown


# ---------------------------------------------------------------------------
# Default paths
# ---------------------------------------------------------------------------
DEFAULT_QILABS_ROOT = Path(r"C:\QiLabs")
DEFAULT_SOURCE = Path(r"C:\QiLabs\40_QiVault")
DEFAULT_DIST = Path(r"C:\QiLabs\10_QiSpark\dist")
BOOKMARKS_CSV = Path(
    r"C:\QiLabs\00_QiLabs.workspace\_qiconfig\_bookmarks\bookmarks.csv"
)

# Controlled tag vocabulary configuration
VALID_STATUSES = {"publish", "published", "public", "pub"}
EXCLUDE_SENSITIVITY = {"private", "sensitive", "confidential"}
EXCLUDE_CLASSIFICATION = {"private", "sensitive", "confidential"}
EXCLUDE_FLAGS = ["private", "sensitive", "confidential", "private_theory_flag"]

# Tree safety defaults.
TREE_SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".obsidian",
    ".trash",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "dist",
    "build",
    ".wrangler",
    ".vercel",
    ".netlify",
    "30_QiDrive",
}
TREE_SKIP_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.development",
    ".env.production",
    ".env.test",
    "id_rsa",
    "id_dsa",
    "id_ed25519",
}
TREE_SKIP_EXTENSIONS = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
    ".sqlite",
    ".sqlite3",
    ".db",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def rel(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def normalize_path(path: Path) -> Path:
    return path.expanduser().resolve()


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def ensure_safe_build_paths(source_dir: Path, dist_dir: Path) -> None:
    source_dir = normalize_path(source_dir)
    dist_dir = normalize_path(dist_dir)

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a directory: {source_dir}")

    if dist_dir == source_dir:
        raise ValueError("Refusing to build: --dist cannot be the same as --source.")

    if is_relative_to(dist_dir, source_dir):
        raise ValueError(
            "Refusing to build: --dist is inside --source. "
            "That risks deleting or publishing source content."
        )


def safe_clean_dist(dist_dir: Path) -> None:
    dist_dir = normalize_path(dist_dir)

    if dist_dir.exists():
        if dist_dir.name.lower() != "dist":
            raise ValueError(
                f"Refusing to delete output folder because it is not named 'dist': {dist_dir}"
            )
        shutil.rmtree(dist_dir)

    dist_dir.mkdir(parents=True, exist_ok=True)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"['\"`]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def text_to_title(value: str) -> str:
    value = Path(value).stem
    value = value.replace("_", " ").replace("-", " ")
    return value.title()


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text

    match = re.search(r"\n---\s*\n", text)
    if not match:
        return {}, text

    raw = text[4 : match.start()]
    body = text[match.end() :]
    data: dict[str, Any] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        list_item = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if list_item and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(list_item.group(1).strip("'\" "))
            continue

        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not key_match:
            continue

        key, value = key_match.group(1), key_match.group(2).strip("'\" ")
        current_key = key

        if value == "":
            data[key] = [] if key in {"tags", "aliases", "keywords", "references"} else ""
        elif value == "[]":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            data[key] = [v.strip("'\" ") for v in value.strip("[]").split(",") if v.strip()]
        else:
            if key in {"tags", "aliases", "keywords", "references"}:
                data[key] = [value]
            else:
                data[key] = value

    return data, body


def should_include(fm: dict[str, Any], allow_active: bool = False, strict_publish: bool = False) -> tuple[bool, str]:
    """Return (True, "") if a file should be included in the build.

    Safety Rule:
      1. Exclude if visibility is 'private', 'internal', 'business_internal', or 'confidential'.
      2. Exclude if sensitivity is in EXCLUDE_SENSITIVITY.
      3. Exclude if classification is in EXCLUDE_CLASSIFICATION.
      4. Exclude if draft is True or publish is False or explicit exclude flags are set.
      5. If strict_publish is True, require visibility=='public', sensitivity=='public', classification=='public', and 'qispark' in publish_target.
      6. Otherwise (default vault mode), include all non-restricted documents.
    """
    status = str(fm.get("status") or "").lower().strip()
    visibility = str(fm.get("visibility") or "").lower().strip()
    sensitivity = str(fm.get("sensitivity") or "").lower().strip()
    classification = str(fm.get("classification") or "").lower().strip()

    if fm.get("draft") is True or str(fm.get("draft")).lower() in ("true", "1", "yes"):
        return False, "Draft document"
    if fm.get("publish") is False or str(fm.get("publish")).lower() in ("false", "0", "no"):
        return False, "Publish is disabled"

    pt_val = fm.get("publish_target") or ""
    if isinstance(pt_val, list):
        targets = [str(t).lower().strip() for t in pt_val]
    else:
        targets = [t.strip() for t in str(pt_val).lower().replace(";", ",").split(",") if t.strip()]

    # Explicit exclusions check
    if visibility in ("private", "internal", "business_internal", "confidential"):
        return False, f"Visibility is '{visibility}'"
    if sensitivity in EXCLUDE_SENSITIVITY:
        return False, f"Sensitivity '{sensitivity}' is restricted"
    if classification in EXCLUDE_CLASSIFICATION:
        return False, f"Classification '{classification}' is restricted"
    for flag in EXCLUDE_FLAGS:
        val = fm.get(flag)
        if isinstance(val, bool) and val or str(val).lower() in ("yes", "true", "1"):
            return False, f"Explicit flag '{flag}' is enabled"

    if strict_publish:
        if visibility != "public":
            return False, f"Visibility '{visibility}' is not 'public'"
        if sensitivity != "public":
            return False, f"Sensitivity '{sensitivity}' is not 'public'"
        if classification != "public":
            return False, f"Classification '{classification}' is not 'public'"
        if "qispark" not in targets:
            return False, f"Publish target '{pt_val}' does not include 'qispark'"
        if status not in VALID_STATUSES and not (allow_active and status == "active"):
            return False, f"Status '{status}' is not a publish status"

    return True, ""


def process_markdown_alerts(html_text: str) -> str:
    """Replace GitHub alert callouts with styled HTML alerts."""
    alert_types = {
        "NOTE": ("alert-note", "info", "Note"),
        "TIP": ("alert-tip", "lightbulb", "Tip"),
        "IMPORTANT": ("alert-important", "alert-circle", "Important"),
        "WARNING": ("alert-warning", "alert-triangle", "Warning"),
        "CAUTION": ("alert-caution", "shield-alert", "Caution"),
    }
    for tag, (css_class, icon, label) in alert_types.items():
        pattern = re.compile(rf"<blockquote>\s*<p>\s*\[!{tag}\]\s*", re.IGNORECASE)
        replacement = f'<blockquote class="markdown-alert {css_class}"><p class="alert-title"><i data-lucide="{icon}"></i> {label}</p><p>'
        html_text = pattern.sub(replacement, html_text)
    return html_text


def estimate_reading_time(text: str) -> str:
    words = len(re.findall(r"\w+", text))
    minutes = max(1, round(words / 200))
    return f"{minutes} min read"


def hex_to_rgb(hex_str: str) -> str:
    hex_str = hex_str.lstrip("#")
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)
    return f"{r}, {g}, {b}"


# ---------------------------------------------------------------------------
# Shared HTML shell
# ---------------------------------------------------------------------------
HTML_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-color: #05060b;
            --card-bg: rgba(255, 255, 255, 0.028);
            --card-border: rgba(255, 255, 255, 0.065);
            --card-hover-border: rgba(99, 102, 241, 0.45);
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.22);
            --accent-purple: #a855f7;
            --text-color: #e2e8f0;
            --text-muted: #94a3b8;
            --text-subtle: #64748b;
            --sidebar-width: 340px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.65;
            overflow-x: hidden;
        }

        .bg-glow-1 {
            position: fixed;
            top: -10%;
            left: -10%;
            width: 50vw;
            height: 50vw;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.14) 0%, rgba(99, 102, 241, 0) 70%);
            filter: blur(100px);
            z-index: -1;
            pointer-events: none;
        }

        .bg-glow-2 {
            position: fixed;
            bottom: -10%;
            right: -10%;
            width: 45vw;
            height: 45vw;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(168, 85, 247, 0.09) 0%, rgba(168, 85, 247, 0) 70%);
            filter: blur(100px);
            z-index: -1;
            pointer-events: none;
        }

        header {
            border-bottom: 1px solid var(--card-border);
            background: rgba(5, 6, 11, 0.92);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 1px 0 rgba(255,255,255,0.03);
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            padding: 1rem 1.5rem;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            color: white;
            font-weight: 650;
            font-size: 1.32rem;
            letter-spacing: -0.5px;
            white-space: nowrap;
        }

        .nav-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-end;
            gap: 0.4rem;
        }

        .nav-link {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.93rem;
            font-weight: 500;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.48rem 0.75rem;
            border-radius: 9999px;
            position: relative;
        }

        .nav-link:hover, .nav-link.active {
            color: white;
            background: rgba(255, 255, 255, 0.06);
        }

        .nav-link.active::after {
            content: '';
            position: absolute;
            bottom: -3px;
            left: 50%;
            transform: translateX(-50%);
            width: 16px;
            height: 2px;
            background: var(--primary);
            border-radius: 2px;
        }

        .container {
            max-width: 1300px;
            margin: 0 auto;
            padding: 2.5rem 1.5rem;
        }

        .glass-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.25rem;
            margin-bottom: 3.5rem;
        }

        .section-subtitle {
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--text-muted);
            margin: 2.5rem 0 1.25rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            letter-spacing: -0.3px;
        }
    </style>
</head>
<body>
    <div class="bg-glow-1"></div>
    <div class="bg-glow-2"></div>
    <header>
        <div class="nav-container">
            <a href="{home_path}" class="logo-section">
                <i data-lucide="zap" class="logo-icon"></i>
                <span>{site_title}</span>
            </a>
            <div class="nav-links">
                <a href="{home_path}" class="nav-link"><i data-lucide="home"></i> Home</a>
                <a href="{docs_path}" class="nav-link"><i data-lucide="book-open"></i> Documentation</a>
                <a href="{tree_path}" class="nav-link"><i data-lucide="folder-tree"></i> QiLabs Tree</a>
            </div>
        </div>
    </header>
"""


HTML_FOOTER = """
    <script>
        lucide.createIcons();

        function setActiveNav() {
            const currentPath = window.location.pathname;
            document.querySelectorAll('.nav-link').forEach(link => {
                const href = link.getAttribute('href');
                if (!href) return;
                try {
                    const resolved = new URL(href, window.location.href).pathname;
                    if (resolved === currentPath || currentPath === resolved + 'index.html' || (href.includes('docs/index.html') && currentPath.includes('/docs/'))) {
                        link.classList.add('active');
                        return;
                    }
                } catch(e) {}
                if (currentPath.endsWith(href) || (href.includes('index.html') && (currentPath === '/' || currentPath.endsWith('/')))) {
                    link.classList.add('active');
                }
            });
        }

        function toggleAllDetails(open) {
            document.querySelectorAll('.doc-tree details').forEach(el => el.open = open);
        }

        function filterSidebar(query) {
            const q = query.trim().toLowerCase();
            document.querySelectorAll('.doc-tree .tree-item').forEach(item => {
                const text = item.textContent.toLowerCase();
                if (!q || text.includes(q)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
            if (q) {
                document.querySelectorAll('.doc-tree details').forEach(el => el.open = true);
            }
        }

        // Setup Code Copy Buttons
        document.querySelectorAll('.markdown-body pre').forEach(pre => {
            if (pre.querySelector('.copy-code-btn')) return;
            const btn = document.createElement('button');
            btn.className = 'copy-code-btn';
            btn.innerHTML = '<i data-lucide="copy" style="width:12px;height:12px;"></i> Copy';
            btn.onclick = () => {
                const code = pre.querySelector('code')?.innerText || pre.innerText;
                navigator.clipboard.writeText(code).then(() => {
                    btn.innerHTML = '<i data-lucide="check" style="width:12px;height:12px;"></i> Copied!';
                    setTimeout(() => { btn.innerHTML = '<i data-lucide="copy" style="width:12px;height:12px;"></i> Copy'; }, 2000);
                });
            };
            pre.style.position = 'relative';
            pre.appendChild(btn);
        });

        window.addEventListener('load', setActiveNav);
    </script>
</body>
</html>
"""


def make_header(title: str, home_path: str, docs_path: str, tree_path: str, site_title: str = "QiSpark") -> str:
    return (
        HTML_HEADER
        .replace("{title}", html.escape(title))
        .replace("{home_path}", home_path)
        .replace("{docs_path}", docs_path)
        .replace("{tree_path}", tree_path)
        .replace("{site_title}", html.escape(site_title))
    )


# ---------------------------------------------------------------------------
# Landing Page
# ---------------------------------------------------------------------------
def render_landing(services: list[dict[str, Any]], docs_root_rel: str, tree_rel: str) -> str:
    public_services = [svc for svc in services if "public" in svc.get("surface", ["public"])]

    service_groups = {}
    for svc in public_services:
        category = svc.get("category", "Other Services") or "Other Services"
        service_groups.setdefault(category, []).append(svc)

    services_sections_html = ""
    for category, svcs in service_groups.items():
        cards_html = ""
        for svc in svcs:
            url = svc.get("url")
            status = str(svc.get("status", "active")).lower().strip()
            is_dev = status == "development" or not url or url == "#"

            if url == "docs/index.html" or svc.get("id") == "qispark_docs":
                url = docs_root_rel if docs_root_rel != "#" else "docs/index.html"
            elif url == "tree.html":
                url = tree_rel

            color = svc.get('color', '#6366f1')
            rgb = hex_to_rgb(color)
            title = html.escape(svc.get('title', 'Untitled'))
            desc = html.escape(svc.get('description', ''))
            icon = svc.get('icon', 'zap')

            if is_dev:
                cards_html += f'''
                <div class="glass-card service-card service-card-disabled" style="--accent: {color}; cursor: default; opacity: 0.85;">
                    <div class="service-icon" style="background: rgba({rgb}, 0.12); color: {color}"><i data-lucide="{icon}"></i></div>
                    <div class="service-details">
                        <h3>{title} <span class="status-badge dev-badge">In Development</span></h3>
                        <p>{desc}</p>
                    </div>
                </div>
                '''
            else:
                cards_html += f'''
                <a href="{html.escape(url, quote=True)}" class="glass-card service-card" style="--accent: {color}; text-decoration: none;">
                    <div class="service-icon" style="background: rgba({rgb}, 0.12); color: {color}"><i data-lucide="{icon}"></i></div>
                    <div class="service-details">
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                    <div class="service-arrow"><i data-lucide="chevron-right"></i></div>
                </a>
                '''

        services_sections_html += f'''
        <h2 class="section-subtitle"><i data-lucide="layers" style="color: var(--primary); width: 18px; height: 18px;"></i> {html.escape(category)}</h2>
        <div class="dashboard-grid">
            {cards_html}
        </div>
        '''

    return f'''
    <style>
        .hero-section {{
            text-align: center;
            padding: 4rem 1rem;
            margin-bottom: 2rem;
        }}
        .hero-section h1 {{
            font-size: clamp(2.5rem, 6vw, 4rem);
            font-weight: 800;
            letter-spacing: -1px;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #fff, #a5b4fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero-section p {{
            font-size: 1.25rem;
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto 2.5rem auto;
        }}
        .service-card {{
            padding: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1.25rem;
            position: relative;
        }}
        .service-card:hover {{
            border-color: var(--accent);
            transform: translateY(-2px);
            box-shadow: 0 10px 30px -10px rgba(0,0,0,0.5);
        }}
        .service-icon {{
            width: 52px;
            height: 52px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}
        .service-details h3 {{
            font-size: 1.15rem;
            color: white;
            margin-bottom: 0.35rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .service-details p {{
            font-size: 0.88rem;
            color: var(--text-muted);
        }}
        .service-arrow {{
            margin-left: auto;
            color: var(--text-subtle);
        }}
    </style>

    <main class="container">
        <section class="hero-section">
            <h1>QiSpark Workspace Command Center</h1>
            <p>Sanitized public surface for QiLabs systems, documentation, and live services.</p>
        </section>
        {services_sections_html}
    </main>
    '''


# ---------------------------------------------------------------------------
# Docs Layout & Component Styling
# ---------------------------------------------------------------------------
def render_docs_layout(
    sidebar_html: str,
    content_html: str,
    fm: dict[str, Any],
    rel_html_path: str = "",
    prev_doc: dict[str, Any] | None = None,
    next_doc: dict[str, Any] | None = None,
    base_path: str = "/"
) -> str:
    # Build Breadcrumbs
    parts = rel_html_path.replace("\\", "/").split("/")
    if parts and parts[0] == "docs":
        parts = parts[1:]
    
    crumb_items = ['<a href="' + base_path + 'docs/index.html"><i data-lucide="book-open"></i> Docs</a>']
    for idx, p in enumerate(parts[:-1]):
        crumb_name = text_to_title(p)
        crumb_items.append(f'<span>{html.escape(crumb_name)}</span>')
    if parts:
        crumb_items.append(f'<span class="active">{html.escape(text_to_title(parts[-1]))}</span>')
    
    breadcrumbs_html = f'<div class="doc-breadcrumbs">{" / ".join(crumb_items)}</div>'

    # Build Metadata Header
    metadata_html = ""
    meta_blocks = ""
    
    if fm.get("author"):
        meta_blocks += f'<span class="meta-pill"><i data-lucide="user"></i> {html.escape(str(fm["author"]))}</span>'
    if fm.get("status"):
        meta_blocks += f'<span class="meta-pill status-pill"><i data-lucide="tag"></i> {html.escape(str(fm["status"]))}</span>'
    if fm.get("updated_at") or fm.get("date"):
        dt_val = str(fm.get("updated_at") or fm.get("date"))
        meta_blocks += f'<span class="meta-pill"><i data-lucide="calendar"></i> {html.escape(dt_val)}</span>'

    # Estimate reading time
    read_time = estimate_reading_time(content_html)
    meta_blocks += f'<span class="meta-pill time-pill"><i data-lucide="clock"></i> {read_time}</span>'

    if meta_blocks:
        metadata_html = f'<div class="doc-meta-bar">{meta_blocks}</div>'

    # Pagination controls
    pagination_html = ""
    prev_html = ""
    next_html = ""
    if prev_doc:
        prev_url = html.escape(base_path + prev_doc["rel_html"], quote=True)
        prev_title = html.escape(prev_doc["nav_title"])
        prev_html = f'<a href="{prev_url}" class="doc-page-btn prev-btn"><span class="btn-sub">← Previous</span><span class="btn-title">{prev_title}</span></a>'
    if next_doc:
        next_url = html.escape(base_path + next_doc["rel_html"], quote=True)
        next_title = html.escape(next_doc["nav_title"])
        next_html = f'<a href="{next_url}" class="doc-page-btn next-btn"><span class="btn-sub">Next →</span><span class="btn-title">{next_title}</span></a>'

    if prev_html or next_html:
        pagination_html = f'<div class="doc-pagination">{prev_html}{next_html}</div>'

    return f"""
    <style>
        .docs-layout {{
            display: flex;
            min-height: calc(100vh - 69px);
        }}

        .sidebar {{
            width: var(--sidebar-width);
            border-right: 1px solid var(--card-border);
            background: rgba(8, 9, 13, 0.46);
            flex-shrink: 0;
            padding: 1.5rem 1rem;
            overflow-y: auto;
            position: sticky;
            top: 69px;
            height: calc(100vh - 69px);
        }}

        .sidebar-header {{
            margin-bottom: 1.25rem;
        }}

        .sidebar-title {{
            font-size: 0.78rem;
            font-weight: 760;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .sidebar-search-box {{
            width: 100%;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--card-border);
            border-radius: 8px;
            padding: 0.5rem 0.75rem;
            color: white;
            font-size: 0.85rem;
            margin-bottom: 0.75rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        .sidebar-search-box:focus {{
            border-color: var(--primary);
        }}

        .sidebar-controls {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }}

        .sidebar-controls button {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--card-border);
            color: var(--text-muted);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.35rem;
        }}
        .sidebar-controls button:hover {{
            color: white;
            background: rgba(255, 255, 255, 0.08);
        }}

        .doc-tree {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .tree-folder summary {{
            list-style: none;
            cursor: pointer;
            padding: 0.38rem 0.5rem;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.88rem;
            color: #cbd5e1;
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }}
        .tree-folder summary:hover {{
            background: rgba(255, 255, 255, 0.04);
            color: white;
        }}

        .folder-content {{
            padding-left: 0.85rem;
            margin-left: 0.5rem;
            border-left: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            gap: 0.15rem;
            margin-top: 0.25rem;
        }}

        .tree-item {{
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            padding: 0.35rem 0.6rem;
            border-radius: 6px;
            display: block;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            transition: all 0.15s ease;
        }}
        .tree-item:hover {{
            color: white;
            background: rgba(255, 255, 255, 0.04);
        }}
        .tree-item.active {{
            color: white;
            background: var(--primary-glow);
            border-left: 2px solid var(--primary);
            font-weight: 600;
        }}

        .content-area {{
            flex: 1;
            max-width: 960px;
            padding: 2.5rem 3rem;
            margin: 0 auto;
        }}

        .doc-breadcrumbs {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            color: var(--text-subtle);
            margin-bottom: 1.25rem;
        }}
        .doc-breadcrumbs a {{
            color: var(--text-muted);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}
        .doc-breadcrumbs a:hover {{
            color: white;
        }}
        .doc-breadcrumbs .active {{
            color: var(--primary);
        }}

        .doc-meta-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--card-border);
        }}

        .meta-pill {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--card-border);
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            font-size: 0.8rem;
            color: var(--text-muted);
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .markdown-body {{
            font-size: 1.05rem;
            color: #cbd5e1;
        }}

        .markdown-body h1 {{ font-size: 2.2rem; margin-bottom: 1.5rem; color: white; letter-spacing: -0.5px; }}
        .markdown-body h2 {{ font-size: 1.5rem; margin: 2rem 0 1rem 0; color: white; border-bottom: 1px solid var(--card-border); padding-bottom: 0.5rem; }}
        .markdown-body h3 {{ font-size: 1.25rem; margin: 1.5rem 0 0.75rem 0; color: #f1f5f9; }}
        .markdown-body p {{ margin-bottom: 1.25rem; }}
        .markdown-body ul, .markdown-body ol {{ margin-bottom: 1.25rem; padding-left: 1.5rem; }}
        .markdown-body li {{ margin-bottom: 0.4rem; }}
        .markdown-body code {{ background: rgba(255, 255, 255, 0.08); padding: 0.2rem 0.4rem; border-radius: 4px; font-size: 0.9em; font-family: monospace; color: #a5b4fc; }}
        .markdown-body pre {{ background: #0b0d17; border: 1px solid var(--card-border); padding: 1.25rem; border-radius: 12px; overflow-x: auto; margin-bottom: 1.5rem; position: relative; }}
        .markdown-body pre code {{ background: none; padding: 0; color: #e2e8f0; }}
        
        .copy-code-btn {{
            position: absolute;
            top: 8px;
            right: 8px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--card-border);
            color: var(--text-muted);
            padding: 0.25rem 0.5rem;
            border-radius: 6px;
            font-size: 0.72rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.3rem;
            transition: background 0.2s;
        }}
        .copy-code-btn:hover {{ background: rgba(255, 255, 255, 0.15); color: white; }}

        .markdown-alert {{
            padding: 1rem 1.25rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--primary);
            background: rgba(99, 102, 241, 0.08);
        }}
        .alert-title {{ font-weight: 700; display: flex; align-items: center; gap: 0.4rem; margin-bottom: 0.4rem; font-size: 0.95rem; }}
        .alert-note {{ border-color: #3b82f6; background: rgba(59, 130, 246, 0.08); }}
        .alert-tip {{ border-color: #10b981; background: rgba(16, 185, 129, 0.08); }}
        .alert-important {{ border-color: #a855f7; background: rgba(168, 85, 247, 0.08); }}
        .alert-warning {{ border-color: #f59e0b; background: rgba(245, 158, 11, 0.08); }}
        .alert-caution {{ border-color: #ef4444; background: rgba(239, 68, 68, 0.08); }}

        .doc-pagination {{
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            margin-top: 3.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--card-border);
        }}
        .doc-page-btn {{
            text-decoration: none;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 1rem 1.25rem;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
            transition: all 0.2s;
            max-width: 48%;
        }}
        .doc-page-btn:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
        }}
        .doc-page-btn.next-btn {{ margin-left: auto; text-align: right; }}
        .btn-sub {{ font-size: 0.78rem; color: var(--text-muted); text-transform: uppercase; font-weight: 600; }}
        .btn-title {{ font-size: 0.98rem; color: white; font-weight: 600; }}

        @media (max-width: 900px) {{
            .docs-layout {{ display: block; }}
            .sidebar {{ width: 100%; height: auto; position: static; border-right: none; border-bottom: 1px solid var(--card-border); }}
            .content-area {{ padding: 1.5rem; }}
        }}
    </style>

    <main class="docs-layout">
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title"><i data-lucide="book-open" style="width: 16px; height: 16px;"></i> Document Tree</div>
                <input type="text" class="sidebar-search-box" placeholder="Filter docs..." oninput="filterSidebar(this.value)" />
                <div class="sidebar-controls">
                    <button onclick="toggleAllDetails(true)"><i data-lucide="folder-open"></i> Expand All</button>
                    <button onclick="toggleAllDetails(false)"><i data-lucide="folder-closed"></i> Collapse All</button>
                </div>
            </div>
            <nav class="doc-tree">
                {sidebar_html}
            </nav>
        </aside>

        <section class="content-area">
            {breadcrumbs_html}
            {metadata_html}
            <div class="markdown-body">
                {content_html}
            </div>
            {pagination_html}
        </section>
    </main>
    """


# ---------------------------------------------------------------------------
# Sidebar Tree Builder
# ---------------------------------------------------------------------------
def build_sidebar(docs_list: list[dict[str, Any]], current_rel_path: str | None = None, base_path: str = "/") -> str:
    visible_docs = [doc for doc in docs_list if not doc.get("nav_hidden", False)]
    link_prefix = base_path

    root_node: dict[str, Any] = {"files": [], "dirs": {}}

    for doc in visible_docs:
        rel_html = doc["rel_html"]
        path_str = rel_html
        if path_str.startswith("docs/"):
            path_str = path_str[5:]
        elif path_str.startswith("docs\\"):
            path_str = path_str[5:]

        parts = path_str.replace("\\", "/").split("/")
        dir_parts = parts[:-1]

        current_node = root_node
        for part in dir_parts:
            if not part:
                continue
            current_node = current_node["dirs"].setdefault(part, {"files": [], "dirs": {}})

        current_node["files"].append(doc)

    def render_node(node: dict[str, Any], current_path: str | None, prefix: str) -> str:
        html_out = ""

        for dir_key in sorted(node["dirs"].keys()):
            child = node["dirs"][dir_key]
            display_name = dir_key
            if display_name.isdigit() or (len(display_name) > 2 and display_name[:2].isdigit()):
                display_name = re.sub(r"^\d+_", "", display_name)
            display_name = display_name.replace("_", " ").title()

            child_html = render_node(child, current_path, prefix)
            if not child_html.strip():
                continue

            is_open = False
            if current_path:
                norm_path = current_path.replace("\\", "/")
                path_parts = norm_path.split("/")[:-1]
                if dir_key in path_parts:
                    is_open = True

            open_attr = " open" if is_open else ""

            html_out += f"""
            <div class="tree-folder">
                <details{open_attr}>
                    <summary class="folder-header">
                        <i data-lucide="folder" style="width: 14px; height: 14px; color: var(--text-muted)"></i>
                        {html.escape(display_name)}
                    </summary>
                    <div class="folder-content">
                        {child_html}
                    </div>
                </details>
            </div>
            """

        sorted_files = sorted(
            node["files"],
            key=lambda x: (x.get("nav_order", 999), str(x.get("nav_title") or "").lower())
        )
        for f in sorted_files:
            is_active = current_path == f["rel_html"]
            active_class = " active" if is_active else ""
            html_out += f"""
            <a href="{html.escape(prefix + f['rel_html'], quote=True)}" class="tree-item{active_class}" title="{html.escape(f['nav_title'], quote=True)}">
                {html.escape(f['nav_title'])}
            </a>
            """

        return html_out

    return render_node(root_node, current_rel_path, link_prefix)


# ---------------------------------------------------------------------------
# Documentation Index Portal
# ---------------------------------------------------------------------------
def render_docs_index(docs_list: list[dict[str, Any]], sidebar_html: str, base_path: str = "/", site_title: str = "QiSpark") -> str:
    categories = {}
    for doc in docs_list:
        folder = doc.get("folder", "General Documentation")
        categories.setdefault(folder, []).append(doc)

    cat_cards_html = ""
    for cat_name, cat_docs in sorted(categories.items()):
        doc_links = ""
        for d in cat_docs[:5]:
            d_title = html.escape(d["nav_title"])
            d_url = html.escape(base_path + d["rel_html"], quote=True)
            doc_links += f'<li><a href="{d_url}"><i data-lucide="file-text" style="width:14px;height:14px;"></i> {d_title}</a></li>'

        more_count = len(cat_docs) - 5
        more_badge = f'<p class="cat-more">+{more_count} more documents</p>' if more_count > 0 else ""

        cat_cards_html += f"""
        <div class="glass-card doc-cat-card">
            <div class="cat-header">
                <h3><i data-lucide="folder-git2" style="color: var(--primary);"></i> {html.escape(cat_name)}</h3>
                <span class="cat-count">{len(cat_docs)} docs</span>
            </div>
            <ul class="cat-doc-list">
                {doc_links}
            </ul>
            {more_badge}
        </div>
        """

    index_body_html = f"""
    <style>
        .docs-portal-hero {{
            margin-bottom: 2.5rem;
        }}
        .docs-portal-hero h1 {{
            font-size: 2.4rem;
            color: white;
            margin-bottom: 0.75rem;
            letter-spacing: -0.5px;
        }}
        .docs-portal-hero p {{
            color: var(--text-muted);
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }}

        .portal-stats-bar {{
            display: flex;
            gap: 1rem;
            margin-bottom: 2.5rem;
        }}
        .portal-stat-pill {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--card-border);
            padding: 0.6rem 1.25rem;
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 0.92rem;
            color: var(--text-muted);
        }}
        .portal-stat-pill strong {{ color: white; font-size: 1.1rem; }}

        .doc-cat-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .doc-cat-card {{
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
        }}
        .cat-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--card-border);
        }}
        .cat-header h3 {{
            font-size: 1.1rem;
            color: white;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .cat-count {{
            background: rgba(99, 102, 241, 0.15);
            color: #a5b4fc;
            padding: 0.25rem 0.5rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .cat-doc-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}
        .cat-doc-list a {{
            color: #cbd5e1;
            text-decoration: none;
            font-size: 0.88rem;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            transition: color 0.15s;
        }}
        .cat-doc-list a:hover {{
            color: var(--primary);
        }}
        .cat-more {{
            margin-top: auto;
            padding-top: 0.75rem;
            font-size: 0.78rem;
            color: var(--text-subtle);
            font-style: italic;
        }}
    </style>

    <section class="docs-portal-hero">
        <h1>{html.escape(site_title)} Documentation Portal</h1>
        <p>Explore technical documentation, system specifications, standard operating procedures, and architectural blueprints.</p>
        <div class="portal-stats-bar">
            <div class="portal-stat-pill"><i data-lucide="book-open" style="color: var(--primary);"></i> Published Docs: <strong>{len(docs_list)}</strong></div>
            <div class="portal-stat-pill"><i data-lucide="folder" style="color: var(--accent-purple);"></i> Categories: <strong>{len(categories)}</strong></div>
        </div>
    </section>

    <h2 class="section-subtitle"><i data-lucide="layers" style="color: var(--primary);"></i> Documentation Taxonomy</h2>
    <div class="doc-cat-grid">
        {cat_cards_html}
    </div>
    """

    return render_docs_layout(
        sidebar_html=sidebar_html,
        content_html=index_body_html,
        fm={},
        rel_html_path="docs/index.html",
        base_path=base_path
    )


# ---------------------------------------------------------------------------
# Convert Markdown Files
# ---------------------------------------------------------------------------
def convert_md_files(
    source_dir: Path,
    dist_dir: Path,
    allow_active: bool = False,
    strict_publish: bool = False
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    docs_list: list[dict[str, Any]] = []
    docs_dir = dist_dir / "docs"

    stats = {
        "scanned": 0,
        "compiled": 0,
        "skipped": 0,
        "status_not_publishable": 0,
        "visibility_restricted": 0,
        "sensitivity_restricted": 0,
        "classification_restricted": 0,
        "explicit_flags_restricted": 0,
        "read_errors": 0
    }

    for root_dir, dirnames, files in os.walk(source_dir):
        root_path = Path(root_dir)

        dirnames[:] = [
            d for d in dirnames
            if not d.startswith(".") and d != "_qiconfig" and d not in TREE_SKIP_DIRS
        ]

        parts = root_path.relative_to(source_dir).parts
        if any(p.startswith(".") for p in parts) or "_qiconfig" in parts:
            continue

        for file_name in files:
            if not file_name.lower().endswith(".md"):
                continue

            full_path = root_path / file_name
            rel_path = full_path.relative_to(source_dir)
            stats["scanned"] += 1

            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
                stats["read_errors"] += 1
                stats["skipped"] += 1
                continue

            fm, body_text = parse_frontmatter(content)

            ok, reason = should_include(fm, allow_active, strict_publish)
            if not ok:
                stats["skipped"] += 1
                if "Status" in reason:
                    stats["status_not_publishable"] += 1
                elif "Visibility" in reason:
                    stats["visibility_restricted"] += 1
                elif "Sensitivity" in reason:
                    stats["sensitivity_restricted"] += 1
                elif "Classification" in reason:
                    stats["classification_restricted"] += 1
                elif "Explicit flag" in reason:
                    stats["explicit_flags_restricted"] += 1
                else:
                    stats["status_not_publishable"] += 1
                continue

            raw_html_body = markdown.markdown(
                body_text,
                extensions=["fenced_code", "tables", "nl2br", "toc"],
                output_format="html5",
            )

            html_body = process_markdown_alerts(raw_html_body)

            title = str(fm.get("title") or text_to_title(rel_path.name))
            slug = str(fm.get("slug") or slugify(title))

            rel_html_path = rel_path.with_suffix(".html")
            out_html_path = docs_dir / rel_html_path

            folder_name = rel_path.parts[0] if len(rel_path.parts) > 1 else ""
            if folder_name.isdigit() or (len(folder_name) > 2 and folder_name[:2].isdigit()):
                folder_name = re.sub(r"^\d+_", "", folder_name).replace("_", " ").title()
            elif folder_name:
                folder_name = folder_name.replace("_", " ").title()
            else:
                folder_name = "General Documentation"

            nav_title = fm.get("nav_title") or title
            nav_group = fm.get("nav_group") or folder_name

            try:
                nav_order = int(fm.get("nav_order", 999))
            except (ValueError, TypeError):
                nav_order = 999

            nav_hidden_val = fm.get("nav_hidden")
            if isinstance(nav_hidden_val, bool):
                nav_hidden = nav_hidden_val
            elif str(nav_hidden_val).lower() in ("yes", "true", "1"):
                nav_hidden = True
            else:
                nav_hidden = False

            is_index_val = fm.get("is_index")
            if is_index_val is not None:
                if isinstance(is_index_val, bool):
                    is_index = is_index_val
                else:
                    is_index = str(is_index_val).lower() in ("yes", "true", "1")
            else:
                is_index = rel_path.name.lower() in ("_index.md", "index.md")

            parent_ref = str(fm.get("parent_ref") or "")

            docs_list.append(
                {
                    "title": title,
                    "slug": slug,
                    "source_path": full_path,
                    "source_rel": rel_path.as_posix(),
                    "rel_html": "docs/" + rel_html_path.as_posix(),
                    "out_path": out_html_path,
                    "html_body": html_body,
                    "frontmatter": fm,
                    "folder": folder_name,
                    "nav_title": nav_title,
                    "nav_group": nav_group,
                    "nav_order": nav_order,
                    "nav_hidden": nav_hidden,
                    "is_index": is_index,
                    "parent_ref": parent_ref,
                }
            )
            stats["compiled"] += 1

    return docs_list, stats


# ---------------------------------------------------------------------------
# QiLabs Tree Page Helper
# ---------------------------------------------------------------------------
def should_skip_tree_path(path: Path, root: Path, include_hidden: bool) -> bool:
    name = path.name

    if not include_hidden and name.startswith("."):
        return True

    if path.is_dir():
        return name in TREE_SKIP_DIRS

    lowered = name.lower()
    if lowered in TREE_SKIP_FILE_NAMES:
        return True

    if path.suffix.lower() in TREE_SKIP_EXTENSIONS:
        return True

    return False


def build_doc_source_link_map(docs: list[dict[str, Any]], tree_root: Path) -> dict[str, str]:
    link_map: dict[str, str] = {}
    for doc in docs:
        source_path = normalize_path(Path(doc["source_path"]))
        try:
            rel_key = source_path.relative_to(tree_root).as_posix().lower()
            link_map[rel_key] = doc["rel_html"]
        except ValueError:
            pass
    return link_map


def render_manifest_node(node: dict[str, Any], docs: list[dict[str, Any]], base_path: str = "/") -> str:
    name = html.escape(node.get("name", "Untitled"))
    node_type = node.get("type", "file")

    if node_type == "directory":
        children = node.get("children", [])
        children_html = "".join(render_manifest_node(child, docs, base_path) for child in children)
        count = len(children)
        return f"""
        <li class="tree-dir">
            <details open>
                <summary class="tree-row">
                    <i data-lucide="folder"></i>
                    <span class="node-name">{name}</span>
                    <span class="node-count">{count}</span>
                </summary>
                <ul>{children_html}</ul>
            </details>
        </li>
        """
    elif node_type == "docs_root":
        doc_items_html = ""
        for doc in sorted(docs, key=lambda d: str(d.get("title")).lower()):
            doc_title = html.escape(doc.get("title", "Untitled"))
            doc_url = html.escape(base_path + doc.get("rel_html", ""), quote=True)
            doc_items_html += f"""
            <li class="tree-file linked">
                <a class="tree-row" href="{doc_url}">
                    <i data-lucide="file-text"></i>
                    <span class="node-name">{doc_title}</span>
                    <span class="node-badge">published</span>
                </a>
            </li>
            """
        if not doc_items_html.strip():
            doc_items_html = '<li class="tree-file"><span class="tree-row"><i data-lucide="info"></i><span class="node-name">No published documents</span></span></li>'

        return f"""
        <li class="tree-dir">
            <details open>
                <summary class="tree-row">
                    <i data-lucide="book-open"></i>
                    <span class="node-name">{name}</span>
                    <span class="node-count">{len(docs)}</span>
                </summary>
                <ul>{doc_items_html}</ul>
            </details>
        </li>
        """
    else:
        url = node.get("url")
        if url:
            if not (url.startswith("http://") or url.startswith("https://") or url.startswith("/")):
                url = base_path + url
            return f"""
            <li class="tree-file linked">
                <a class="tree-row" href="{html.escape(url, quote=True)}">
                    <i data-lucide="globe"></i>
                    <span class="node-name">{name}</span>
                </a>
            </li>
            """
        return f"""
        <li class="tree-file">
            <span class="tree-row">
                <i data-lucide="file"></i>
                <span class="node-name">{name}</span>
            </span>
        </li>
        """


def render_tree_page(
    manifest_path: Path,
    docs: list[dict[str, Any]],
    base_path: str = "/",
) -> str:
    manifest_data: dict[str, Any] = {}
    if manifest_path.exists() and manifest_path.is_file():
        try:
            with manifest_path.open("r", encoding="utf-8") as f:
                manifest_data = json.load(f)
        except Exception as e:
            print(f"Error loading tree manifest JSON: {e}")

    nodes = manifest_data.get("nodes", [])
    root_title = manifest_data.get("root_name", "QiLabs Public Surface")

    tree_html = "".join(render_manifest_node(node, docs, base_path) for node in nodes)

    return f"""
    <style>
        .tree-page {{ max-width: 1200px; }}
        .tree-hero {{ padding: 1.4rem; margin-bottom: 1.25rem; }}
        .tree-hero h1 {{ font-size: clamp(2rem, 5vw, 2.75rem); line-height: 1.05; letter-spacing: -1px; margin-bottom: 0.65rem; color: white; }}
        .tree-hero p {{ color: var(--text-muted); margin-bottom: 0.75rem; }}
        .tree-meta {{ display: flex; flex-wrap: wrap; gap: 0.6rem; }}
        .tree-pill {{ border: 1px solid var(--card-border); background: rgba(255, 255, 255, 0.04); color: #cbd5e1; padding: 0.35rem 0.65rem; border-radius: 999px; font-size: 0.82rem; }}
        .tree-panel {{ padding: 1rem; overflow-x: auto; }}
        .qilabs-tree, .qilabs-tree ul {{ list-style: none; }}
        .qilabs-tree ul {{ margin-left: 1.25rem; padding-left: 0.75rem; border-left: 1px solid rgba(255, 255, 255, 0.08); }}
        .qilabs-tree li {{ margin: 0.18rem 0; }}
        .tree-row {{ color: #cbd5e1; text-decoration: none; display: inline-flex; align-items: center; gap: 0.45rem; min-height: 1.75rem; padding: 0.2rem 0.45rem; border-radius: 999px; transition: background 0.15s, color 0.15s; }}
        .tree-row:hover {{ color: white; background: rgba(255, 255, 255, 0.045); }}
        .tree-row i {{ width: 16px; height: 16px; color: var(--text-muted); }}
        .tree-dir > details > summary {{ cursor: pointer; user-select: none; color: white; font-weight: 550; }}
        .tree-dir > details > summary::-webkit-details-marker {{ display: none; }}
        .tree-dir > details > summary::before {{ content: "▸"; color: var(--text-muted); display: inline-block; width: 0.8rem; transition: transform 0.15s; }}
        .tree-dir > details[open] > summary::before {{ transform: rotate(90deg); }}
        .tree-file .tree-row {{ font-size: 0.92rem; }}
        .tree-file.linked .tree-row {{ color: #a5b4fc; }}
        .node-name {{ white-space: nowrap; }}
        .node-count, .node-badge {{ color: var(--text-muted); background: rgba(255, 255, 255, 0.055); padding: 0.05rem 0.38rem; border-radius: 999px; font-size: 0.72rem; font-weight: 520; }}
        .node-badge {{ color: #c4b5fd; }}
        .tree-note {{ color: var(--text-muted); font-size: 0.85rem; margin-top: 1rem; }}
    </style>

    <main class="container tree-page">
        <section class="glass-card tree-hero">
            <h1>QiLabs Tree</h1>
            <p>Sanitized public manifest map of QiLabs systems and published documentation pages.</p>
            <div class="tree-meta">
                <span class="tree-pill">Surface: {html.escape(root_title)}</span>
                <span class="tree-pill">Generated: {html.escape(now_iso())}</span>
                <span class="tree-pill">Published Docs: {len(docs)}</span>
            </div>
        </section>

        <section class="glass-card tree-panel">
            <ul class="qilabs-tree">
                {tree_html}
            </ul>
            <p class="tree-note">Built strictly from explicit public architecture manifests. Unpublished filesystem directories are omitted.</p>
        </section>
    </main>
    """


# ---------------------------------------------------------------------------
# Main build entry point
# ---------------------------------------------------------------------------
def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    SCRIPT_DIR = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description="Static HTML documentation site builder for QiSpark.")
    parser.add_argument("--source", type=str, default=None, help="Read-only source markdown directory")
    parser.add_argument("--dist", type=str, default=None, help="Output static site directory")
    parser.add_argument("--tree-root", type=str, default=None, help="Root folder to render into dist/tree.html")
    parser.add_argument("--allow-active", action="store_true", help="Include active status files in documentation build")
    parser.add_argument("--strict-publish", action="store_true", help="Enforce strict public frontmatter tags (visibility=public, sensitivity=public, classification=public)")
    parser.add_argument("--no-tree", action="store_true", help="Skip generating dist/tree.html")
    parser.add_argument("--include-hidden-tree", action="store_true", help="Include hidden dot folders/files in the tree page")
    parser.add_argument("--config", type=str, default=None, help="Site config JSON path")
    parser.add_argument("--bookmarks-csv", type=str, default=None, help="Bookmarks CSV file path (overrides config)")
    parser.add_argument("--services-json", type=str, default=None, help="Services registry JSON path (overrides config)")
    parser.add_argument("--site-title", type=str, default=None, help="Overrides site title")
    parser.add_argument(
        "--base-path",
        type=str,
        default=None,
        help="URL base path for deployment (e.g. '/' for domain root). All internal links become absolute from this root.",
    )
    args = parser.parse_args()

    site_title = "QiSpark"
    source_path = DEFAULT_SOURCE
    dist_path = DEFAULT_DIST
    tree_root_path = DEFAULT_QILABS_ROOT
    base_path = "/"

    config_file = Path(args.config) if args.config else (SCRIPT_DIR / "00_config/site.config.json")
    if config_file.exists() and config_file.is_file():
        try:
            with config_file.open("r", encoding="utf-8") as f:
                site_conf = json.load(f)
                site_title = site_conf.get("site_title", site_title)
                source_path = Path(site_conf.get("default_source", str(source_path)))
                dist_path = Path(site_conf.get("default_dist", str(dist_path)))
                tree_root_path = Path(site_conf.get("default_tree_root", str(tree_root_path)))
                base_path = site_conf.get("base_path", base_path)
        except Exception as e:
            print(f"Error loading site config JSON: {e}")

    if args.site_title:
        site_title = args.site_title
    if args.source:
        source_path = Path(args.source)
    if args.dist:
        dist_path = Path(args.dist)
    if args.tree_root:
        tree_root_path = Path(args.tree_root)
    if args.base_path is not None:
        base_path = args.base_path

    base_path = base_path.strip()
    if not base_path.startswith("/"):
        base_path = "/" + base_path
    if not base_path.endswith("/"):
        base_path = base_path + "/"

    source_dir = normalize_path(source_path)
    dist_dir = normalize_path(dist_path)
    tree_root = normalize_path(tree_root_path)
    allow_active = args.allow_active
    strict_publish = args.strict_publish

    print(f"Building Static Site inside: {dist_dir}")
    print(f"Markdown Source, read-only: {source_dir}")
    print(f"QiLabs Tree Root: {tree_root}")
    print(f"Base Path: {base_path}")
    print(f"Allow active status files: {allow_active}")
    print(f"Strict publish filter: {strict_publish}")
    print(f"Site Title: {site_title}")
    print("-" * 72)

    filters_file = SCRIPT_DIR / "00_config/publish.filters.json"
    if filters_file.exists() and filters_file.is_file():
        try:
            with filters_file.open("r", encoding="utf-8") as f:
                pub_filters = json.load(f)
                global VALID_STATUSES, EXCLUDE_SENSITIVITY, EXCLUDE_CLASSIFICATION, EXCLUDE_FLAGS
                if "allowed_statuses" in pub_filters:
                    VALID_STATUSES = set(pub_filters["allowed_statuses"])
                if "exclude_sensitivity" in pub_filters:
                    EXCLUDE_SENSITIVITY = set(pub_filters["exclude_sensitivity"])
                if "exclude_classification" in pub_filters:
                    EXCLUDE_CLASSIFICATION = set(pub_filters["exclude_classification"])
                if "exclude_flags" in pub_filters:
                    EXCLUDE_FLAGS = list(pub_filters["exclude_flags"])
        except Exception as e:
            print(f"Error loading publish filters JSON: {e}")

    services = []
    services_file = Path(args.services_json) if args.services_json else (SCRIPT_DIR / "00_config/services.registry.json")
    if services_file.exists() and services_file.is_file():
        try:
            with services_file.open("r", encoding="utf-8") as f:
                services = json.load(f)
        except Exception as e:
            print(f"Error loading services registry JSON: {e}")

    if not services:
        services = [
            {"id": "qispark_docs", "title": "QiSpark Docs", "description": "Static documentation, specifications and system blueprints.", "url": "docs/index.html", "icon": "book-open", "color": "#38bdf8", "category": "Primary", "surface": ["public"], "status": "active"},
            {"id": "qilabs_tree", "title": "QiLabs Tree", "description": "Sanitized map of public workspace systems and documentation.", "url": "tree.html", "icon": "folder-tree", "color": "#14b8a6", "category": "Primary", "surface": ["public"], "status": "active"},
            {"id": "qisaysit", "title": "QiSaysIt", "description": "Public writing, posts and publishing surface.", "url": "https://qsaysit.com", "icon": "pencil-line", "color": "#10b981", "category": "Publishing", "surface": ["public"], "status": "active"},
            {"id": "qially", "title": "QiAlly", "description": "Primary QiAlly public domain hub.", "url": "https://qially.com", "icon": "globe", "color": "#3b82f6", "category": "Publishing", "surface": ["public"], "status": "active"}
        ]

    ensure_safe_build_paths(source_dir, dist_dir)
    safe_clean_dist(dist_dir)

    write_text(dist_dir / ".nojekyll", "")
    write_text(
        dist_dir / "build_manifest.json",
        json.dumps(
            {
                "generated_at": now_iso(),
                "source": str(source_dir),
                "dist": str(dist_dir),
                "tree_root": str(tree_root),
                "source_read_only_mode": True,
                "allow_active": allow_active,
                "strict_publish": strict_publish,
                "site_title": site_title
            },
            indent=2,
        ),
    )

    # Process Markdown documents
    docs, stats = convert_md_files(source_dir, dist_dir, allow_active=allow_active, strict_publish=strict_publish)
    print(f"Markdown files scanned: {stats['scanned']}")
    print(f"Published docs compiled: {stats['compiled']}")
    print(f"Skipped: {stats['skipped']}")

    docs_root_url = base_path + "docs/index.html"

    # Sort docs by title/folder for prev/next
    docs.sort(key=lambda d: (d.get("folder", ""), d.get("nav_order", 999), d.get("nav_title", "")))

    # Generate individual docs pages
    for idx, doc in enumerate(docs):
        doc_sidebar = build_sidebar(docs, doc["rel_html"], base_path=base_path)
        home_path = base_path + "index.html"
        tree_path = base_path + "tree.html"

        prev_doc = docs[idx - 1] if idx > 0 else None
        next_doc = docs[idx + 1] if idx < len(docs) - 1 else None

        page_html = make_header(doc["title"], home_path, docs_root_url, tree_path, site_title=site_title)
        page_html += render_docs_layout(
            sidebar_html=doc_sidebar,
            content_html=doc["html_body"],
            fm=doc["frontmatter"],
            rel_html_path=doc["rel_html"],
            prev_doc=prev_doc,
            next_doc=next_doc,
            base_path=base_path
        )
        page_html += HTML_FOOTER

        write_text(doc["out_path"], page_html)

    # Generate docs index page
    docs_idx_path = dist_dir / "docs" / "index.html"
    docs_idx_sidebar = build_sidebar(docs, "docs/index.html", base_path=base_path)
    docs_index = make_header("QiSpark Documentation Portal", base_path + "index.html", docs_root_url, base_path + "tree.html", site_title=site_title)
    docs_index += render_docs_index(docs, docs_idx_sidebar, base_path=base_path, site_title=site_title)
    docs_index += HTML_FOOTER
    write_text(docs_idx_path, docs_index)

    # Generate QiLabs tree page
    if not args.no_tree:
        tree_manifest_file = SCRIPT_DIR / "00_config/tree.manifest.json"
        tree_page = make_header("QiLabs Tree", base_path + "index.html", docs_root_url, base_path + "tree.html", site_title=site_title)
        tree_page += render_tree_page(
            manifest_path=tree_manifest_file,
            docs=docs,
            base_path=base_path,
        )
        tree_page += HTML_FOOTER
        write_text(dist_dir / "tree.html", tree_page)
        print(f"Generated QiLabs tree: {dist_dir / 'tree.html'}")

    # Generate homepage
    dashboard_html = make_header(site_title, base_path + "index.html", docs_root_url, base_path + "tree.html", site_title=site_title)
    dashboard_html += render_landing(services, docs_root_url, base_path + "tree.html")
    dashboard_html += HTML_FOOTER
    write_text(dist_dir / "index.html", dashboard_html)

    print()
    print("=" * 72)
    print("Static Site Build Complete!")
    print(f"Homepage: {dist_dir / 'index.html'}")
    print(f"Docs:     {dist_dir / 'docs' / 'index.html'}")
    print(f"Tree:     {dist_dir / 'tree.html'}")
    print("=" * 72)


if __name__ == "__main__":
    main()
