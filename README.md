# Frida Skills

Codex skills for planning, writing, packaging, and debugging Frida instrumentation across Android, iOS, native libraries, desktop processes, and Frida Gadget workflows.

Tags: `codex-skills`, `agent-skills`, `frida`, `reverse-engineering`, `dynamic-instrumentation`, `android`, `ios`, `native-hooks`, `mobile-security`, `appsec`, `ssl-pinning`, `frida-gadget`

## Install With npx

Install every skill from this repository:

```bash
npx skills add Rudra-ravi/frida-skills --skill '*' --agent codex --yes --full-depth
```

Install one focused skill:

```bash
npx skills add Rudra-ravi/frida-skills --skill frida-workflow --agent codex --yes --full-depth
```

List available skills without installing:

```bash
npx skills add Rudra-ravi/frida-skills --list --full-depth
```

Restart Codex after installing so the new skills are discovered.

## Codex Skill Installer

You can also install with Codex's skill installer from the GitHub URL:

```text
$skill-installer install https://github.com/Rudra-ravi/frida-skills/tree/main/frida-workflow
```

Repeat with any skill folder below.

## Skills

| Skill | Use When |
| --- | --- |
| `frida-workflow` | Planning Frida tasks, selecting attach/spawn/Gadget mode, chaining focused skills, and preserving reproducible evidence. |
| `frida-native-hooks` | Hooking native exports, imports, stripped functions, memory, `Interceptor`, `NativeFunction`, `NativeCallback`, Stalker, and CModule paths. |
| `frida-android-hooks` | Instrumenting Android Java/Kotlin/JNI behavior, overloads, constructors, class loaders, pinning, and native library transitions. |
| `frida-ios-hooks` | Instrumenting Objective-C, Swift/native, iOS trust paths, rootless jailbreak setups, and Gadget workflows. |
| `frida-agent-builder` | Creating maintainable TypeScript Frida agents with structured logging, RPC probes, and multi-hook organization. |
| `frida-troubleshooting` | Debugging attach/spawn failures, version mismatches, hooks that do not fire, runtime bridge issues, and target crashes. |

## Research Basis

The skills combine current official Frida documentation with practitioner patterns from Frida CodeShare, OWASP MASTG, and advanced Frida references. They emphasize observation before mutation, small reversible hooks, explicit version checks, and treating public bypass bundles as reconnaissance rather than final proof.

Primary sources are listed in `frida-workflow/references/frida-sources.md`.

## Validate

```bash
for d in frida-workflow frida-native-hooks frida-android-hooks frida-ios-hooks frida-agent-builder frida-troubleshooting; do
  python3 /home/rudra/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done

bash -n frida-workflow/scripts/frida-env-check.sh
python3 -m py_compile frida-agent-builder/scripts/scaffold-frida-agent.py
npx skills add . --list --full-depth
```

## License

MIT. See `LICENSE`.
