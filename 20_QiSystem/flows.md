# QiSystem Flows

## Health Evidence Flow

```text
Runtime or service check
  -> health result
  -> audit or generated report
  -> maintenance action if needed
  -> retained QiSystem record
```

## Generated Index Flow

```text
Source tree or runtime state
  -> scanner or inventory
  -> generated index
  -> review
  -> update active docs only when facts change
```

## Maintenance Flow

```text
Issue discovered
  -> record evidence
  -> assign maintenance note
  -> fix in matching layer
  -> verify and close with result
```
