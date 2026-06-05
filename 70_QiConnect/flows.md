# QiConnect Flows

## External Access Flow

```text
External request
  -> DNS, policy, or tunnel endpoint
  -> protected QiServer route
  -> target service
  -> internal data service if required
```

## Internal Tool Flow

```text
QiAccess
  -> service link
  -> private or public restricted route
  -> tool runtime
```

## Integration Review Flow

```text
New integration
  -> classify access
  -> identify data touched
  -> define route
  -> document owner and safety boundary
  -> verify from QiServer
```
