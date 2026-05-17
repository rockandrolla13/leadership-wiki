---
type: source
title: "Communicating with Data: Making Your Case with Data"
tags: [communication, data-visualization, persuasion-with-evidence, signal-vs-noise, presentation]
created: 2026-05-17
updated: 2026-05-17
sources: [allchin-communicating-with-data-2024]
related: [communication/persuasion, communication/stakeholder-updates, principles/decision-making, principles/decision-making-biases]
author: "Carl Allchin"
date: 2024-01-01
source_type: book
source_path: "raw/books/markdown/Communicating with Data Making Your Case With Data (Carl Allchin) (z-library.sk, 1lib.sk, z-lib.sk).md"
ingested: 2026-05-17
---

# Communicating with Data: Making Your Case with Data

## Metadata

- **Author:** Carl Allchin (data visualization specialist, The Information Lab)
- **Date:** 2024 (O'Reilly)
- **Type:** book
- **Path:** raw/books/markdown/Communicating with Data Making Your Case With Data (Carl Allchin) (z-library.sk, 1lib.sk, z-lib.sk).md
- **Ingested:** 2026-05-17

## Core Argument

A practitioner's manual for the (still rare) skill of making a decision-driving case with data. Allchin's frame: communication-with-data is its own discipline, not a hybrid of communication-plus-charts. Three-part structure: (1) the principles of communication (information theory, audience context, memory architecture); (2) the elements of data visualization (pre-attentive attributes, chart selection, layout, color); (3) deploying data communication in the workplace (stakeholder mapping, the executive ask, story-driven dashboards, governance of data products).

## Key Leadership Insights

- **Communication is signal-versus-noise, applied to evidence.** Shannon's information-theory frame applied to data: a sender encodes information, transmits it through a channel, the receiver decodes it. Each step introduces noise. The leader's job is to engineer the communication so signal dominates.
- **Audience context is unmarked and dominant.** A chart that lands with the engineering team will confuse the executive committee. *Experience, other messages, and market knowledge* shape what a given audience receives. Failing to model the audience's context is the single most common cause of data-communication failure.
- **Memory is layered: sensory → short-term → long-term.** Information that doesn't survive the transition from sensory to short-term is lost; from short-term to long-term, mostly forgotten within hours. Data-communication should target the memory layer matched to the purpose. *Action* requires short-term retention; *culture-building* requires long-term encoding.
- **Pre-attentive attributes are processed before conscious attention.** Length, 2D position, color hue, color intensity, shape, motion. These pre-cognitive cues do the heavy lifting of a chart — the message lands before the audience reads anything. Mis-using them (color for decoration rather than signal) actively misleads.
- **Charts are arguments, not decorations.** Every chart implicitly makes a claim. The discipline is to make that claim *intentional* — the chart should be the answer to a specific question, not an undirected summary of available data.
- **The right chart depends on the relationship being shown.** Comparison → bar. Trend over time → line. Composition → stacked bar or pie (sparingly). Distribution → histogram. Relationship between two variables → scatter. Geographic → map. Many "data viz failures" are *chart-type-to-relationship* mismatches.
- **Data-driven leadership is not the same as data-saturated leadership.** The leader who shows 30 charts in a meeting has made no argument. The leader who shows one — the *load-bearing* chart for the decision at hand — has made the case. Reeves's "dataism critique" (in HBR 2026) sits behind this: data should *inform* judgment, not *replace* it.
- **Stakeholder context determines the framing.** The CFO needs the variance-from-plan view; the operator needs the ratio-and-trend view; the board needs the strategic-position view. Same underlying data, three different communications.
- **Governance: data products have product managers.** Dashboards that are kept up, used, and trusted require ownership, versioning, and feedback loops. Without these, dashboards become "the truth" that is actually months out of date — and decisions drift away from reality.

## Practical Applications

- **For any data-supported recommendation, ask: what is the *one* chart that, if removed, breaks the argument?** That is the chart that should anchor the presentation. Everything else is support.
- **Match the chart type to the relationship before designing the chart.** What relationship am I claiming? (Comparison / trend / composition / distribution / scatter / geography.) Then design within that constraint.
- **Audit pre-attentive attributes deliberately.** Is the *most important* element the one with the most salient pre-attentive cue? If the brand color is on a low-information element and the signal is in gray, the chart is misleading.
- **Run a "stakeholder context" pass on every executive deck.** What does this audience already know? What other messages are they receiving this week? What's their default unit of analysis (dollars / percent / count / time)?
- **For each recurring dashboard, identify the *decision it informs.*** If you can't, kill the dashboard. Dashboards that don't drive decisions are organizational furniture.

## Relevant Quotes

> "Communication is the transfer of an idea, message, or feeling from one party to another. Every step in that process introduces the possibility of noise. The communicator's job is to engineer the signal so it dominates the noise."

> "Pre-attentive attributes — length, position, color, shape, motion — are processed by the visual system *before* conscious attention engages. They do the heavy lifting of the chart, whether you have designed them deliberately or not."

> "Audience context — their experience, the other messages they have received this week, their market knowledge — shapes what a given audience actually receives from your data. The same chart lands differently for the engineer and the executive."

> "A chart is an argument. Make the argument intentional."

## Frameworks Extracted

- **The Communication Process for Data:** information source → encoder → channel → decoder → receiver, with noise at each step.
- **Three Memory Layers:** sensory (sub-second), short-term (seconds-to-minutes), long-term (encoded for retrieval). Match the communication to the target layer.
- **Pre-Attentive Attributes:** length, 2D position, color hue, color intensity, shape, motion, orientation, area. Used deliberately, they pre-load the message.
- **Chart-Type-to-Relationship Map:** comparison (bar) / trend (line) / composition (stacked bar) / distribution (histogram) / scatter (scatter) / geography (map).
- **Three Pillars of Stakeholder Communication:** audience context modeling, decision-anchored chart selection, governance of data products.

## Contradictions / Tensions With Existing Wiki

- **Extends [[communication/stakeholder-updates]].** The wiki's stakeholder-updates page is about *narrative* communication to stakeholders. Allchin adds the data-presentation layer: what chart, how framed, for which audience.
- **Reinforces [[principles/decision-making-biases]].** Allchin's pre-attentive-attribute discipline is the *positive* counterpart to debiasing: deliberate chart design can either *reduce* the bias load (signal dominates noise) or *increase* it (color/layout choices that mislead).
- **Extends [[communication/persuasion]].** Conger's "provide vivid evidence" step (from [[sources/hbr-communication-vol1]]) is precisely the territory Allchin operationalizes. Vivid evidence in 2026 is usually a chart.

## Pages Updated

- wiki/sources/allchin-communicating-with-data-2024.md (this file, new)
- wiki/communication/stakeholder-updates.md (add Allchin's audience-context discipline + load-bearing-chart rule)

## Questions This Source Raises

- AI-generated dashboards and charts (Tableau Pulse, ChatGPT data interpretation) are starting to mediate between data and decision-maker. How does the data-communication discipline shift when the chart-designer is an agent rather than a human? Does the human's role become editor of agent output rather than author?
- The book treats data as primarily *quantitative.* Qualitative evidence — interview quotes, customer voice — is also a data type and is increasingly important. How do the same disciplines (audience context, signal dominance, decision-anchoring) apply to qualitative communication?
