#!/usr/bin/env python3
"""Ingest a source file into the leadership wiki.

Reads the source, identifies which wiki pages to update or create (planning call),
updates/creates each page (per-page calls), writes a source summary, and updates
index.md and log.md.

Usage:
    python scripts/ingest.py raw/articles/hbr-article.md
    python scripts/ingest.py raw/articles/report.pdf          # auto-converts PDF first
    python scripts/ingest.py raw/articles/                    # ingest entire folder
    python scripts/ingest.py raw/articles/article.md --model claude-sonnet-4-6
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    WIKI_ROOT, SCHEMAS_ROOT,
    load_index, load_pages, write_page, append_log,
    claude_call, list_raw_sources, parse_json_response,
)
from convert import convert_pdf


def _read_source(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        tmp_md = path.with_suffix(".md")
        status, _ = convert_pdf(path, tmp_md)
        if status == "FAILED":
            raise RuntimeError(f"PDF conversion failed for {path}")
        content = tmp_md.read_text(encoding="utf-8")
        tmp_md.unlink()
        return content
    return path.read_text(encoding="utf-8")


def _infer_page_type(page_path: str) -> str:
    if any(d in page_path for d in ("principles/", "organization/", "coaching/")):
        return "concept"
    if "cases/" in page_path:
        return "case"
    return "playbook"


def ingest_source(source_path: Path, model: str, wiki_root: Path = WIKI_ROOT) -> None:
    print(f"\n--- Ingesting: {source_path.name} ---")

    source_content = _read_source(source_path)
    index_content = load_index(wiki_root)
    ingestion_protocol = (SCHEMAS_ROOT / "ingestion_protocol.md").read_text(encoding="utf-8")
    page_templates = (SCHEMAS_ROOT / "page_templates.md").read_text(encoding="utf-8")
    leadership_agent = (SCHEMAS_ROOT / "LEADERSHIP_AGENT.md").read_text(encoding="utf-8")

    # Planning pass
    print("\n[1/4] Planning: identifying pages to update or create...")
    planning_response = claude_call(
        system=f"{ingestion_protocol}\n\nReturn ONLY a JSON object, no surrounding text.",
        user=f"""Source file: {source_path.name}

## Source Content
{source_content[:12000]}

## Current Wiki Index
{index_content}

Return a JSON object with keys: pages_to_update, pages_to_create, source_slug, key_concepts.""",
        model=model,
    )
    plan = parse_json_response(planning_response)

    pages_to_update = plan.get("pages_to_update", [])
    pages_to_create = plan.get("pages_to_create", [])
    source_slug = plan.get("source_slug", source_path.stem.lower().replace(" ", "-"))
    key_concepts = plan.get("key_concepts", [])

    existing_pages = load_pages(wiki_root, pages_to_update)

    # Update existing pages
    print(f"\n[2/4] Updating {len(pages_to_update)} pages...")
    for page_path in pages_to_update:
        current = existing_pages.get(page_path, "")
        print(f"  → {page_path}")
        updated = claude_call(
            system=f"{leadership_agent}\n\nReturn ONLY the complete updated markdown page. No preamble.",
            user=f"""Update this wiki page with insights from the new source.

## Current Page
{current}

## New Source: {source_path.name}
{source_content[:8000]}

Return the complete updated page with correct YAML frontmatter. Update the `updated` date to today.""",
            model=model,
        )
        write_page(wiki_root / page_path, updated)

    # Create new pages
    print(f"\n[3/4] Creating {len(pages_to_create)} pages...")
    for page_path in pages_to_create:
        print(f"  + {page_path}")
        page_type = _infer_page_type(page_path)
        created = claude_call(
            system=f"{leadership_agent}\n\nReturn ONLY the complete new markdown page. No preamble.",
            user=f"""Create a new {page_type} wiki page at path: {page_path}

## Source: {source_path.name}
{source_content[:8000]}

## Available Templates
{page_templates}

Return the complete page with correct YAML frontmatter.""",
            model=model,
        )
        write_page(wiki_root / page_path, created)

    # Source summary
    print(f"\n[4/4] Writing source summary ({source_slug})...")
    summary_content = claude_call(
        system=f"{leadership_agent}\n\nReturn ONLY the complete source summary page. No preamble.",
        user=f"""Write a source summary page for this source.

Source path: {source_path}
Slug: {source_slug}

## Source Content
{source_content[:10000]}

## Pages Updated
{chr(10).join(f"- [[{p}]]" for p in pages_to_update) or "- None"}

## Pages Created
{chr(10).join(f"- [[{p}]]" for p in pages_to_create) or "- None"}

Use the source summary template. Fill in all sections.""",
        model=model,
    )
    write_page(wiki_root / "sources" / f"{source_slug}.md", summary_content)

    # Update index
    _update_index(wiki_root, pages_to_update, pages_to_create, source_slug, model)

    # Log
    today = date.today().isoformat()
    append_log(
        wiki_root,
        f"""## [{today}] ingest | {source_path.name}

- Source: {source_path}
- Pages created:
{chr(10).join(f"  - [[{p}]]" for p in pages_to_create) or "  - None"}
- Pages updated:
{chr(10).join(f"  - [[{p}]]" for p in pages_to_update) or "  - None"}
- Key concepts: {", ".join(key_concepts)}
- Contradictions / tensions: See source summary
- Follow-up questions: See source summary""",
    )

    print(f"\n✓ Done: {len(pages_to_create)} created, {len(pages_to_update)} updated")


def _update_index(
    wiki_root: Path,
    updated: list[str],
    created: list[str],
    source_slug: str,
    model: str,
) -> None:
    current_index = load_index(wiki_root)
    all_changed = updated + created + [f"sources/{source_slug}.md"]

    new_index = claude_call(
        system="You maintain a leadership wiki index. Return ONLY the updated index.md content.",
        user=f"""Update index.md to reflect these changes. Maintain table structure.
Update the 'Last updated' date header. Add new rows, update existing rows.

## Current index.md
{current_index}

## Pages changed
{chr(10).join(f"- {p}" for p in all_changed)}""",
        model=model,
    )
    write_page(wiki_root / "index.md", new_index)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Source file or directory (.md, .txt, .pdf)")
    parser.add_argument("--model", default="claude-opus-4-7")
    args = parser.parse_args(argv)

    sources = list_raw_sources(args.source)
    if not sources:
        print(f"No source files found at {args.source}", file=sys.stderr)
        return 1

    for path in sources:
        ingest_source(path, args.model)
    return 0


if __name__ == "__main__":
    sys.exit(main())
