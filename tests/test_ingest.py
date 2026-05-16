import pytest
from pathlib import Path
from unittest.mock import patch
from ingest import ingest_source, _infer_page_type


PLANNING_JSON = """{
  "pages_to_update": ["principles/trust.md"],
  "pages_to_create": ["principles/psychological-safety.md"],
  "source_slug": "hbr-psych-safety-2019",
  "key_concepts": ["psychological safety", "trust"]
}"""

UPDATED_TRUST = "---\ntype: concept\ntitle: Trust\nupdated: 2026-05-16\n---\n# Trust\n\nUpdated.\n"
NEW_PSYCH_SAFETY = "---\ntype: concept\ntitle: Psychological Safety\ncreated: 2026-05-16\n---\n# Psychological Safety\n\nNew.\n"
SOURCE_SUMMARY = "---\ntype: source\ntitle: HBR Psych Safety\ningested: 2026-05-16\n---\n# Source: HBR\n"
UPDATED_INDEX = "# Leadership Wiki Index\n\n_Last updated: 2026-05-16_\n"


def _setup_wiki(tmp_path: Path) -> tuple[Path, Path]:
    wiki_root = tmp_path / "wiki"
    schemas_root = tmp_path / "schemas"
    wiki_root.mkdir()
    schemas_root.mkdir()

    (wiki_root / "index.md").write_text("# Index\n", encoding="utf-8")
    (wiki_root / "log.md").write_text("# Log\n", encoding="utf-8")
    (wiki_root / "sources").mkdir()
    (wiki_root / "principles").mkdir()
    (wiki_root / "principles" / "trust.md").write_text(
        "---\ntype: concept\ntitle: Trust\n---\n# Trust\n", encoding="utf-8"
    )

    (schemas_root / "ingestion_protocol.md").write_text("# Ingestion Protocol\n", encoding="utf-8")
    (schemas_root / "page_templates.md").write_text("# Templates\n", encoding="utf-8")
    (schemas_root / "LEADERSHIP_AGENT.md").write_text("# Agent\n", encoding="utf-8")

    return wiki_root, schemas_root


def test_ingest_source_creates_and_updates_pages(tmp_path):
    wiki_root, schemas_root = _setup_wiki(tmp_path)

    source = tmp_path / "raw" / "hbr-psych-safety.md"
    source.parent.mkdir(parents=True)
    source.write_text("# HBR Article\nContent about psychological safety.\n", encoding="utf-8")

    responses = [
        PLANNING_JSON,
        UPDATED_TRUST,
        NEW_PSYCH_SAFETY,
        SOURCE_SUMMARY,
        UPDATED_INDEX,
    ]

    with patch("ingest.SCHEMAS_ROOT", schemas_root):
        with patch("ingest.claude_call", side_effect=responses):
            ingest_source(source, "claude-opus-4-7", wiki_root=wiki_root)

    assert (wiki_root / "principles" / "trust.md").read_text(encoding="utf-8") == UPDATED_TRUST
    assert (wiki_root / "principles" / "psychological-safety.md").exists()
    assert (wiki_root / "sources" / "hbr-psych-safety-2019.md").exists()

    log = (wiki_root / "log.md").read_text(encoding="utf-8")
    assert "ingest | hbr-psych-safety.md" in log
    assert "psychological safety" in log


def test_ingest_source_calls_claude_correct_number_of_times(tmp_path):
    wiki_root, schemas_root = _setup_wiki(tmp_path)

    source = tmp_path / "source.md"
    source.write_text("# Source\nContent.\n", encoding="utf-8")

    responses = [PLANNING_JSON, UPDATED_TRUST, NEW_PSYCH_SAFETY, SOURCE_SUMMARY, UPDATED_INDEX]

    with patch("ingest.SCHEMAS_ROOT", schemas_root):
        with patch("ingest.claude_call", side_effect=responses) as mock_claude:
            ingest_source(source, "claude-opus-4-7", wiki_root=wiki_root)

    # planning + 1 update + 1 create + source summary + index update = 5 calls
    assert mock_claude.call_count == 5


def test_infer_page_type():
    assert _infer_page_type("principles/delegation.md") == "concept"
    assert _infer_page_type("management/one-on-ones.md") == "playbook"
    assert _infer_page_type("cases/2026-05-16-case.md") == "case"
    assert _infer_page_type("coaching/profile.md") == "concept"
    assert _infer_page_type("organization/culture.md") == "concept"
