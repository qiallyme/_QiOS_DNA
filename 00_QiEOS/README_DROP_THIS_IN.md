# QiDNA Database Standards Pack - Drop-In Instructions

Generated: 2026-06-13
Target root: `C:\QiLabs`

## What this is

This pack is a drop-in set of QiDNA database governance documents.

It is designed to land here:

```text
C:\QiLabs\_QiOS_DNA\00_QiEOS\30_standards\40_database\
```

## What to do

Unzip this package into:

```text
C:\QiLabs\
```

It already includes the `_QiOS_DNA/...` folder path.

## Files included

```text
_QiOS_DNA/00_QiEOS/30_standards/40_database/
  00_INDEX.md
  00_master_schema_governance.md
  10_master_table_catalog.md
  20_field_registry_standard.md
  30_source_of_truth_rules.md
  40_sensitivity_classification.md
  50_ingestion_staging_standard.md
  60_database_naming_conventions.md
  70_schema_decision_matrix.md
  80_codex_implementation_prompt.md
  _support/
    qidna_database_pack_manifest.json
    overlap_review_notes.md
```

## Important note

This is a governance and blueprint pack, not final SQL. That is intentional.

Build order is:

```text
Doctrine -> table catalog -> migration plan -> SQL -> API contracts -> UI wiring
```

Do not let Codex skip straight from messy CSVs to production tables. That is how you get a pristine disaster.
