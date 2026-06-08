# QiDNA

## Overview

QiDNA is the governance and documentation layer for the Qi system. It defines the mirror rule: documentation must live in the same layer as the thing it describes.

The active system model is:

```text
QiAccess -> QiLife -> (QiSystem + QiNexus + QiCapture + QiConnect)
```

QiDNA names system layers, keeps their boundaries clear, and holds system-level doctrine in `01_QiDNA/QiEOS/`.

## Responsibilities

- Maintain the mirrored documentation structure.
- Keep system-layer names stable.
- Hold doctrine, philosophy, decisions, and system reasoning in `QiEOS/`.
- Prevent duplicate or conflicting source-of-truth documents.
- Record the active system model clearly and consistently.

## Flows

```text
Question
  -> identify the system layer
  -> open the matching folder
  -> read _folder.md
```

Runtime facts beat planning notes. Active mirrored docs beat legacy documents. QiEOS explains why, but each layer owns its operating details.

## Structure

```text
01_QiDNA/
├── _folder.md
└── QiEOS/
    └── _folder.md
```

