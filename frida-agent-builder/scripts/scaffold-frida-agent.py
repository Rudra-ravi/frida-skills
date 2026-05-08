#!/usr/bin/env python3
"""Create a small TypeScript Frida agent skeleton."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--java", action="store_true", help="Include frida-java-bridge dependency note/package.")
    args = parser.parse_args()

    root = args.output
    root.mkdir(parents=True, exist_ok=True)

    deps = {"@types/frida-gum": "latest", "frida-compile": "latest", "typescript": "latest"}
    if args.java:
        deps["frida-java-bridge"] = "latest"

    package = {
        "private": True,
        "type": "module",
        "scripts": {
            "build": "frida-compile src/index.ts -o dist/agent.js",
            "check": "tsc --noEmit",
        },
        "devDependencies": deps,
    }

    write(root / "package.json", json.dumps(package, indent=2) + "\n")
    write(
        root / "tsconfig.json",
        """{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "types": ["frida-gum"]
  },
  "include": ["src/**/*.ts"]
}
""",
    )
    write(
        root / "src" / "log.ts",
        """export function log(tag: string, data: unknown = null): void {
  console.log(JSON.stringify({ tag, data }));
}
""",
    )
    write(
        root / "src" / "index.ts",
        """import { log } from "./log";

log("agent.loaded", {
  platform: Process.platform,
  arch: Process.arch,
  pointerSize: Process.pointerSize,
});

rpc.exports = {
  ping() {
    return "pong";
  },
};
""",
    )
    write(root / "dist" / ".gitkeep", "")
    print(f"Created Frida agent skeleton at {root}")


if __name__ == "__main__":
    main()
