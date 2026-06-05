# QiOS DNA Repository

## Overview

QiOS DNA is the mirrored documentation filesystem for the live Qi system.

The active model is:

```text
QiAccess -> QiLife -> (QiSystem + QiNexus + QiCapture + QiConnect)
```

## Responsibilities

- Keep every physical folder documented by exactly one `_folder.md`.
- Keep documentation location-based.
- Keep active system-layer names stable.
- Keep the single-page mirror viewer in `site/`.

## Flows

```text
System folder -> matching QiDNA folder -> _folder.md
```

## Structure

Active system folders:

- `01_QiDNA`
- `10_QiAccess`
- `20_QiSystem`
- `30_QiServer`
- `40_QiCapture`
- `50_QiNexus`
- `60_QiApp_QiLife`
- `70_QiConnect`

The `site/` folder contains the single-page system mirror viewer.

