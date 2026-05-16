#!/usr/bin/env python3
"""Ask the leadership coach a question.

Two-pass: routing call (which wiki pages?) then coaching call (answer using those pages).
Optionally saves the answer as a case page.

Usage:
    python scripts/coach.py "My engineer keeps undermining the project in meetings"
    python scripts/coach.py "How do I delegate without losing quality control?"
    python scripts/coach.py "..." --no-save --model claude-sonnet-4-6
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    WIKI_ROOT, SCHEMAS_ROOT,
    load_index, load_pages, write_page, append_log,
    claude_call, parse_json_response,
)


def answer_question(
    question: str,
    model: str,
    wiki_root: Path = WIKI_ROOT,
) -> tuple[str, list[str], str]:
    index_content = load_index(wiki_root)
    coaching_protocol = (SCHEMAS_ROOT / "coaching_protocol.md").read_text(encoding="utf-8")
    leadership_agent = (SCHEMAS_ROOT / "LEADERSHIP_AGENT.md").read_text(encoding="utf-8")

    # Routing pass
    print("\n[1/2] Routing: identifying relevant wiki pages...")
    routing_response = claude_call(
        system="You are a routing assistant. Return ONLY a JSON object, no surrounding text.",
        user=f"""Given this leadership question and wiki index, identify the 8–12 most relevant pages.

## Question
{question}

## Wiki Index
{index_content}

Return JSON with keys: relevant_pages (list of page paths), response_format (one of: coaching, situation-map, conversation-script, development-note).""",
        model=model,
    )
    routing = parse_json_response(routing_response)
    relevant_pages = routing.get("relevant_pages", [])
    response_format = routing.get("response_format", "coaching")

    pages = load_pages(wiki_root, relevant_pages)
    pages_context = "\n\n---\n\n".join(
        f"## {path}\n{content}" for path, content in pages.items()
    )

    # Coaching pass
    print(f"\n[2/2] Generating {response_format} response...")
    answer = claude_call(
        system=f"{leadership_agent}\n\n{coaching_protocol}",
        user=f"""## Leadership Question
{question}

## Relevant Wiki Pages
{pages_context}

Provide a {response_format} response. Be specific, direct, and practical.
Do not use generic advice. Include suggested language the user can actually say.""",
        model=model,
    )

    return answer, relevant_pages, response_format


def _save_as_case(question: str, answer: str, relevant_pages: list[str], model: str) -> None:
    leadership_agent = (SCHEMAS_ROOT / "LEADERSHIP_AGENT.md").read_text(encoding="utf-8")
    today = date.today().isoformat()

    case_content = claude_call(
        system=f"{leadership_agent}\n\nReturn ONLY the complete case page markdown. No preamble.",
        user=f"""Create a case page from this coaching session.

## Question
{question}

## Coaching Answer
{answer}

## Relevant Wiki Pages
{chr(10).join(relevant_pages)}

Today: {today}. Use the case page template with correct YAML frontmatter. Set status: open.
Use roles for people (the engineer, the senior PM) — no real names.""",
        model=model,
    )

    slug = re.sub(r"[^a-z0-9]+", "-", question.lower())[:50].strip("-")
    case_path = WIKI_ROOT / "cases" / f"{today}-{slug}.md"
    write_page(case_path, case_content)
    print(f"Case saved: {case_path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", help="Leadership question to ask")
    parser.add_argument("--model", default="claude-opus-4-7")
    parser.add_argument("--no-save", action="store_true", help="Skip case save prompt")
    args = parser.parse_args(argv)

    answer, pages_list, response_format = answer_question(args.question, args.model)

    print("\n" + "=" * 60)
    print(answer)
    print("=" * 60)

    today = date.today().isoformat()
    append_log(
        WIKI_ROOT,
        f"""## [{today}] query | {args.question[:60]}

- User question: "{args.question}"
- Pages consulted:
{chr(10).join(f"  - [[{p}]]" for p in pages_list)}
- Answer type: {response_format}
- Filed back into wiki: No
- Follow-up action:""",
    )

    if not args.no_save:
        save = input("\nSave this as a case? [y/N] ").strip().lower()
        if save == "y":
            _save_as_case(args.question, answer, pages_list, args.model)

    return 0


if __name__ == "__main__":
    sys.exit(main())
