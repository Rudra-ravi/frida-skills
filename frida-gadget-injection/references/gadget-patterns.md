# Gadget Patterns

## Official Anchors

- Frida Gadget docs: https://frida.re/docs/gadget/
- Frida modes of operation: https://frida.re/docs/modes/
- Frida JavaScript API code-signing policy notes: https://frida.re/docs/javascript-api/

## Common Failure Checks

- Wrong architecture: app loads `arm64-v8a` but Gadget is `armeabi-v7a`, or iOS slice is missing.
- Wrong filename: config must match the Gadget binary name with `.config`.
- Late load: target behavior happens before Gadget is loaded.
- Code signing: iOS app or library was changed but not re-signed correctly.
- Network mode mismatch: `listen` waits for host; `connect` needs reachable host and port.

## Safer Embedded Script Pattern

Use embedded script mode for deterministic startup logging first:

```json
{
  "interaction": {
    "type": "script",
    "path": "agent.js"
  }
}
```

Use only observation hooks until the Gadget load path and target behavior are proven.
