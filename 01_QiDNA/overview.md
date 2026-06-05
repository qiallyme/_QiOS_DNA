# QiDNA Overview

QiDNA is the governance and documentation layer for the Qi system. It defines the mirror rule: documentation must live in the same layer as the thing it describes.

The active system model is:

```text
QiAccess -> QiLife -> (QiSystem + QiNexus + QiCapture + QiConnect)
```

QiDNA does not replace the system layers. It names them, keeps their boundaries clear, and holds system-level doctrine in `01_QiDNA/QiEOS/`.

## Active Layers

- `10_QiAccess`: the portal and navigation shell.
- `20_QiSystem`: operational integrity and generated system evidence.
- `30_QiServer`: runtime host for protected services.
- `40_QiCapture`: intake and review pipeline.
- `50_QiNexus`: folder discipline and storage backbone.
- `60_QiApp_QiLife`: the private life operating app.
- `70_QiConnect`: integrations and access boundaries.
