# QiDNA and Implementation Reconciliation

## Scope

Audit date: 2026-06-10.

Inspected evidence included all tracked paths; active `01-70` descriptors; doctrine, schema summaries, decisions, module docs, workflows, deployment notes, build scripts, and project receipts. Binary personal-media imports were inventoried by path but were not treated as architecture documents.

No Supabase migrations, `supabase/config.toml`, SQL schema, or connected Supabase project was available. No claim about a live Supabase schema is made.

## Extracted System Model

### Domains and Boundaries

| Domain | Responsibility | Boundary |
|---|---|---|
| QiDNA | Governance, schema, decisions, reconciliation | Does not own runtime operations |
| QiAccess | Portal, navigation, daily entry point | Does not own service runtime or product data |
| QiSystem | Audits, health, generated operational records | Does not own portal or app behavior |
| QiServer | Host, stacks, services, routes, backups | Runtime facts override repo plans |
| QiCapture | Raw intake, extraction, AI draft, review handoff | Raw evidence remains preserved |
| QiNexus | Durable files, exports, reference, archive | Not the relational database |
| QiApp QiLife | Structured life ledger and operating app | Does not own system doctrine |
| QiConnect | External APIs, connectors, access boundaries | Does not own target services or data models |

### Entities

Documented QiLife entities are `qibits`, `buckets`, `threads`, `actions`, `action_steps`, `people`, `transactions`, `obligations`, `knowledge_items`, `documents`, `events`, `links`, `activity_log`, `ai_outputs`, and `daily_summaries`.

Capture entities are raw capture, ingestion item, extracted content, AI draft, review decision, accepted QiLife record, and activity entry.

Infrastructure entities include host, stack, service, route, access class, backup, health result, audit, and generated report.

### Relationships

- Raw capture becomes an ingestion item and may produce an AI draft.
- An approved draft creates or updates a QiLife entity.
- `links` preserves provenance between QiBits and derived records.
- Threads group QiBits, actions, documents, transactions, obligations, and people.
- Timeline projects timestamped entities; it is not a canonical table.
- QiLife metadata links to files governed by QiNexus.
- QiConnect routes external requests to protected QiServer services.

### Flows

```text
Capture -> Extract -> Draft -> Review -> Approve/Edit/Reject -> QiLife -> Timeline
QiAccess -> tool or service -> QiServer route -> application
Canonical Markdown -> npm run build -> site/index.html
```

## Findings and Recommendations

| Finding | Recommendation | Reasoning |
|---|---|---|
| New `01_QiDNA` docs and older `00_QiEOS` docs define competing root models | MERGE | Consolidate active doctrine around one `01-70` vocabulary and mark historical roots as legacy aliases |
| QiAccess appears as `10_QiAccess`, `10_QiOS_Start`, and `60_qiapps/qiaccess_start` | MERGE | These describe one front-door capability at different stages |
| QiLife appears under `60_QiApp_QiLife`, `60_QiApps/QiLife`, `50_modules`, and `60_ai_layer` | MERGE | Keep one owning domain and integrate useful app detail without duplicate authority |
| QiNexus appears as `50_QiNexus` and legacy `20_qinexus` | MERGE | Uppercase numbered domain matches the active model |
| QiConnect appears as `70_QiConnect` and `70_qiconnect` | MERGE | Workflow detail belongs under the active QiConnect boundary |
| QiServer docs are split between `30_QiServer` and `50_qiserver` | MERGE | Runbooks should live with the active runtime domain |
| Data doctrine mixes SQLite, legacy Supabase, and QiNexus storage | UPDATE | Apply ADR-0012 and state database versus file-storage roles explicitly |
| Folder descriptors are missing or named `_index.md` or `index.mdx` | ADD | Add one descriptor only when a folder is retained as governed structure |
| Imported personal-media paths exceed four levels | UPDATE | Classify them as imported evidence; flatten only through a separate reviewed migration |
| The HTML build required a moved report at its old path | UPDATE | Keep build validation synchronized with canonical source paths |
| Node HTML and Python chronicle builds overlap | UPDATE | Keep HTML as the reader; label chronicle and manifest as secondary generated artifacts |
| `docs.json` still navigates the older root model | UPDATE | Align it if Mintlify remains in use; otherwise remove it in reviewed cleanup |
| Source-of-truth rules rank doctrine above implemented schema | UPDATE | Doctrine governs intent; verified runtime and migrations govern implemented facts |
| No Supabase schema is available | ADD | Add an actual schema snapshot when obtained; do not reconstruct it from prose |
| Empty placeholder folders exist in active domains | DELETE | Remove only after confirming no external dependency; this audit performs no deletion |

## Suggested Structural Updates

These are proposals, not executed moves or deletions.

1. MERGE `10_QiOS_Start/QiAccess_Start` and reviewed `60_qiapps/qiaccess_start` material into `10_QiAccess`.
2. MERGE `60_QiApps/QiLife`, `60_ai_layer`, relevant `50_modules`, and QiLife deployment docs into `60_QiApp_QiLife`.
3. MERGE `50_qiserver/qiserver_runbook.md` into `30_QiServer`.
4. MERGE `70_qiconnect/06_workflows` into `70_QiConnect`.
5. MERGE reviewed `20_qinexus` content into `50_QiNexus`.
6. UPDATE `00_QiEOS` doctrine and `docs.json` to identify the current model or label them legacy.
7. DELETE empty placeholders and redundant legacy roots only after reviewed merges.

## Unknowns

- The live QiLife repository and its actual SQLite migrations were not present.
- The legacy Supabase schema and project configuration were unavailable.
- Runtime components were described by receipts but not re-verified in this repository-only audit.
- The intended disposition of the tracked personal-media import is unstated.
