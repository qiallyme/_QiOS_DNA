const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

// --- Configuration ---
const ROOT_DIR = __dirname;
const OUT_DIR = path.join(ROOT_DIR, 'site');
const OUT_FILE = path.join(OUT_DIR, 'index.html');

// Directories to ignore
const EXCLUDE_DIRS = new Set(['node_modules', 'site', '.git', '.github']);

// --- File Discovery ---
function findMarkdownFiles(dir, fileList = []) {
    const items = fs.readdirSync(dir, { withFileTypes: true });
    
    for (const item of items) {
        const fullPath = path.join(dir, item.name);
        
        if (item.isDirectory()) {
            if (!EXCLUDE_DIRS.has(item.name) && !item.name.startsWith('.')) {
                findMarkdownFiles(fullPath, fileList);
            }
        } else if (item.isFile() && item.name.startsWith('_') && item.name.endsWith('.md')) {
            fileList.push(fullPath);
        }
    }
    
    return fileList;
}

// --- Content Processing ---
function processFiles(files) {
    const sections = [];
    
    for (const file of files) {
        const content = fs.readFileSync(file, 'utf-8');
        const htmlContent = marked.parse(content);
        
        const fileName = path.basename(file, '.md');
        const cleanName = fileName.replace(/^_+/, ''); 
        const title = cleanName.replace(/_/g, ' ');    
        const id = cleanName.toLowerCase().replace(/[^a-z0-9]+/g, '-'); 

        sections.push({ id, title, htmlContent, sourceFile: file, originalName: cleanName });
    }
    
    sections.sort((a, b) => a.originalName.localeCompare(b.originalName));
    return sections;
}

// --- HTML Generation ---
function generateHTML(sections) {
    const navLinks = sections.map(section => 
        `<li><a href="#${section.id}" class="nav-link">${section.title}</a></li>`
    ).join('\n');

    const contentSections = sections.map(section => `
        <section id="${section.id}" class="doc-section">
            ${section.htmlContent}
        </section>
    `).join('\n');

    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentation</title>
    <style>
        :root {
            --bg-color: #f4f4f5;
            --card-bg: #ffffff;
            --text-main: #3f3f46;
            --text-heading: #18181b;
            --sidebar-bg: #fafafa;
            --sidebar-border: #e4e4e7;
            --accent: #0284c7;
            --accent-hover: #0369a1;
            --accent-light: #e0f2fe;
            --code-bg: #f1f5f9;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            --header-height: 60px;
        }

        * { box-sizing: border-box; }

        html { 
            scroll-behavior: smooth; 
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        body {
            margin: 0; padding: 0;
            display: flex;
            color: var(--text-main);
            background-color: var(--bg-color);
            line-height: 1.6;
        }

        /* Mobile Header */
        #mobile-header {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0;
            height: var(--header-height);
            background: var(--card-bg);
            border-bottom: 1px solid var(--sidebar-border);
            z-index: 900;
            align-items: center;
            padding: 0 1.5rem;
            box-shadow: var(--shadow);
        }

        #menu-btn {
            background: none; border: none;
            font-size: 1.5rem; color: var(--text-heading);
            cursor: pointer; padding: 0.5rem;
            margin-left: -0.5rem; margin-right: 1rem;
        }

        #mobile-header h1 {
            font-size: 1.25rem; margin: 0; color: var(--text-heading);
        }

        /* Sidebar Navigation */
        #sidebar-overlay {
            display: none; position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.5); z-index: 950;
            opacity: 0; transition: opacity 0.3s;
        }

        nav {
            width: 280px; height: 100vh;
            position: fixed; top: 0; left: 0;
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--sidebar-border);
            overflow-y: auto; z-index: 1000;
            padding: 2rem 1.5rem;
            transition: transform 0.3s ease;
        }

        nav h1 {
            font-size: 1.25rem; color: var(--text-heading);
            margin: 0 0 1.5rem 0; padding-bottom: 1rem;
            border-bottom: 1px solid var(--sidebar-border);
        }

        nav ul { list-style: none; padding: 0; margin: 0; }
        nav li { margin-bottom: 0.25rem; }

        nav a {
            text-decoration: none; color: var(--text-main);
            font-size: 0.95rem; font-weight: 500;
            display: block; padding: 0.5rem 0.75rem;
            border-radius: 6px; transition: all 0.2s;
        }

        nav a:hover { background-color: var(--sidebar-border); }
        
        /* Active State for Navigation */
        nav a.active {
            background-color: var(--accent-light);
            color: var(--accent);
            border-left: 4px solid var(--accent);
            padding-left: calc(0.75rem - 4px);
        }

        /* Main Content Area */
        main {
            margin-left: 280px;
            padding: 3rem;
            width: 100%;
            display: flex;
            justify-content: center;
        }

        .content-wrapper {
            max-width: 800px;
            width: 100%;
        }

        .doc-section {
            background: var(--card-bg);
            padding: 2.5rem 3rem;
            margin-bottom: 2rem;
            border-radius: 12px;
            box-shadow: var(--shadow);
            border: 1px solid var(--sidebar-border);
            scroll-margin-top: 2rem;
        }

        /* Typography */
        h1, h2, h3, h4 { color: var(--text-heading); margin-top: 1.5rem; font-weight: 600; }
        .doc-section > h1:first-child, .doc-section > h2:first-child { margin-top: 0; }
        h1 { font-size: 2rem; border-bottom: 2px solid var(--sidebar-border); padding-bottom: 0.5rem; }
        h2 { font-size: 1.5rem; }
        
        a { color: var(--accent); text-decoration: none; }
        a:hover { text-decoration: underline; }

        code {
            background-color: var(--code-bg); padding: 0.2em 0.4em;
            border-radius: 4px; font-family: ui-monospace, monospace; font-size: 0.9em;
        }
        pre {
            background-color: var(--text-heading); color: #f8fafc;
            padding: 1.25rem; border-radius: 8px; overflow-x: auto;
        }
        pre code { background-color: transparent; color: inherit; padding: 0; }

        blockquote {
            border-left: 4px solid var(--accent);
            background: var(--accent-light);
            margin: 1.5rem 0; padding: 1rem 1.5rem;
            border-radius: 0 8px 8px 0; color: #0c4a6e;
        }

        /* Back to Top Button */
        #back-to-top {
            position: fixed; bottom: 2rem; right: 2rem;
            background: var(--accent); color: white;
            width: 3rem; height: 3rem; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            border: none; cursor: pointer;
            box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);
            opacity: 0; visibility: hidden;
            transition: all 0.3s; transform: translateY(10px);
            z-index: 800;
        }
        #back-to-top.visible {
            opacity: 1; visibility: visible; transform: translateY(0);
        }
        #back-to-top:hover { background: var(--accent-hover); transform: translateY(-3px); }

        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            #mobile-header { display: flex; }
            nav h1 { display: none; } /* Hide duplicate title in sidebar on mobile */
            
            nav {
                transform: translateX(-100%);
                padding-top: var(--header-height);
            }
            nav.open { transform: translateX(0); }
            
            #sidebar-overlay.open { display: block; opacity: 1; }

            main { margin-left: 0; padding: 1rem; padding-top: calc(var(--header-height) + 1rem); }
            .doc-section { padding: 1.5rem; border-radius: 8px; scroll-margin-top: calc(var(--header-height) + 1rem); }
            
            #back-to-top { bottom: 1.5rem; right: 1.5rem; }
        }
    </style>
</head>
<body>

    <div id="mobile-header">
        <button id="menu-btn" aria-label="Toggle Menu">☰</button>
        <h1>Documentation</h1>
    </div>

    <div id="sidebar-overlay"></div>

    <nav id="sidebar">
        <h1>Documentation</h1>
        <ul>${navLinks}</ul>
    </nav>

    <main>
        <div class="content-wrapper">
            ${contentSections}
        </div>
    </main>

    <button id="back-to-top" aria-label="Back to Top">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Mobile Menu Toggle Logic
            const menuBtn = document.getElementById('menu-btn');
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('sidebar-overlay');
            const navLinks = document.querySelectorAll('.nav-link');

            function toggleMenu() {
                const isOpen = sidebar.classList.contains('open');
                if (isOpen) {
                    sidebar.classList.remove('open');
                    overlay.classList.remove('open');
                    document.body.style.overflow = ''; // Restore scrolling
                } else {
                    sidebar.classList.add('open');
                    overlay.classList.add('open');
                    document.body.style.overflow = 'hidden'; // Prevent background scrolling
                }
            }

            menuBtn.addEventListener('click', toggleMenu);
            overlay.addEventListener('click', toggleMenu);
            
            // Close menu when a link is clicked (on mobile)
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) toggleMenu();
                });
            });

            // Back to Top Button Logic
            const backToTopBtn = document.getElementById('back-to-top');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 300) {
                    backToTopBtn.classList.add('visible');
                } else {
                    backToTopBtn.classList.remove('visible');
                }
            });

            backToTopBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });

            // Scroll Spy (Highlight active section in sidebar)
            const sections = document.querySelectorAll('.doc-section');
            const observerOptions = {
                root: null,
                rootMargin: '-20% 0px -60% 0px', // Triggers when section is roughly in the top third of screen
                threshold: 0
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.getAttribute('id');
                        
                        // Remove active class from all links
                        navLinks.forEach(link => link.classList.remove('active'));
                        
                        // Add active class to the current link
                        const activeLink = document.querySelector(\`.nav-link[href="#\${id}"]\`);
                        if (activeLink) {
                            activeLink.classList.add('active');
                            
                            // Ensure the active link is visible in the sidebar scroll area
                            activeLink.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                        }
                    }
                });
            }, observerOptions);

            sections.forEach(section => observer.observe(section));
        });
    </script>
</body>
</html>`;
}

// --- Main Execution ---
function build() {
    console.log('🚀 Starting documentation build...');
    
    if (!fs.existsSync(OUT_DIR)) {
        fs.mkdirSync(OUT_DIR, { recursive: true });
    }

    const mdFiles = findMarkdownFiles(ROOT_DIR);
    if (mdFiles.length === 0) {
        console.warn('⚠️ No markdown files matching "_*.md" were found.');
    } else {
        console.log(`📄 Found ${mdFiles.length} documentation files.`);
    }

    const sections = processFiles(mdFiles);
    const finalHtml = generateHTML(sections);

    fs.writeFileSync(OUT_FILE, finalHtml);
    console.log(`✅ Build complete! Site generated at: ${OUT_FILE}`);
}

build();
