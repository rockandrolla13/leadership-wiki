#!/usr/bin/env python3
"""Health-check the leadership wiki.

Loads all wiki pages, runs a full audit (one Claude call), prints severity-ranked
report, and optionally applies auto-fixable issues.

Usage:
    python scripts/lint.py
    python scripts/lint.py --report-only
    python scripts/lint.py --model claude-sonnet-4-6
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    WIKI_ROOT,
    load_index, write_page,
    claude_call, parse_json_response,
)

AUTO_FIXABLE = {"missing_link", "orphan_page", "generic_playbook"}


def run_lint(
    wiki_root: Path = WIKI_ROOT,
    model: str = "claude-opus-4-7",
    report_only: bool = False,
) -> dict:
    print("\n[1/2] Loading wiki pages...")
    all_pages: dict[str, str] = {}
    for md_file in wiki_root.rglob("*.md"):
        rel_path = str(md_file.relative_to(wiki_root))
        if not any(part.startswith("_") for part in md_file.parts):
            all_pages[rel_path] = md_file.read_text(encoding="utf-8")

    index_content = load_index(wiki_root)
    print(f"  Loaded {len(all_pages)} pages.")

    pages_preview = "\n\n".join(
        f"### {path}\n{content[:400]}{'...' if len(content) > 400 else ''}"
        for path, content in list(all_pages.items())[:40]
    )

    print("\n[2/2] Auditing wiki health...")
    audit_response = claude_call(
        system="You are a wiki health auditor. Return ONLY a JSON object, no surrounding text.",
        user=f"""Audit this leadership wiki for structural and content issues.

## Wiki Index
{index_content}

## Page Previews (first 400 chars each)
{pages_preview}

Return JSON with keys:
- issues: list of {{severity (Critical|Warning|Info), type, page, description}}
- patterns: list of recurring leadership patterns observed across cases
- summary: one paragraph health summary

Issue types: orphan_page, missing_link, stale_page, contradictory_guidance,
missing_page, generic_playbook, unsupported_claim""",
        model=model,
    )

    report = parse_json_response(audit_response)
    _print_report(report)

    if not report_only and report.get("issues"):
        choice = input("\nApply suggested fixes? [y/N] ").strip().lower()
        if choice == "y":
            _apply_fixes(report, all_pages, wiki_root, model)

    return report


def _print_report(report: dict) -> None:
    issues = report.get("issues", [])
    print("\n" + "=" * 60)
    print("WIKI HEALTH REPORT")
    print("=" * 60)

    for severity in ("Critical", "Warning", "Info"):
        group = [i for i in issues if i.get("severity") == severity]
        if group:
            print(f"\n{severity.upper()} ({len(group)})")
            for issue in group:
                print(f"  [{issue.get('type', '?')}] {issue.get('page', '')} — {issue.get('description', '')}")

    patterns = report.get("patterns", [])
    if patterns:
        print(f"\nRECURRING PATTERNS ({len(patterns)})")
        for p in patterns:
            print(f"  • {p}")

    print(f"\n{report.get('summary', 'No summary provided.')}")
    print("=" * 60)


def _apply_fixes(report: dict, all_pages: dict[str, str], wiki_root: Path, model: str) -> None:
    fixable = [i for i in report.get("issues", []) if i.get("type") in AUTO_FIXABLE]
    if not fixable:
        print("No auto-fixable issues found.")
        return

    print(f"\nApplying {len(fixable)} fix(es)...")
    for issue in fixable:
        page_path = issue.get("page", "")
        if not page_path or page_path not in all_pages:
            continue
        print(f"  Fixing {page_path} ({issue.get('type')})...")
        current = all_pages[page_path]
        fixed = claude_call(
            system="You fix leadership wiki pages. Return ONLY the corrected complete page. No preamble.",
            user=f"""Fix this wiki page.

## Issue
Type: {issue.get("type")}
Description: {issue.get("description")}

## Current Page
{current}

Return the complete corrected page with valid YAML frontmatter.""",
            model=model,
        )
        write_page(wiki_root / page_path, fixed)
        print(f"    ✓ Fixed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-only", action="store_true", help="Print report without fix prompt")
    parser.add_argument("--model", default="claude-opus-4-7")
    args = parser.parse_args(argv)

    run_lint(report_only=args.report_only, model=args.model)
    return 0


if __name__ == "__main__":
    sys.exit(main())
