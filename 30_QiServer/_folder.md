# QiServer

## Overview

QiServer is the protected runtime host for internal services. It contains live Docker Compose stacks, system services, private access routes, public restricted routes, and runtime configuration paths.

Verified runtime facts win over repo planning notes.

## Responsibilities

- Host protected runtime services.
- Keep runtime stack paths and service facts clear.
- Separate public restricted access from private-only access.
- Run Docker Compose stacks and systemd services.
- Verify local, tailnet, and public routes after changes.

## Flows

```text
Inspect qiserver
  -> confirm repo, branch, remote, stack, ports, and working tree
  -> pull only from the confirmed repo
  -> back up runtime config before overwriting
  -> deploy or restart only the needed stack
  -> verify routes
```

## Structure

Known runtime paths include `/srv/qios/stacks/_qiaccess_start`, `/srv/qios/stacks/_qiaccess_start/docker-compose.yml`, and `/srv/qios/apps/_QiAccess_Start/qiaccess/config`.

