# Discovery Patterns

## Official Anchors

- Frida CLI: https://frida.re/docs/frida-cli/
- Frida JavaScript API: https://frida.re/docs/javascript-api/
- Frida examples: https://frida.re/docs/examples/
- Frida functions tutorial: https://frida.re/docs/functions/

## Trace Ladders

Network:
URL builders, request constructors, headers, body writers, TLS validation, socket connect, native SSL read/write.

Crypto:
Base64, JSON parse/stringify, Java crypto APIs, CommonCrypto, BoringSSL/OpenSSL, app wrapper methods, native byte buffers.

Filesystem:
SharedPreferences/UserDefaults, SQLite, open/read/write, app cache directories, document providers.

Dynamic code:
ClassLoader, DexClassLoader, Runtime.loadLibrary, dlopen, module load callbacks.

## Stop Conditions

- You can name the app-owned caller.
- The hook fires only on the target action.
- Arguments and return values prove the behavior.
- The next hook can be narrower than the current hook.
