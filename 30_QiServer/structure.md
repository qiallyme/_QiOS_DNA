# QiServer Structure

Known runtime paths:

- QiAccess stack: `/srv/qios/stacks/_qiaccess_start`
- QiAccess compose: `/srv/qios/stacks/_qiaccess_start/docker-compose.yml`
- QiAccess runtime config: `/srv/qios/stacks/_qiaccess_start/config`
- QiAccess repo config source: `/srv/qios/apps/_QiAccess_Start/qiaccess/config`

Access classes:

- Private Only: local host or tailnet only.
- Public Restricted: internet reachable but protected by Cloudflare Access or equivalent.
- Public Safe: intended unauthenticated public surface.

Do not deploy from alternate checkouts unless inspection proves they are intended.
