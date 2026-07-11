---
type: note
title: Writing an Effective Design Doc
description: "the design doc as an artifact: when it's worth writing, how much to invest, a selective component catalogue (goals/non-goals, scenarios, SLOs, alternatives considered, trust boundaries), and concrete practices; the larger up-front cousin of the ADR"
tags: [architecture, documentation, system-design, decision-making, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/adr.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/c4-model.md
  - engineering/ai-native/spec-driven-development.md
source: "https://refactoringenglish.com/excerpts/write-an-effective-design-doc/"
updated: 2026-07-05
---

# Writing an Effective Design Doc

A **design doc** is the artifact you write *before* implementation to force critical
architectural thinking, coordinate decisions across a team, and catch expensive mistakes
while they are still cheap to fix. Michael Lynch's argument (an excerpt from *Refactoring
English*) is that the value of the document is the thinking it forces, not the paperwork —
so it should be sized to the risk, and its sections chosen selectively rather than filled
in by rote.

This note is about the **document** as a whole. Its lightweight cousin, the
[ADR](adr.md), records a *single* consequential decision; a design doc is the larger
up-front artifact that may spawn several ADRs.

## When a design doc is worth writing

The payoff scales with the cost of getting it wrong. Lynch's signals that a doc earns its
keep:

- **Complexity** — many moving parts or non-obvious interactions.
- **Duration** — projects expected to run 3+ months.
- **Production lifespan** — the longer it lives, the longer a bad decision hurts.
- **Cross-team coordination** — the doc becomes the shared contract.
- **Catastrophic risk** — security, data loss, or reputational exposure.

There is **no universal rule** for how much to invest; it depends on the team's goals,
risks, deadlines, and culture. The framing echoes reversibility: spend on the decisions
where the *penalty for being wrong* is high, and skip the doc for changes you can back out
in an afternoon — the one-way vs. two-way door test from
[Agile Design Decisions](agile-design-decisions.md#reversibility--one-way-vs-two-way-doors).

## Component catalogue

The sections are a **menu, not a checklist** — include only those that carry weight for
this project.

| Section | Captures |
|---|---|
| **Title & metadata** | Author, creation date, an authoritative (short-)link URL |
| **Objective** | What this design is trying to achieve, in a sentence or two |
| **Background** | Context a reader needs to evaluate the design |
| **Goals / Non-Goals** | Explicit scope — Non-Goals prevent scope misunderstandings |
| **Scenarios** | Practical pictures of how the finished system behaves in real use |
| **Diagrams** | Visual structure — see below |
| **Glossary** | Unfamiliar terms, defined inline where possible |
| **Constraints** | Fixed limits the design must respect |
| **SLOs** | Measurable targets — uptime, latency percentiles, throughput/scale |
| **Monitoring & alerting** | How you will know the running system is healthy |
| **Interfaces** | APIs and contracts exposed or consumed |
| **Dependencies / infrastructure** | What the design relies on to run |
| **Security & privacy** | Attack surface, trust boundaries, data handling |
| **Legal & logging** | Compliance considerations and what gets logged |
| **Timeline** | Rough schedule / estimation |
| **Alternatives considered** | Options rejected and *why* — preserves rationale |
| **Open / resolved issues** | Outstanding decisions: problem, options, next step |

### A few sections worth calling out

- **Non-Goals** are as valuable as goals — they are the explicit scope boundary that stops
  reviewers arguing about work you never intended to do.
- **SLOs vs. SLAs.** An SLO is a measurable performance target (99.9% uptime, p99 latency);
  an SLA adds a *financial penalty* for missing it. Design docs specify SLOs; latency is
  best stated as percentiles, not averages.
- **Alternatives considered** is where the doc earns its long-term value — six months later
  the *why we didn't* survives alongside the *what we did*, the same durability argument that
  motivates [ADRs](adr.md).
- **Security** hinges on identifying **trust boundaries** — where data crosses between
  privilege levels — and the **attack surface** where the system processes potentially
  malicious input.
- **Open issues** should be structured: problem statement, the options, and the immediate
  next step — not just a question mark.

## Concrete practices

- **Editable diagrams over whiteboard photos.** Use tools that let you revise the diagram
  as the design changes — Excalidraw, draw.io, [Mermaid](c4-model.md), D2, Graphviz — rather
  than a photo of a whiteboard that rots on first edit. LLMs can help generate the diagram
  source. See the [C4 Model](c4-model.md) for a diagramming vocabulary that fits here.
- **Write scenarios, not just structure.** A concrete walk-through of the finished system in
  a real situation communicates far more than a box diagram alone.
- **Define terms inline.** Prefer defining an unfamiliar term where it appears over sending
  the reader to a separate glossary.
- **Include real metadata.** Author, date, and a stable canonical URL make the doc citable
  and findable later.

## Relationship to other notes

- **[ADR](adr.md)** — the design doc's lightweight cousin. A design doc reasons about the
  whole design up front; ADRs capture individual consequential decisions as durable,
  version-controlled records. A single design doc often produces several ADRs.
- **[Agile Design Decisions](agile-design-decisions.md)** — supplies the *reversibility and
  blast-radius* frameworks that tell you how much to invest here; the design doc is where
  that thinking gets written down for the high-penalty decisions.
- **[C4 Model](c4-model.md)** — a concrete diagramming approach for the Diagrams section.
- **[Spec-Driven Development](../ai-native/spec-driven-development.md)** — an adjacent design
  artifact from the AI-agent world, where an executable spec (not prose) is the primary
  thing engineers iterate on.
