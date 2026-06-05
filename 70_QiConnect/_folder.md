# QiConnect

## Overview

QiConnect is the integration and access-boundary layer. It documents how Qi services connect to each other, to external providers, and to protected entrypoints.

## Responsibilities

- External integrations.
- API and webhook boundaries.
- Public restricted access paths.
- Private-only access paths.
- Tailscale and Cloudflare Access patterns.
- Service-to-service connection notes.
- Integration safety rules.

## Flows

```text
External request
  -> DNS, policy, or tunnel endpoint
  -> protected QiServer route
  -> target service
  -> internal data service if required
```

## Structure

Access classes are Private Only, Public Restricted, and Public Safe. Known connection surfaces include Cloudflare Access, Tailscale, localhost verification ports, Docker Compose networks, API endpoints, and webhooks.

