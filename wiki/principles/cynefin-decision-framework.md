---
type: framework
title: "Cynefin Framework: A Leader's Framework for Decision-Making"
tags: [cynefin, decision-making, complexity, snowden, problem-classification]
created: 2026-05-17
updated: 2026-05-17
sources: [hbr-essential-leadership-guide]
related: [principles/decision-making, organization/change-management, organization/adaptive-organization, principles/decision-making-biases]
---

# Cynefin Framework

## Purpose

Different kinds of problems require different decision-making processes. Cynefin (Welsh for "habitat" or "place of belonging") gives the leader a discipline for *classifying* a problem before choosing how to address it. Most decision-making failures are *classification* failures — applying expert-driven analysis to a complex problem that requires experimentation, or applying experimentation to a problem that already has a known best practice.

## Core Idea

Five domains, each with a different decision-action pattern:

- **Simple / Obvious:** sense → categorize → respond. *Best practice* exists; the answer is known. Direct execution.
- **Complicated:** sense → analyze → respond. *Good practice* exists; the answer requires expertise. Bring in experts; analyze; decide.
- **Complex:** probe → sense → respond. *Emergent practice.* The cause-and-effect relationship is only knowable in retrospect. Run safe-to-fail experiments and see what emerges.
- **Chaotic:** act → sense → respond. *Novel practice.* No clear pattern. The first move is to *stabilize* — any action that creates enough order to move the problem into the Complex domain.
- **Disorder:** the unknown domain. The system has not yet identified which of the four other domains applies. Break the problem apart; classify the pieces.

The leader's first move on any consequential problem is to ask: *which domain is this in?*

## Steps

1. **Sense the problem.** Gather initial observation. What is happening?
2. **Classify the domain.** Use the diagnostic questions below.
3. **Apply the matched process:**
   - Simple: sense-categorize-respond.
   - Complicated: sense-analyze-respond.
   - Complex: probe-sense-respond.
   - Chaotic: act-sense-respond.
4. **Watch for domain transitions.** Problems move between domains as conditions change. A Complicated problem becomes Complex when a new variable is introduced. A Complex problem becomes Chaotic if a shock destabilizes the system.
5. **Re-classify.** Periodically test whether you are still operating in the right domain.

## Diagnostic Questions for Classification

- **Is cause and effect clear and repeatable?** → Simple/Obvious. (E.g., processing an expense report.)
- **Is cause and effect knowable through expert analysis?** → Complicated. (E.g., diagnosing a fault in a known system.)
- **Is cause and effect only knowable in retrospect, after probing?** → Complex. (E.g., launching a new product category.)
- **Is there no pattern, immediate threat, and a need to stabilize first?** → Chaotic. (E.g., crisis response in the first hours.)
- **Is the situation so unclear we can't even agree which domain applies?** → Disorder. (Most common at the start of a crisis. Resolve by breaking the situation into pieces.)

## When To Use

- Before any decision where the cost of getting it wrong is high.
- When the team is in disagreement about *how* to approach a problem (frequently this is a Cynefin-domain disagreement disguised as a substantive one).
- When a previously well-handled problem is suddenly producing bad outcomes — likely it has moved into a new domain.
- In post-mortems: which domain was the problem actually in? Which domain did we treat it as? The gap is often the lesson.

## When Not To Use

- For genuinely Simple problems with established best practice — Cynefin adds overhead without value.
- When the team is already aligned on the domain — don't re-litigate.
- As a substitute for substantive decision-making — Cynefin classifies the process, it does not produce the answer.

## Example Application

**Situation:** A high-performing engineering team is missing deadlines. The VP of Engineering is considering options.

- **Treating it as Simple:** "Hire faster, ship more." Misses the underlying issue.
- **Treating it as Complicated:** "Bring in a consultant to analyze the bottlenecks." Useful if the bottleneck is a known system issue.
- **Treating it as Complex:** "Run 3 experiments: pair-programming on one feature, mandatory afternoon focus blocks on another, code-review SLAs on a third. Measure for 4 weeks." Useful if the underlying causes are emergent — perhaps the team's makeup, the work's nature, or the organizational context have shifted.
- **Treating it as Chaotic:** "Pause feature work; do nothing but bug-fix and stabilize for two weeks." Useful only if the system is in actual crisis.

The diagnostic question: is the cause of the missed deadlines knowable through expert analysis (Complicated), or is it emergent and requires probing (Complex)? Most engineering-team performance issues are *Complex* but get treated as *Complicated.*

## Failure Modes

- **Default to Complicated.** Most expert-trained leaders treat every problem as Complicated and apply expert analysis. Many problems are actually Complex; the expert can't analyze them ex ante.
- **Apply Simple solutions to Complex problems.** Best practice presumes repeatable cause-and-effect. In a Complex domain, "best practice" usually fails.
- **Treat Chaotic as Complex.** In Chaotic, you must *stabilize first* (any action that creates order). Trying to "probe-sense-respond" in a true crisis is too slow.
- **Get stuck in Disorder.** Refusing to classify because the situation is unclear. Better to make a *provisional* classification and revisit than to remain in indecision.
- **Confuse domain transitions for failure.** A well-run problem moves from Complex to Complicated as you learn. This is *success,* not failure — but if the leader doesn't update the process, they'll continue running experiments on a problem that now has a known answer.

## Adaptation For This User

The wiki's user operates in technical leadership in financial services and AI-augmented environments — a context where:
- Many problems *look* Complicated (because experts and dashboards are readily available) but are actually *Complex* (because the AI-augmented system has emergent behavior).
- Crisis response (Chaotic) is rare but consequential. The discipline is *prepared* response — knowing the first 3 stabilization moves before the crisis.
- The hardest classification calls are between Complicated and Complex. Default to Complex when the system is new, when the team is new, or when the environment is changing fast.

## Related Pages

- [[principles/decision-making]] — Cynefin classifies the *process*; the decision-making page describes the *processes themselves*.
- [[principles/decision-making-biases]] — debiasing operates *within* a chosen process; Cynefin operates *upstream* of it.
- [[organization/change-management]] — Heifetz's adaptive challenges are largely Complex-domain problems. Both frames are compatible.
- [[organization/adaptive-organization]] — the Octopus Org's hypothesize-experiment-reflect-spread loop is the Complex-domain process operationalized.

## Sources

- [[sources/hbr-essential-leadership-guide]] — Snowden & Boone's "A Leader's Framework for Decision Making" (HBR 2007), reproduced in the Essential Guide collection.
