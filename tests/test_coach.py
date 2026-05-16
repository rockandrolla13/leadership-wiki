import pytest
from pathlib import Path
from unittest.mock import patch
from coach import answer_question


ROUTING_JSON = """{
  "relevant_pages": ["principles/delegation.md", "management/underperformance.md"],
  "response_format": "coaching"
}"""

COACHING_ANSWER = """## Diagnosis

This is a delegation problem, not a motivation problem.

## What This Is Really About

The engineer lacks clear ownership. Ownership was delegated without being transferred.

## What To Do Next

1. Schedule a 30-minute one-on-one this week.
2. Name the gap directly: "I want to give you full ownership of this. Let's align on what that means."
3. Agree on a check-in cadence — weekly is enough.

## Suggested Language

"I want to step back from the day-to-day decisions on this component. I'd like you to own it fully — that means you make the calls and I trust you to flag anything you need from me. Can we walk through what that looks like?"

## What Not To Do

Do not keep shadowing their decisions. It signals distrust and perpetuates the problem.

## Follow-Up

Check in two weeks. If they are still waiting for approval on small decisions, revisit the handoff conversation.
"""


def _setup(tmp_path: Path) -> tuple[Path, Path]:
    wiki_root = tmp_path / "wiki"
    schemas_root = tmp_path / "schemas"
    wiki_root.mkdir()
    schemas_root.mkdir()

    (wiki_root / "index.md").write_text("# Index\n", encoding="utf-8")
    (wiki_root / "log.md").write_text("# Log\n", encoding="utf-8")
    (wiki_root / "principles").mkdir()
    (wiki_root / "principles" / "delegation.md").write_text("# Delegation\nContent.\n", encoding="utf-8")
    (wiki_root / "management").mkdir()
    (wiki_root / "management" / "underperformance.md").write_text("# Underperformance\nContent.\n", encoding="utf-8")

    (schemas_root / "LEADERSHIP_AGENT.md").write_text("# Agent\n", encoding="utf-8")
    (schemas_root / "coaching_protocol.md").write_text("# Coaching Protocol\n", encoding="utf-8")

    return wiki_root, schemas_root


def test_answer_question_returns_coaching_response(tmp_path):
    wiki_root, schemas_root = _setup(tmp_path)

    with patch("coach.SCHEMAS_ROOT", schemas_root):
        with patch("coach.claude_call", side_effect=[ROUTING_JSON, COACHING_ANSWER]):
            answer, pages, fmt = answer_question(
                "How do I delegate without losing quality control?",
                "claude-opus-4-7",
                wiki_root=wiki_root,
            )

    assert "delegation problem" in answer
    assert "delegation.md" in pages
    assert fmt == "coaching"


def test_answer_question_makes_two_claude_calls(tmp_path):
    wiki_root, schemas_root = _setup(tmp_path)

    with patch("coach.SCHEMAS_ROOT", schemas_root):
        with patch("coach.claude_call", side_effect=[ROUTING_JSON, COACHING_ANSWER]) as mock_claude:
            answer_question(
                "How do I delegate without losing quality control?",
                "claude-opus-4-7",
                wiki_root=wiki_root,
            )

    assert mock_claude.call_count == 2


def test_answer_question_loads_relevant_pages(tmp_path):
    wiki_root, schemas_root = _setup(tmp_path)

    with patch("coach.SCHEMAS_ROOT", schemas_root):
        with patch("coach.claude_call", side_effect=[ROUTING_JSON, COACHING_ANSWER]):
            answer, pages, _ = answer_question(
                "How do I delegate without losing quality control?",
                "claude-opus-4-7",
                wiki_root=wiki_root,
            )

    assert "principles/delegation.md" in pages
    assert "management/underperformance.md" in pages
