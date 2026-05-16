import pytest
from pathlib import Path
from utils import (
    load_index, load_pages, write_page, append_log,
    list_raw_sources, parse_json_response,
)


def test_load_index_missing_returns_placeholder(tmp_path):
    result = load_index(tmp_path)
    assert "No pages yet" in result


def test_load_index_existing(tmp_path):
    (tmp_path / "index.md").write_text("# Index\n\n| Page | Summary |\n", encoding="utf-8")
    result = load_index(tmp_path)
    assert "Index" in result


def test_load_pages_existing(tmp_path):
    (tmp_path / "principles").mkdir()
    (tmp_path / "principles" / "delegation.md").write_text("# Delegation\n", encoding="utf-8")
    result = load_pages(tmp_path, ["principles/delegation.md"])
    assert "principles/delegation.md" in result
    assert "Delegation" in result["principles/delegation.md"]


def test_load_pages_skips_missing(tmp_path):
    result = load_pages(tmp_path, ["nonexistent.md"])
    assert result == {}


def test_write_page_creates_parent_dirs(tmp_path):
    path = tmp_path / "principles" / "trust.md"
    write_page(path, "# Trust\n")
    assert path.exists()
    assert path.read_text() == "# Trust\n"


def test_write_page_overwrites(tmp_path):
    path = tmp_path / "page.md"
    write_page(path, "old")
    write_page(path, "new")
    assert path.read_text() == "new"


def test_append_log_appends_entry(tmp_path):
    (tmp_path / "log.md").write_text("# Log\n", encoding="utf-8")
    append_log(tmp_path, "## [2026-05-16] ingest | test source")
    content = (tmp_path / "log.md").read_text()
    assert "ingest | test source" in content


def test_append_log_creates_log_if_missing(tmp_path):
    append_log(tmp_path, "## entry")
    assert (tmp_path / "log.md").exists()


def test_list_raw_sources_single_file(tmp_path):
    f = tmp_path / "article.md"
    f.write_text("# Article\n")
    result = list_raw_sources(f)
    assert result == [f]


def test_list_raw_sources_directory(tmp_path):
    (tmp_path / "a.md").write_text("A")
    (tmp_path / "b.txt").write_text("B")
    (tmp_path / "c.pdf").write_text("C")
    (tmp_path / "_ignore.md").write_text("X")
    result = list_raw_sources(tmp_path)
    names = {f.name for f in result}
    assert names == {"a.md", "b.txt", "c.pdf"}
    assert not any(f.name.startswith("_") for f in result)


def test_parse_json_response_direct():
    result = parse_json_response('{"key": "value"}')
    assert result == {"key": "value"}


def test_parse_json_response_markdown_fence():
    text = 'Here is the JSON:\n```json\n{"key": "value"}\n```\n'
    result = parse_json_response(text)
    assert result == {"key": "value"}


def test_parse_json_response_embedded_in_text():
    text = 'Analysis complete. {"key": "value"} Done.'
    result = parse_json_response(text)
    assert result == {"key": "value"}


def test_parse_json_response_invalid_raises():
    with pytest.raises(ValueError, match="No JSON found"):
        parse_json_response("no json here at all")
