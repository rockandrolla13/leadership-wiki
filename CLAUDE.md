# Leadership Coach Wiki — Claude Code Instructions

## What This Is

A compounding leadership knowledge system. The `wiki/` directory contains structured markdown pages. You own this layer — you create, update, link, and maintain pages.

The `raw/` directory contains immutable source documents. You read but never write there.

The `schemas/` directory contains your operating instructions. Read them before significant operations.

## Answering Coaching Questions

When the user asks a leadership or management question:

1. Read `wiki/index.md` to identify the most relevant pages.
2. Load those pages.
3. Follow the protocol in `schemas/coaching_protocol.md`.
4. Produce a structured response (see coaching_protocol.md for formats).
5. Ask if the user wants to save the answer as a case page.
6. Append a log entry to `wiki/log.md`.

Never give generic advice. No "communicate clearly", "build trust", or "set expectations" without specific language and actions.

## Ingesting a Source Manually

When the user says "ingest this" and provides content or a file path:

1. Read `schemas/ingestion_protocol.md`.
2. Identify which existing pages to update and which new pages to create.
3. Update/create pages following the templates in `schemas/page_templates.md`.
4. Write a source summary to `wiki/sources/<slug>.md`.
5. Update `wiki/index.md`.
6. Append a log entry to `wiki/log.md`.

## Running a Lint Pass

When the user says "lint the wiki" or "health check":

1. Read all pages in `wiki/`.
2. Check for orphan pages, missing cross-links, stale pages, contradictions, recurring patterns.
3. Report findings by severity (Critical / Warning / Info).
4. Ask if the user wants fixes applied.

## Using the Python Scripts

For automated ingestion use the scripts:
```bash
python scripts/convert.py raw/articles/   # convert PDFs first
python scripts/ingest.py raw/articles/article.md
python scripts/coach.py "question here"
python scripts/lint.py
```

## Maintaining index.md

After every page create or update:
- Add or update the row in the relevant table in `wiki/index.md`
- Update the "Last updated" date header
- Keep summaries to one line
- Use 3–5 tags per page

## Maintaining log.md

Append to `wiki/log.md` after every ingest and every coaching query. Use the structured formats defined in `schemas/ingestion_protocol.md` and `schemas/coaching_protocol.md`.

## Quality Bar

See `schemas/LEADERSHIP_AGENT.md` for the full quality bar and list of banned phrases.

## Citation and Instructive Format

Every coaching answer must:
- Reference at least two wiki pages explicitly using [[wikilinks]]
- Include at least one direct quote from an ingested source
- Format each recommendation as: What to do / Why it works / What to say / What to watch for
- End with a footer listing all wiki pages consulted and sources used

Read `schemas/coaching_protocol.md` for the full required format.

## Sensitive Material

Use roles, not names, in case pages. Do not over-diagnose the user. Keep claims about recurring patterns grounded in specific case examples.
