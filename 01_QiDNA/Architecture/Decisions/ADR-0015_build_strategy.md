# ADR-0015: Markdown to Single HTML Build

## Status

Accepted.

## Context

The repository has a small Node build that discovers Markdown and renders `site/index.html`. It also contains Mintlify navigation configuration and a Python chronicle generator. Multiple publication models can create conflicting navigation and authority.

## Decision

Canonical documentation remains Markdown in its owning folders. The supported reader build is one generated static HTML file at `site/index.html`, produced by `npm run build`.

HTML, chronicles, manifests, indexes, and external publications are derived outputs and do not become canonical by being generated or deployed.

## Rationale

The existing build is lightweight, searchable, portable, and introduces no additional documentation framework.

## Consequences

- Stale required paths are corrected when source documents move.
- Markdown and MDX coverage must be explicit; the current HTML builder discovers `.md` only.
- `docs.json` and wiki plans remain secondary until aligned with this decision.
