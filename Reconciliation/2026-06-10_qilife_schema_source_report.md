# QiLife Schema Source Report

## Scope

Assessment date: 2026-06-10.

This audit performed three targeted searches for the actual QiLife implementation schema. Dependency, build, cache, virtual-environment, Git, and generated-site directories were excluded.

## Result

The actual QiLife database or implementation schema was **not found**.

The expected local application repositories are missing:

```text
/home/qiadmin/qi_workspace/qilife
/home/qiadmin/qi_workspace/QiLife
```

No separate QiLife application repository was found under:

```text
/home/qiadmin/qi_workspace
/srv/qios/apps
/srv/qios/repos
/home/qiadmin
```

## Sources Found

### QiLife Documentation Only

```text
/home/qiadmin/qi_workspace/_QiOS_DNA/60_QiApp_QiLife
/home/qiadmin/qi_workspace/_QiOS_DNA/60_QiApps/QiLife
```

These locations contain documentation, not executable database definitions.

### Unrelated SQL

```text
/srv/qios/apps/_QiAccess_Start/worker/schema.sql
/srv/qios/repos/_QiAccess_Start/worker/schema.sql
```

These files belong to the QiAccess worker and are not evidence of the QiLife schema.

### Schema Types Found

| Schema type | Found for QiLife |
|---|---|
| SQLite database file | No |
| SQL migrations | No |
| ORM models | No |
| API models | No |
| Database initialization code | No |
| Documentation-only schema | Yes |

## Documented Entities Discovered

The active QiDNA data spine and governing documents name these intended entities:

```text
qibits
buckets
threads
actions
action_steps
people
transactions
obligations
knowledge_items
documents
events
links
activity_log
ai_outputs
daily_summaries
```

These names are documented intent and must not be treated as proof that matching tables exist.

## Alignment With ADR-0017

The documentation-only model is directionally consistent with ADR-0017:

- SQLite is identified as the intended current structured-data authority.
- QiNexus remains file, export, reference, and archive storage.
- Supabase remains legacy import or possible future integration.
- The named entities support the manual-first v1 workflows.

Implementation compliance cannot be verified because no SQLite database, migration history, ORM model, or initialization code was found.

## What Is Still Missing

- The actual QiLife application repository and current commit.
- The runtime `qilife.sqlite` file or a read-only schema dump.
- SQL migration history, if migrations exist.
- ORM or database model definitions.
- Database creation and initialization code.
- The canonical runtime database path.

## Next Exact Step

Provide or restore the actual QiLife implementation repository and identify its path. The preferred expected path is:

```text
/home/qiadmin/qi_workspace/qilife
```

If the repository exists elsewhere, provide that exact path. It must contain at least one verified schema source: the SQLite database, a `.schema` dump, migrations, ORM models, or database initialization code.

Database blueprint work remains blocked until that source is available. No schema should be invented from the documentation.
