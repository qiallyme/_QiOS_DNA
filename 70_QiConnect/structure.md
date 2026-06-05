# QiConnect Structure

Access classes:

- Private Only: local host or tailnet only.
- Public Restricted: internet reachable but protected by Cloudflare Access or equivalent.
- Public Safe: intended unauthenticated public surface.

Known connection surfaces:

- Cloudflare Access for public restricted QiAccess.
- Tailscale for private qiserver access.
- Localhost ports for service verification.
- Docker Compose networks for internal service communication.
- API endpoints and webhooks for integrations.

Do not copy secrets, tunnel tokens, or private credentials into documentation.
