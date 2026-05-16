# Leadership Wiki — System Overview

## What This Is

A compounding leadership knowledge system. Not a library. A living operating system for becoming a better leader and manager.

## The Four Layers

1. **Raw sources** (`raw/`) — immutable inputs: articles, books, notes, reflections. The LLM reads but never writes here.
2. **Wiki** (`wiki/`) — structured, interlinked markdown pages. The LLM owns this layer.
3. **Coaching layer** — the agent's applied reasoning: diagnose, recommend, script, file back.
4. **Schema layer** (`schemas/`) — operating instructions for the agent.

## How To Use It

**Ingest a source:**
```bash
python scripts/convert.py raw/articles/   # if PDFs — convert first
python scripts/ingest.py raw/articles/hbr-article.md
```

**Ask a coaching question:**
```bash
python scripts/coach.py "How do I handle an engineer who undermines the project in meetings?"
```

**Health-check the wiki:**
```bash
python scripts/lint.py
```

## The Goal

Over time, the wiki should stop giving generic advice and start giving advice that reflects your specific leadership style, recurring challenges, and organizational context. Every source ingested, every case filed, every coaching question answered makes the system more personalized.
