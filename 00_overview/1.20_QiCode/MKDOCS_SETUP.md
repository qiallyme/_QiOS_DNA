# MkDocs Setup Guide for QiCode

This directory now includes MkDocs configuration to generate a wiki-style documentation site similar to the Indiana Code website.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or if using a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Preview the Site

Start the development server:

```bash
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`

### 3. Build the Site

Generate static HTML files:

```bash
mkdocs build
```

The output will be in the `site/` directory (which is gitignored).

## Configuration

The `mkdocs.yml` file contains:

- **Material Theme**: Modern, wiki-like appearance with light/dark mode
- **Navigation Structure**: Organized by Titles with expandable sections
- **Search**: Full-text search enabled
- **Extensions**: Various Markdown extensions for tables, code blocks, etc.

## Site Structure

- **Homepage**: `index.md` (serves as the main landing page)
- **Navigation**: Configured in `mkdocs.yml` nav section
- **Source Files**: All markdown files in the current directory (except excluded files)

## Customization

### Update Navigation

When adding new Principles, update the `nav:` section in `mkdocs.yml`:

```yaml
nav:
  - Title I — Foundations:
    - Title I Overview: 1.21_Title_Foundations/1.21.00_Title_Index.md
    - §1 Principle of Awareness: 1.21_Title_Foundations/1.21.1_Principle_of_Awareness.md
    - §2 Principle of Presence: 1.21_Title_Foundations/1.21.2_Principle_of_Presence.md
    - §3 New Principle: 1.21_Title_Foundations/1.21.3_New_Principle.md  # Add new entries here
```

### Change Theme Colors

Edit the `palette:` section in `mkdocs.yml`:

```yaml
theme:
  palette:
    - scheme: default
      primary: indigo  # Change to blue, green, red, etc.
```

### Deploy

#### GitHub Pages

1. Push the repository to GitHub
2. Enable GitHub Pages in repository settings
3. Run `mkdocs gh-deploy` (requires `mkdocs-git-revision-date-plugin` if adding dates)

#### Other Hosting

Upload the contents of the `site/` directory to any static hosting service:
- Netlify
- Vercel
- AWS S3 + CloudFront
- Any web server

## Troubleshooting

### Port Already in Use

If port 8000 is busy:

```bash
mkdocs serve -a 127.0.0.1:8080
```

### Missing Dependencies

If you see import errors:

```bash
pip install --upgrade -r requirements.txt
```

### Navigation Not Updating

After adding new files, ensure they're:
1. Added to the `nav:` section in `mkdocs.yml`
2. Not in the `exclude_docs:` list
3. Saved with `.md` extension

## Features

- ✅ Material Design theme (wiki-like appearance)
- ✅ Light/Dark mode toggle
- ✅ Full-text search
- ✅ Mobile-responsive
- ✅ Table of contents on each page
- ✅ Navigation tabs and sections
- ✅ Code syntax highlighting
- ✅ Table support
- ✅ Footnotes support

## Next Steps

1. Run `mkdocs serve` to preview
2. Customize colors/theme in `mkdocs.yml` if desired
3. Add any missing navigation entries
4. Deploy to your preferred hosting service

