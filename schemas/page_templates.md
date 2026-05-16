# Page Templates

Use these templates when creating new wiki pages. Select the template that matches the page type. Fill in all sections; remove a section only if it is genuinely inapplicable, and note why.

---

## Concept Page

```markdown
---
type: concept
title: ""
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
---

# [Title]

## Definition

[One or two sentences. What is this concept? Be precise.]

## Why It Matters

[Why does this matter to a manager or leader? What goes wrong when it is absent?]

## When It Applies

[In what situations is this concept most relevant? What contexts make it especially important?]

## Key Principles

- [Principle 1]
- [Principle 2]
- [Principle 3]

## Practical Behaviors

[What does a leader actually do differently when applying this concept? Be specific and behavioral.]

- [Behavior 1]
- [Behavior 2]
- [Behavior 3]

## Common Failure Modes

[What are the ways people get this wrong? What does the failure look like in practice?]

- [Failure mode 1]
- [Failure mode 2]

## Diagnostic Questions

[Questions to ask yourself or the situation to determine if this concept is in play.]

- [Question 1]
- [Question 2]
- [Question 3]

## Useful Scripts

[Exact language the leader can use. No vague prompts — actual sentences.]

- **[Situation]:** "[Script]"
- **[Situation]:** "[Script]"

## Related Concepts

- [[related-page-1]]
- [[related-page-2]]

## Source Notes

[What do the sources say? Cite source slugs. Note any disagreements between sources.]

## Open Questions

[What is still unclear, contested, or context-dependent about this concept?]
```

---

## Framework Page

```markdown
---
type: framework
title: ""
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
---

# [Framework Name]

## Purpose

[What problem does this framework solve? What does it help a leader do or decide?]

## Core Idea

[The central mechanism or logic of the framework in 2–4 sentences.]

## Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]

## When To Use

[Specific conditions under which this framework is appropriate. Be concrete.]

## When Not To Use

[When does this framework fail or mislead? What situations does it poorly fit?]

## Example Application

[A concrete example of the framework applied to a real or realistic situation. Use roles, not names.]

## Failure Modes

[Ways the framework is commonly misapplied or produces bad outcomes when used incorrectly.]

- [Failure mode 1]
- [Failure mode 2]

## Adaptation For This User

[How should this framework be modified or weighted given what we know about the user's context, tendencies, or organization?]

## Related Pages

- [[related-page-1]]
- [[related-page-2]]

## Sources

[Which sources introduced or substantiated this framework? Cite source slugs.]
```

---

## Playbook Page

```markdown
---
type: playbook
title: ""
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
---

# [Playbook Title]

## Use Case

[Describe the specific situation this playbook addresses. When would a leader reach for this?]

## Diagnosis

[How do you know you are in this situation? What signals confirm it?]

## First Principles

[What are the underlying truths that make this playbook the right approach?]

## Step-by-Step Approach

1. [Step 1 — what to do and why]
2. [Step 2 — what to do and why]
3. [Step 3 — what to do and why]

## Suggested Language

[Exact scripts for key moments in this playbook.]

- **[Moment]:** "[Script]"
- **[Moment]:** "[Script]"

## What To Avoid

[Common mistakes, tempting but counterproductive moves, things that blow up the playbook.]

- [Avoid 1]
- [Avoid 2]

## Escalation Path

[If the standard steps fail, what is the next level of intervention? At what point should the leader escalate, and to whom or what?]

## Follow-Up Actions

[What should the leader monitor after executing this playbook? How will they know it worked?]

## Related Frameworks

- [[related-page-1]]
- [[related-page-2]]

## Sources

[Which sources informed this playbook? Cite source slugs.]
```

---

## Case Page

```markdown
---
type: case
title: ""
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
date: YYYY-MM-DD
people: []
status: open | resolved | stalled
---

# [Case Title]

## Date

[When did this situation occur or begin?]

## Context

[Brief background. What is the organizational setting? What is the user's role? What is the broader situation?]

## People / Roles Involved

[List roles only — no names. E.g., "the engineer", "the senior PM", "the skip-level manager".]

## Situation

[What happened? Describe the observable facts as accurately as possible.]

## Leadership Challenge

[What is the hard part? What makes this difficult to handle well?]

## Diagnosis

[What is the underlying problem? Distinguish surface symptoms from root causes.]

## Relevant Wiki Concepts

[Which wiki pages apply here? List them with [[wikilinks]].]

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| [Option A] | | |
| [Option B] | | |

## Recommended Action

[What should the leader do? Be specific about sequence and timing.]

## Script / Communication Plan

[Exact language for the most important conversation or message in this case.]

## Outcome

[What actually happened? Fill this in after the situation resolves.]

## Lessons Learned

[What does this case teach? What would the leader do differently next time?]

## Follow-Up

[Outstanding actions, open questions, or next check-in points.]

## Tags

[Repeat key tags for discoverability. E.g., delegation, underperformance, conflict.]
```

---

## Source Summary Page

```markdown
---
type: source
title: ""
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
related: []
author: ""
date: YYYY-MM-DD
source_type: book | article | podcast | transcript | paper | other
source_path: ""
ingested: YYYY-MM-DD
---

# [Source Title]

## Metadata

- **Author:** [Author name]
- **Date:** [Publication or recording date]
- **Type:** [book | article | podcast | transcript | paper | other]
- **Path:** [File path or URL]
- **Ingested:** [Date this was processed]

## Core Argument

[What is the central claim or thesis of this source? 2–4 sentences.]

## Key Leadership Insights

[Bullet list of the most actionable leadership insights from this source.]

- [Insight 1]
- [Insight 2]
- [Insight 3]

## Practical Applications

[How can the insights be applied? What should a leader do differently as a result of reading this?]

## Relevant Quotes

[Exact quotes (or close paraphrases for audio) that capture key ideas. Attribute each.]

> "[Quote]" — [Author, page or timestamp]

## Frameworks Extracted

[Any models, frameworks, or structured approaches introduced or elaborated by this source.]

- **[Framework name]:** [Brief description]

## Contradictions / Tensions With Existing Wiki

[Does this source contradict or qualify anything already in the wiki? Name the specific page and the tension.]

## Pages Updated

[Which wiki pages were updated during ingestion of this source? List file paths.]

- [wiki/path/to/page.md]

## Questions This Source Raises

[What does this source leave open, contested, or insufficiently addressed?]
```
