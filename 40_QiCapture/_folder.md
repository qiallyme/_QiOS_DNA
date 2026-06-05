# QiCapture

## Overview

QiCapture is the intake, ingestion, review, and approval layer. It protects raw input while turning it into usable QiLife records.

Raw capture is sacred. AI interpretation is a draft until approved or trusted by explicit rules.

## Responsibilities

- Fast intake of raw thoughts, files, notes, messages, and documents.
- Preserve original capture text or source files.
- Create ingestion items.
- Run extraction or inspection.
- Produce draft interpretations.
- Support approve, edit, or reject review actions.
- Hand official records to QiLife.

## Flows

```text
Raw capture
  -> ingestion item
  -> extraction
  -> AI draft
  -> review
  -> approve, edit, or reject
  -> QiBit, Action, or Thread
```

## Structure

QiCapture records distinguish raw capture, ingestion item, extracted text or metadata, AI draft, review decision, official QiLife object, and timeline/activity log entry.

