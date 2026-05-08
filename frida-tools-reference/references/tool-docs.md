# Frida Tool Docs

## Official Links

- Frida CLI: https://frida.re/docs/frida-cli/
- frida-trace: https://frida.re/docs/frida-trace/
- frida-ps: https://frida.re/docs/frida-ps/
- frida-ls-devices: https://frida.re/docs/frida-ls-devices/
- frida-discover: https://frida.re/docs/frida-discover/
- frida-kill: https://frida.re/docs/frida-kill/
- Frida tools repository: https://github.com/frida/frida-tools

## Notes

- `frida-trace` can trace native functions, Objective-C methods, Java methods, and module patterns.
- `frida-trace` include and exclude order affects the final working set.
- Use `frida-ps -Uai` before mobile spawn/attach to confirm visible identifiers.
- Use `frida-kill` only when the user explicitly wants to terminate a target process.
