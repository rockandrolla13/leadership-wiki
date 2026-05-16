# Ingestion Protocol

You are processing a new source to integrate into the leadership wiki. Follow this protocol precisely.

## Step 1: Identify Leadership Insights

Read the source and extract:
- Core claims about leadership or management
- Reusable frameworks or models
- Specific behaviors and scripts
- Warning patterns and failure modes
- Evidence or examples

Ignore filler: biographical detail, general background, promotional content, repetition, non-leadership topics.

## Step 2: Decide Which Pages to Update

For each extracted insight, identify which existing wiki page(s) it most naturally belongs to. A single insight may belong to multiple pages.

Rules:
- Update an existing page if the insight directly extends, refines, or provides evidence for what the page already says.
- Create a new page if the insight introduces a concept, framework, or playbook that has no existing home.
- Do not create redundant pages. If a concept could live on an existing page, update the existing one.
- A single source may update 3–15 pages.

## Step 3: Write Cross-Links

When updating a page, add [[wikilinks]] to related concepts. Example: if updating `delegation.md`, link to `[[accountability]]`, `[[trust]]`, and `[[one-on-ones]]` where relevant.

## Step 4: Flag Contradictions

If the source contradicts or qualifies existing wiki content, note it explicitly in the source summary under "Contradictions / Tensions With Existing Wiki". Do not silently overwrite existing guidance. Instead, represent both positions and note the tension.

## Step 5: Planning Call JSON Format

When returning the planning JSON, use exactly this structure:

```json
{
  "pages_to_update": ["principles/delegation.md", "management/one-on-ones.md"],
  "pages_to_create": ["principles/psychological-safety.md"],
  "source_slug": "hbr-psych-safety-edmondson-1999",
  "key_concepts": ["psychological safety", "trust", "team performance"]
}
```

Rules for `source_slug`: lowercase, hyphens only, include author name or publication and year if known.

## Step 6: Update Frontmatter

When updating a page, always update the `updated` date in the frontmatter to today's date. Add the source slug to the `sources` list if not already present.

## Step 7: Update index.md

After all page writes, rewrite `wiki/index.md` to reflect:
- New pages added (with a one-line summary and correct tags)
- Updated pages (refresh the "Updated" date in the relevant table row)
- Update the total page count in the header
- Maintain existing table structure and all existing rows
