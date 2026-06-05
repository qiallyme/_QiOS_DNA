# QiApp QiLife Structure

Core v1 tables:

- `qibits`
- `buckets`
- `threads`
- `actions`
- `action_steps`
- `people`
- `transactions`
- `obligations`
- `knowledge_items`
- `documents`
- `events`
- `links`
- `activity_log`
- `ai_outputs`
- `daily_summaries`

Canonical conventions:

- IDs use ULIDs except static lookup tables.
- `note` and `reflection` are QiBit types.
- Monetary amounts are stored as integer cents.
- Repo docs imported into `knowledge_items` are read-only in-app.
- Tags support search; links define exact relationships.
