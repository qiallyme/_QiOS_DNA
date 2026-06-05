# QiSystem

## Overview

QiSystem is the operational integrity layer. It tracks evidence that the system is running correctly and keeps generated operational material separate from product, portal, and doctrine docs.

## Responsibilities

- Logs and operational records.
- Audits and validation outputs.
- Backup and restore references.
- Health checks and verification results.
- Generated reports.
- Generated indexes and inventories.
- Maintenance notes and cleanup tasks.

## Flows

```text
Runtime or service check
  -> health result
  -> audit or generated report
  -> maintenance action if needed
  -> retained QiSystem record
```

## Structure

QiSystem may contain physical subfolders for real operational records when needed. Each subfolder must contain its own `_folder.md` when created.

