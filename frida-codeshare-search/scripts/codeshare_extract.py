#!/usr/bin/env python3
"""Extract Frida CodeShare search results or project source from saved HTML."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


class SearchParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.results: list[dict[str, str]] = []
        self._current: dict[str, str] | None = None
        self._capture: str | None = None
        self._text: list[str] = []
        self._article_depth = 0
        self._last_href = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag == "article":
            self._current = {}
            self._article_depth = 1
        elif self._current is not None:
            self._article_depth += 1

        if self._current is None:
            return

        if tag == "a":
            self._last_href = attrs_map.get("href") or ""
        if tag in {"h2", "h3", "h4", "p"}:
            self._capture = tag
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._current is None:
            return

        if tag == self._capture:
            text = " ".join(" ".join(self._text).split())
            if tag == "h2":
                self._current["title"] = text
                self._current["url"] = self._last_href
                match = re.search(r"/@([^/]+)/", self._last_href)
                if match:
                    self._current["author"] = f"@{match.group(1)}"
            elif tag == "h3":
                numbers = re.findall(r"[\d.]+K?|\d+", text)
                if numbers:
                    self._current["likes"] = numbers[0]
                if len(numbers) > 1:
                    self._current["views"] = numbers[1]
            elif tag == "p" and "description" not in self._current:
                self._current["description"] = text
            self._capture = None
            self._text = []

        if tag == "article":
            if self._current.get("title") and self._current.get("url"):
                self.results.append(self._current)
            self._current = None
            self._article_depth = 0
        elif self._current is not None:
            self._article_depth = max(0, self._article_depth - 1)


def read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def parse_project_source(source: str) -> dict[str, str]:
    fields = {}
    for key in ("projectName", "projectSlug", "projectDesc", "projectUUID"):
        match = re.search(rf'{key}:\s*"((?:\\.|[^"\\])*)"', source)
        if match:
            fields[key] = json.loads(f'"{match.group(1)}"')

    match = re.search(r'projectSource:\s*"((?:\\.|[^"\\])*)"', source)
    if not match:
        raise SystemExit("Could not find projectSource in CodeShare page")
    fields["projectSource"] = json.loads(f'"{match.group(1)}"')

    fingerprint = re.search(r"Fingerprint:\s*([0-9a-fA-F]{64})", source)
    if fingerprint:
        fields["fingerprint"] = fingerprint.group(1)

    return fields


def command_search(args: argparse.Namespace) -> None:
    parser = SearchParser()
    parser.feed(read_input(args.html))
    results: list[dict[str, Any]] = []
    for item in parser.results:
        url = item.get("url", "")
        if url.startswith("/"):
            item["url"] = f"https://codeshare.frida.re{url}"
        item["title"] = html.unescape(item.get("title", ""))
        item["description"] = html.unescape(item.get("description", ""))
        results.append(item)

    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
        return

    for index, item in enumerate(results, 1):
        print(f"{index}. {item.get('title', '')}")
        print(f"   author: {item.get('author', '')}  likes: {item.get('likes', '?')}  views: {item.get('views', '?')}")
        print(f"   url: {item.get('url', '')}")
        if item.get("description"):
            print(f"   desc: {item['description']}")


def command_project(args: argparse.Namespace) -> None:
    fields = parse_project_source(read_input(args.html))
    script = fields["projectSource"]
    if args.output:
        Path(args.output).write_text(script, encoding="utf-8", newline="\n")
        print(f"Wrote {args.output}")
    else:
        print(script)

    if not args.metadata:
        return

    metadata = {key: value for key, value in fields.items() if key != "projectSource"}
    print(json.dumps(metadata, indent=2, sort_keys=True), file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="parse a saved CodeShare search page")
    search.add_argument("html", help="HTML file path, or '-' for stdin")
    search.add_argument("--json", action="store_true", help="emit JSON")
    search.set_defaults(func=command_search)

    project = subparsers.add_parser("project", help="extract script from a saved CodeShare project page")
    project.add_argument("html", help="HTML file path, or '-' for stdin")
    project.add_argument("-o", "--output", help="write extracted script to this file")
    project.add_argument("--metadata", action="store_true", help="print project metadata to stderr")
    project.set_defaults(func=command_project)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
