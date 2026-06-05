# QiCapture Flows

## Capture Review Flow

```text
Raw capture
  -> ingestion item
  -> file or text extraction
  -> mock or real AI draft
  -> review
  -> approve, edit, or reject
  -> QiBit, Action, or Thread
  -> Timeline and Activity Log
```

## Document Ingestion Flow

```text
Source file
  -> drop zone or watch path
  -> local agent detect
  -> resolve domain
  -> register canonical ID
  -> extract or OCR
  -> enrich metadata
  -> chunk
  -> embed
  -> index
  -> route, review, and act
```

High-risk areas such as money, legal, medical, deletion, and messaging require review.
