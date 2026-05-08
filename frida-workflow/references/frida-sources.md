# Frida Sources

Use these sources before making version-sensitive claims:

- Official docs home: https://frida.re/docs/home/
- Quick start: https://frida.re/docs/quickstart/
- JavaScript API: https://frida.re/docs/javascript-api/
- Best practices: https://frida.re/docs/best-practices/
- Modes of operation: https://frida.re/docs/modes/
- Frida CLI: https://frida.re/docs/frida-cli/
- frida-trace: https://frida.re/docs/frida-trace/
- frida-ps: https://frida.re/docs/frida-ps/
- frida-ls-devices: https://frida.re/docs/frida-ls-devices/
- frida-discover: https://frida.re/docs/frida-discover/
- frida-kill: https://frida.re/docs/frida-kill/
- Gadget: https://frida.re/docs/gadget/
- Messages: https://frida.re/docs/messages/
- Functions: https://frida.re/docs/functions/
- Bridges: https://frida.re/docs/bridges/
- Troubleshooting: https://frida.re/docs/troubleshooting/
- Stalker: https://frida.re/docs/stalker/
- Official releases: https://frida.re/news/releases/
- Frida source repository: https://github.com/frida/frida
- Frida tools repository: https://github.com/frida/frida-tools
- Frida website/docs repository: https://github.com/frida/frida-website
- PyPI package: https://pypi.org/project/frida/
- Frida CodeShare: https://codeshare.frida.re/
- OWASP MASTG Frida generic tool: https://mas.owasp.org/MASTG/tools/generic/MASTG-TOOL-0031/
- OWASP MASTG Frida CodeShare: https://mas.owasp.org/MASTG/tools/generic/MASTG-TOOL-0032/
- OWASP MASTG Android Frida: https://mas.owasp.org/MASTG/tools/android/MASTG-TOOL-0001/
- OWASP MASTG iOS Frida: https://mas.owasp.org/MASTG/tools/ios/MASTG-TOOL-0039/
- OWASP MASTG Android certificate pinning bypass: https://mas.owasp.org/MASTG/techniques/android/MASTG-TECH-0012/
- Frida Handbook advanced usage: https://learnfrida.info/advanced_usage/
- Frida Handbook Android instrumentation: https://learnfrida.info/java/
- Claude skills overview: https://claude.com/docs/skills/overview
- Claude custom skills guide: https://claude.com/docs/skills/how-to
- Agent Skills overview: https://learn.microsoft.com/en-us/agent-framework/agents/skills

Current research snapshot, 2026-05-08:

- Official Frida docs and repositories list the main CLI tools as `frida`, `frida-ps`, `frida-ls-devices`, `frida-trace`, `frida-discover`, and `frida-kill`.
- Official JavaScript API docs note that as of Frida 17 the Java runtime bridge is no longer baked into GumJS and may be fetched with `npm install frida-java-bridge`.
- Official best practices emphasize allocating replacement strings instead of overwriting fixed buffers, and keeping allocated strings alive.
- Official Gadget docs describe Listen, Connect, Script, and ScriptDirectory interactions, and note iOS code-signing constraints around `Interceptor`.
- Official `frida-trace` docs show native, ObjC, Java, JNI, include, exclude, and address tracing patterns; include/exclude order affects the working set.
- Frida CodeShare and OWASP MASTG show common practitioner use of ready-made scripts for discovery and concrete mobile testing tasks, especially unpinning, ObjC observers, JNI tracing, and dynamic DEX dumping.
- OWASP notes that `frida-multiple-unpinning` covers more Android pinning scenarios than Objection's built-in bypass, but this should still be used as reconnaissance before writing narrow target-specific hooks.
- Stalker guidance and the Frida Handbook both point toward bounded tracing. Prefer call summaries or scoped tracing over instruction-level `exec` tracing unless the volume and performance cost are justified.
- Claude and Agent Skills guidance emphasize progressive disclosure: concise descriptions for activation, focused `SKILL.md` files, and separate `references/`, `scripts/`, and `assets/` loaded only when needed.
