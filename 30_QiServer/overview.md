# QiServer Overview

QiServer is the protected runtime host for internal services. It contains the live Docker Compose stacks, system services, private access routes, public restricted routes, and runtime configuration paths.

Verified runtime facts win over repo planning notes.

Confirmed host identity:

- Host: `qiserver`
- Working account: `qiadmin`
- Operator home: `/home/qiadmin`
- Public restricted entrypoint: `https://access.qially.com`
- Tailnet entrypoint: `https://qiserver-1.cerberus-sirius.ts.net`

QiServer supports QiAccess, QiLife, QiSystem, QiNexus, QiCapture, and QiConnect by hosting the services those layers use.
