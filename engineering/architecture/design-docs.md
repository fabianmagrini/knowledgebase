---
type: note
title: Writing an Effective Design Doc
description: "the design doc as an artifact: when it's worth writing, how much to invest, a selective component catalogue, concrete practices — plus the proof-of-work problem, since the thinking it forces was a property of writing being expensive, and study hall as the half that survives cheap generation"
tags: [architecture, documentation, system-design, decision-making, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/adr.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/c4-model.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/architecture/reversibility-decays.md
  - engineering/ai-native/accountability-for-unread-code.md
source: "https://refactoringenglish.com/excerpts/write-an-effective-design-doc/; https://alifeengineered.substack.com/p/on-the-death-of-amazons-writing-culture"
updated: 2026-10-25
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

## The forcing function was a property of the cost

*"The value of the document is the thinking it forces"* is the premise this whole note rests on.
It was true because writing was **expensive**, and that condition no longer holds automatically.

[Steve Huynh](https://alifeengineered.substack.com/p/on-the-death-of-amazons-writing-culture)
(October 2026) makes the point via Amazon, whose six-page narrative memo was the most
committed version of this practice anywhere. Jeff Bezos's rationale is unusually explicit that
the mechanism *was* the difficulty:

> Full sentences are harder to write. They have verbs. The paragraphs have topic sentences.
> There is no way to write a six-page, narratively structured memo and not have clear thinking.

**The memo was proof-of-work.** It was expensive to fake, so its existence certified the
thinking behind it — which is why the format could be trusted as a signal and why PowerPoint was
banned in 2004 for letting recipients miss critical ideas. Cheap generation voids the
certificate while leaving the ritual intact: the document still looks like six pages of
reasoning, and no longer evidences any.

That generalises past memos to every forcing-function artefact in these notes — design docs,
[ADRs](adr.md), PR descriptions, promotion packets. **Any practice whose value came from an
artefact being costly to produce loses its signalling value when production gets cheap**, and
keeps its appearance. The remedies are to re-establish cost somewhere, or to stop reading the
artefact as a signal and check the thinking directly.

> **How much to believe.** Huynh left Amazon in **2024** and says *"everything after that date
> is secondhand"*; his central evidence that this has actually happened is a single relayed
> anecdote (an L7 principal PM visibly reading his own six-page document for the first time, via
> an L6 who was in the room). He is a shareholder, now writes for an audience, and says *"I'd
> like to be wrong about this."* **The mechanism is portable; the claim that a culture has died
> is one story.**

### Study hall is the half that survives

The transferable practice is the one Huynh describes almost in passing: at Amazon the **first 30
minutes of a one-hour meeting are silent reading** — six-page printouts, annotated in red pen,
with discussion starting only once everyone has read the same thing.

That is the **reading** half of proof-of-work, and unlike the writing half it is unaffected by
generation getting cheap. A ritual that forces *consumption* still works no matter how the
document was produced. If the signalling value of authorship is gone, the enforced-reading half
is what is left worth keeping — and it is cheap to adopt without any of Amazon's apparatus.

Huynh cites a complementary policy from **Sophie Alpert at Clay**: stand behind every sentence,
treat writing as thinking, **spend more authorial time than reader time**, avoid unnecessary
length, and label generated text. The third is the usable test — it prices the document in the
author's attention rather than in its word count, which is the one quantity AI does not deflate.

**Not carried from that piece:** its headline proposal that *"two-way doors can be AI, one-way
doors require humans."* That is Bezos's own 2016 framework, already used above and held in depth
in [Agile Design Decisions](agile-design-decisions.md#reversibility--one-way-vs-two-way-doors) —
and [Reversibility Decays](reversibility-decays.md) is a direct objection to it: if two-way doors
lock behind you as dependencies accumulate, "this one is reversible, let the model write it"
understates the commitment being made. His other two rules have more teeth: **you own every
word**, with managerial consequences for passing generated text off as your own thinking, and
some documents are **always** human-written — he lists shareholder letters, OP1/OP2 planning,
PR-FAQs, new initiatives, major rearchitectures, performance reviews and promotion documents.

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
