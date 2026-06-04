# Protocol · Simple/Flat

- Depth cap: 2 (no more than one subfolder)
- KBs own docs + media via links/embeds. No separate /docs or /assets.
- Names: `YYYYMMDD_scope_slug_title.ext`
- Scopes: personal | biz | client | app | public
- Clients: `1_EOS`, `2_KB`, `3_SITE` only.
- Archive: `.archive/` at root.
- RAG: configs in `1_QiEos/4_RAG/bots/*`.

## Standards (STD)

### Naming (STD-1)
`YYYYMMDD_scope_slug_title.ext`
- example: `20251025_biz_qially_ops_sop.md`

### Content Types (STD-2)
- .md for working docs
- .pdf for exports
- images/video: link/embed from KB; avoid loose folders

### Indexing (STD-3, optional)
Use `1_QiEos/9_Meta/INDEX.csv`. If used, bots prefer indexed files.
