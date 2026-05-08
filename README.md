# Frida AI Skills

Model-agnostic AI skills for planning, writing, packaging, and debugging Frida instrumentation across Android, iOS, native libraries, desktop processes, and Frida Gadget workflows.

Tags: `ai-skills`, `agent-skills`, `codex-skills`, `frida`, `reverse-engineering`, `dynamic-instrumentation`, `android`, `ios`, `native-hooks`, `mobile-security`, `appsec`, `ssl-pinning`, `frida-gadget`

## AI Agent Compatibility

These skills are written as plain `SKILL.md` instruction folders so any AI agent or skill runner can use them by reading the relevant skill directory. The `agents/openai.yaml` files are compatibility metadata for OpenAI/Codex-style skill lists; they do not make the skill content OpenAI-only.

## Install With npx

List available skills without installing:

```bash
npx skills add Rudra-ravi/frida-skills --list --full-depth
```

Install every skill from this repository for Codex:

```bash
npx skills add Rudra-ravi/frida-skills --skill '*' --agent codex --yes --full-depth
```

Install every skill globally for every supported agent:

```bash
npx skills add Rudra-ravi/frida-skills --all --global --yes --full-depth
```

Install to selected agents:

```bash
npx skills add Rudra-ravi/frida-skills --skill '*' --agent codex --agent claude-code --agent cursor --yes --full-depth
```

Install one focused skill:

```bash
npx skills add Rudra-ravi/frida-skills --skill frida-workflow --agent codex --yes --full-depth
```

Install from the full GitHub URL:

```bash
npx skills add https://github.com/Rudra-ravi/frida-skills --skill frida-tls-pinning --agent codex --yes --full-depth
```

Install from a direct skill folder URL:

```bash
npx skills add https://github.com/Rudra-ravi/frida-skills/tree/main/frida-codeshare-search --agent codex --yes --full-depth
```

Use `--copy` if your agent setup cannot use symlinks:

```bash
npx skills add Rudra-ravi/frida-skills --skill '*' --agent codex --copy --yes --full-depth
```

Restart your AI agent after installing so the new skills are discovered.

For non-Codex agents, clone this repository and register or copy the skill folders your agent supports. Each skill is self-contained in its own directory and uses the same required structure:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

## Codex/OpenAI-Compatible Skill Installer

You can also install with an OpenAI/Codex-compatible skill installer from the GitHub URL:

```text
$skill-installer install https://github.com/Rudra-ravi/frida-skills/tree/main/frida-workflow
```

Repeat with any skill folder below.

## Skills

| Skill | Use When |
| --- | --- |
| `frida-workflow` | Planning Frida tasks, selecting attach/spawn/Gadget mode, chaining focused skills, and preserving reproducible evidence. |
| `frida-setup-checklist` | Verifying host tools, Android/iOS devices, transports, Frida versions, architecture, and smoke scripts before hook work. |
| `frida-tools-reference` | Choosing and running Frida CLI tools such as `frida`, `frida-ps`, `frida-ls-devices`, `frida-trace`, `frida-discover`, `frida-kill`, and `frida-create`. |
| `frida-tracing-discovery` | Discovering classes, methods, modules, exports, imports, symbols, stack traces, and call paths before writing final hooks. |
| `frida-native-hooks` | Hooking native exports, imports, stripped functions, memory, `Interceptor`, `NativeFunction`, `NativeCallback`, Stalker, and CModule paths. |
| `frida-android-hooks` | Instrumenting Android Java/Kotlin/JNI behavior, overloads, constructors, class loaders, pinning, and native library transitions. |
| `frida-ios-hooks` | Instrumenting Objective-C, Swift/native, iOS trust paths, rootless jailbreak setups, and Gadget workflows. |
| `frida-agent-builder` | Creating maintainable TypeScript Frida agents with structured logging, RPC probes, and multi-hook organization. |
| `frida-gadget-injection` | Planning and debugging Frida Gadget workflows for Android, iOS, desktop apps, jailed devices, embedded configs, and load timing. |
| `frida-tls-pinning` | Identifying and hooking TLS/SSL pinning paths across Android, iOS, Flutter, React Native, native TLS stacks, and app-specific trust code. |
| `frida-anti-instrumentation` | Diagnosing and bypassing anti-Frida, anti-debugging, root/jailbreak, emulator, ptrace, port scan, module scan, and integrity checks. |
| `frida-data-extraction` | Observing runtime data such as HTTP requests, headers, tokens, JSON, crypto values, preferences, SQLite, files, and memory buffers. |
| `frida-codeshare-search` | Searching Frida CodeShare with curl, extracting scripts from project pages, and converting public snippets into reviewed local agents or `--codeshare` commands. |
| `frida-script-review` | Reviewing, hardening, and simplifying public, generated, broad, native-pointer-heavy, or mutation-heavy Frida scripts before running them. |
| `frida-troubleshooting` | Debugging attach/spawn failures, version mismatches, hooks that do not fire, runtime bridge issues, and target crashes. |

## Research Basis

The skills combine current official Frida documentation with practitioner patterns from Frida CodeShare, OWASP MASTG, and advanced Frida references. They emphasize observation before mutation, small reversible hooks, explicit version checks, and treating public bypass bundles as reconnaissance rather than final proof.

Primary sources are listed in `frida-workflow/references/frida-sources.md`.

## Validate

```bash
for d in frida-workflow frida-setup-checklist frida-tools-reference frida-tracing-discovery frida-native-hooks frida-android-hooks frida-ios-hooks frida-agent-builder frida-gadget-injection frida-tls-pinning frida-anti-instrumentation frida-data-extraction frida-codeshare-search frida-script-review frida-troubleshooting; do
  python3 /home/rudra/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d"
done

bash -n frida-workflow/scripts/frida-env-check.sh
python3 -m py_compile frida-agent-builder/scripts/scaffold-frida-agent.py
python3 -m py_compile frida-codeshare-search/scripts/codeshare_extract.py
npx skills add . --list --full-depth
```

## License

MIT. See `LICENSE`.
