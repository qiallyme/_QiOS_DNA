# Site

## Overview

`site/` contains the single-page system mirror viewer.

## Responsibilities

- Render all active `_folder.md` files into one scrollable HTML page.
- Provide a location-based navigation tree.
- Preserve the physical folder hierarchy visually.

## Flows

```text
Open site/index.html
  -> navigation tree loads
  -> click folder link
  -> scroll to matching rendered _folder.md section
```

## Structure

```text
site/
├── _folder.md
├── index.html
├── script.js
└── style.css
```

