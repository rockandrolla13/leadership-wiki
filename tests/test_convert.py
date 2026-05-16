import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from convert import parse_stem, select_canonical, convert_pdf


def test_parse_stem_plain():
    base, version, paren = parse_stem("my-article")
    assert base == "my-article"
    assert version == -1
    assert paren is False


def test_parse_stem_versioned():
    base, version, paren = parse_stem("my-article_v2")
    assert base == "my-article"
    assert version == 2
    assert paren is False


def test_parse_stem_paren_dup():
    base, version, paren = parse_stem("my-article (1)")
    assert base == "my-article"
    assert paren is True


def test_parse_stem_versioned_case_insensitive():
    base, version, _ = parse_stem("doc_V3")
    assert base == "doc"
    assert version == 3


def test_select_canonical_keeps_highest_version(tmp_path):
    files = []
    for name in ["doc_v1.pdf", "doc_v2.pdf", "doc_v3.pdf"]:
        f = tmp_path / name
        f.write_text("x")
        files.append(f)
    kept, dropped = select_canonical(files)
    assert len(kept) == 1
    assert kept[0].name == "doc_v3.pdf"
    assert len(dropped) == 2


def test_select_canonical_single_file(tmp_path):
    f = tmp_path / "doc.pdf"
    f.write_text("x")
    kept, dropped = select_canonical([f])
    assert kept == [f]
    assert dropped == []


def test_select_canonical_drops_paren_dup(tmp_path):
    orig = tmp_path / "doc.pdf"
    dup = tmp_path / "doc (1).pdf"
    orig.write_text("x")
    dup.write_text("x")
    kept, dropped = select_canonical([orig, dup])
    assert len(kept) == 1
    assert kept[0].name == "doc.pdf"


def test_convert_pdf_success(tmp_path):
    src = tmp_path / "test.pdf"
    src.write_text("fake")
    dst = tmp_path / "test.md"
    with patch("convert.pymupdf4llm.to_markdown", return_value="# Converted\n"):
        status, detail = convert_pdf(src, dst)
    assert status == "OK"
    assert dst.read_text() == "# Converted\n"
    assert "bytes" in detail


def test_convert_pdf_fallback_to_pdftotext(tmp_path):
    src = tmp_path / "test.pdf"
    src.write_text("fake")
    dst = tmp_path / "test.md"
    dst.write_text("# Fallback content")
    with patch("convert.pymupdf4llm.to_markdown", side_effect=RuntimeError("bad pdf")):
        with patch("convert.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)
            status, detail = convert_pdf(src, dst)
    assert status == "FALLBACK"
    assert "pdftotext" in detail


def test_convert_pdf_failed(tmp_path):
    src = tmp_path / "test.pdf"
    src.write_text("fake")
    dst = tmp_path / "test.md"
    with patch("convert.pymupdf4llm.to_markdown", side_effect=RuntimeError("bad")):
        with patch("convert.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=1)
            status, detail = convert_pdf(src, dst)
    assert status == "FAILED"
