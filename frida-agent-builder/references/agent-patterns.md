# Agent Patterns

## Host Command

```bash
frida -U -f com.example.app -l dist/agent.js --no-pause
```

## RPC Probe

```ts
rpc.exports = {
  ping() {
    return {
      platform: Process.platform,
      arch: Process.arch,
      pointerSize: Process.pointerSize
    };
  }
};
```

## Logging

Use stable tags so host scripts can filter output:

```ts
export function log(tag: string, data: unknown): void {
  console.log(JSON.stringify({ tag, data }));
}
```

## Organization

- `src/index.ts`: environment checks, hook registration.
- `src/hooks/android.ts`: Java/Kotlin hooks.
- `src/hooks/native.ts`: module/export hooks.
- `src/hooks/ios.ts`: ObjC/Swift hooks.
- `src/log.ts`: structured logging helpers.

Only include files relevant to the target platform.
