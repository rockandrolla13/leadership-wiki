#!/usr/bin/env python3
"""Convert PDFs (and plain-text files) in raw/ to markdown for LLM ingestion.

Primary: pymupdf4llm. Fallback: pdftotext -layout (requires poppler-utils).
Deduplicates by version: drops paren-copies and superseded _vN files.
Skips already-converted files unless --force is given.

Usage:
    python scripts/convert.py raw/articles/
    python scripts/convert.py raw/books/leadership.pdf
    python scripts/convert.py raw/ --out raw/_markdown/ --force
"""
from __future__ import annotations

import argparse
import logging
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import pymupdf4llm

PAREN_DUP = re.compile(r" \(\d+\)$")
TRAILING_VERSION = re.compile(r"_v(\d+)$", re.IGNORECASE)


def parse_stem(stem: str) -> tuple[str, int, bool]:
    """Strip paren-dup suffix, then trailing _vN. Returns (base, version_or_neg1, was_paren_dup)."""
    has_paren = bool(PAREN_DUP.search(stem))
    s = PAREN_DUP.sub("", stem)
    m = TRAILING_VERSION.search(s)
    if m:
        return s[: m.start()], int(m.group(1)), has_paren
    return s, -1, has_paren


def select_canonical(files: list[Path]) -> tuple[list[Path], list[tuple[Path, str]]]:
    """Group by base name; keep highest version, prefer non-paren original on tie."""
    groups: dict[str, list[Path]] = defaultdict(list)
    for f in files:
        base, _v, _p = parse_stem(f.stem)
        groups[base].append(f)

    kept: list[Path] = []
    dropped: list[tuple[Path, str]] = []
    for members in groups.values():
        if len(members) == 1:
            kept.append(members[0])
            continue
        scored = sorted(
            members,
            key=lambda p: (
                parse_stem(p.stem)[1],
                not parse_stem(p.stem)[2],
                p.stat().st_mtime,
            ),
            reverse=True,
        )
        kept.append(scored[0])
        for loser in scored[1:]:
            dropped.append((loser, f"superseded by {scored[0].name}"))
    return kept, dropped


def convert_pdf(src: Path, dst: Path) -> tuple[str, str]:
    """Convert one PDF to markdown. Returns (status, detail)."""
    try:
        md = pymupdf4llm.to_markdown(str(src))
        dst.write_text(md, encoding="utf-8")
        return ("OK", f"{len(md):,} bytes")
    except Exception as e:
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", str(src), str(dst)],
                capture_output=True, text=True, timeout=180,
            )
            if result.returncode == 0 and dst.exists():
                return ("FALLBACK", f"pymupdf4llm failed ({type(e).__name__}); used pdftotext")
            return ("FAILED", f"pymupdf4llm: {e}; pdftotext rc={result.returncode}")
        except Exception as e2:
            return ("FAILED", f"pymupdf4llm: {e}; pdftotext: {e2}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="PDF file or directory to convert")
    parser.add_argument("--out", type=Path, default=None, help="output dir (default: <source_dir>/markdown)")
    parser.add_argument("--force", action="store_true", help="re-convert even if output is up-to-date")
    parser.add_argument("--no-dedupe", action="store_true", help="skip version deduplication")
    args = parser.parse_args(argv)

    src = Path(args.source).resolve()
    src_dir = src if src.is_dir() else src.parent
    out_dir = (args.out or (src_dir / "markdown")).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    log = logging.getLogger("convert")
    log.info(f"source: {src}  →  output: {out_dir}")

    if src.is_file():
        pdfs = [src] if src.suffix.lower() == ".pdf" else []
        txts = [src] if src.suffix.lower() == ".txt" else []
    else:
        pdfs = sorted(src.glob("*.pdf"))
        txts = sorted(f for f in src.glob("*") if f.suffix.lower() == ".txt")

    if not args.no_dedupe and pdfs:
        kept, dropped_list = select_canonical(pdfs)
        for f, reason in dropped_list:
            log.info(f"SUPERSEDED  {f.name}  ({reason})")
        pdfs = sorted(kept)

    summary: list[tuple[str, str, float]] = []

    for pdf in pdfs:
        dst = out_dir / f"{pdf.stem}.md"
        if dst.exists() and not args.force and dst.stat().st_mtime >= pdf.stat().st_mtime:
            log.info(f"CACHED      {pdf.name}")
            summary.append((pdf.name, "CACHED", 0.0))
            continue
        t0 = time.perf_counter()
        status, detail = convert_pdf(pdf, dst)
        elapsed = time.perf_counter() - t0
        log.info(f"{status:<11} {pdf.name}  ({detail}, {elapsed:.1f}s)")
        summary.append((pdf.name, status, elapsed))

    for txt in txts:
        dst = out_dir / f"{txt.stem}.md"
        if dst.exists() and not args.force and dst.stat().st_mtime >= txt.stat().st_mtime:
            log.info(f"CACHED      {txt.name}")
            continue
        shutil.copyfile(txt, dst)
        log.info(f"COPIED      {txt.name}")
        summary.append((txt.name, "COPIED", 0.0))

    by_status: dict[str, int] = defaultdict(int)
    for _, s, _ in summary:
        by_status[s] += 1
    log.info("SUMMARY: " + ", ".join(f"{s}={c}" for s, c in sorted(by_status.items())))
    log.info(f"total time: {sum(t for _, _, t in summary):.1f}s")

    return 1 if any(s == "FAILED" for _, s, _ in summary) else 0


if __name__ == "__main__":
    sys.exit(main())
