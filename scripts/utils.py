#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

import anthropic
from dotenv import load_dotenv

load_dotenv()

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
SCHEMAS_ROOT = Path(__file__).parent.parent / "schemas"


def load_index(wiki_root: Path) -> str:
    index_path = wiki_root / "index.md"
    if not index_path.exists():
        return "# Leadership Wiki Index\n\n_No pages yet._\n"
    return index_path.read_text(encoding="utf-8")


def load_pages(wiki_root: Path, paths: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for p in paths:
        full = wiki_root / p
        if full.exists():
            result[p] = full.read_text(encoding="utf-8")
    return result


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def append_log(wiki_root: Path, entry: str) -> None:
    log_path = wiki_root / "log.md"
    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n" + entry.strip() + "\n")


def claude_call(system: str, user: str, model: str = "claude-opus-4-7") -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    chunks: list[str] = []
    with client.messages.stream(
        model=model,
        max_tokens=8192,
        system=system,
        messages=[{"role": "user", "content": user}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            chunks.append(text)
    print()
    return "".join(chunks)


def list_raw_sources(path: str | Path) -> list[Path]:
    p = Path(path)
    if p.is_file():
        return [p]
    return sorted(
        f for f in p.rglob("*")
        if f.suffix.lower() in {".md", ".txt", ".pdf"}
        and not f.name.startswith("_")
    )


def parse_json_response(text: str) -> Any:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    raise ValueError(f"No JSON found in response: {text[:200]}")
