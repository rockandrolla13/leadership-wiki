import pytest
from pathlib import Path
from unittest.mock import patch
from lint import run_lint


AUDIT_JSON = """{
  "issues": [
    {
      "severity": "Warning",
      "type": "orphan_page",
      "page": "principles/trust.md",
      "description": "No inbound [[wikilinks]] from other pages"
    },
    {
      "severity": "Info",
      "type": "missing_link",
      "page": "principles/delegation.md",
      "description": "Mentions accountability but does not link [[accountability]]"
    }
  ],
  "patterns": ["User repeatedly faces delegation challenges across 3 cases"],
  "summary": "Wiki is healthy overall. One orphan page and one missing link found."
}"""


def _setup(tmp_path: Path) -> Path:
    wiki_root = tmp_path / "wiki"
    wiki_root.mkdir()
    (wiki_root / "index.md").write_text("# Index\n", encoding="utf-8")
    (wiki_root / "log.md").write_text("# Log\n", encoding="utf-8")
    (wiki_root / "principles").mkdir()
    (wiki_root / "principles" / "trust.md").write_text("# Trust\nContent.\n", encoding="utf-8")
    (wiki_root / "principles" / "delegation.md").write_text("# Delegation\nContent.\n", encoding="utf-8")
    return wiki_root


def test_run_lint_returns_report(tmp_path):
    wiki_root = _setup(tmp_path)
    with patch("lint.claude_call", return_value=AUDIT_JSON):
        report = run_lint(wiki_root=wiki_root, model="claude-opus-4-7", report_only=True)

    assert len(report["issues"]) == 2
    assert report["issues"][0]["severity"] == "Warning"
    assert "delegation" in report["patterns"][0]
    assert "healthy" in report["summary"]


def test_run_lint_makes_one_audit_call(tmp_path):
    wiki_root = _setup(tmp_path)
    with patch("lint.claude_call", return_value=AUDIT_JSON) as mock_claude:
        run_lint(wiki_root=wiki_root, model="claude-opus-4-7", report_only=True)

    assert mock_claude.call_count == 1


def test_run_lint_report_only_skips_fix_prompt(tmp_path):
    wiki_root = _setup(tmp_path)
    with patch("lint.claude_call", return_value=AUDIT_JSON):
        with patch("builtins.input") as mock_input:
            run_lint(wiki_root=wiki_root, model="claude-opus-4-7", report_only=True)
    mock_input.assert_not_called()
