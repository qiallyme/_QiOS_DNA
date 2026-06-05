# QiServer Flows

## Deployment Flow

```text
Inspect qiserver
  -> confirm repo, branch, remote, stack, ports, and working tree
  -> pull only from the confirmed repo
  -> back up runtime config before overwriting
  -> deploy or restart only the needed stack
  -> verify local, tailnet, and public routes
```

## Access Flow

```text
Public request
  -> Cloudflare Access or tunnel policy
  -> QiServer route
  -> target service
```

```text
Private request
  -> Tailscale
  -> QiServer route
  -> target service
```

## Runtime Fact Flow

```text
Runtime inspection
  -> verified service map
  -> active QiServer docs
  -> QiAccess links and QiSystem checks
```
