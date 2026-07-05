---
title: AI-DLC and the Reimagined SDLC
tags: [ai-engineering, architecture, reading, agentic-workflows]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/ai-native/ai-sdlc-terminology.md
source: "https://specs.md/methodology/sdlc-reimagined"
updated: 2026-06-20
---

# AI-DLC and the Reimagined SDLC

Traditional methodologies — Waterfall, then Agile — evolved when code production was the
expensive, slow part. AI inverts that assumption: code generation is now near-instant. The
argument here is that you don't retrofit AI into Agile; you reimagine the lifecycle for an
**Agentic Age** where AI plans, reasons, and executes while humans validate and oversee.

> "Faster horse chariots vs. automobiles" — bolting AI onto sprints is the faster chariot.

## The three eras of AI

| Era | Period | Pattern |
|---|---|---|
| **AI-Assisted** | 2020–2023 | Humans create, AI autocompletes |
| **AI-Driven** | 2023–2025 | AI proposes, humans approve |
| **Agentic** | 2025+ | AI executes autonomously, humans supervise |

## Why Agile ceremonies break

The methodology argues specific Agile mechanics become noise once prototypes materialise in
hours rather than weeks:

- **Two-week sprints** create artificial delay when a prototype takes hours.
- **Story points** lose meaning — AI execution time is disconnected from human effort.
- **Velocity** fluctuates with tool choice, not capability.
- **Standups / estimation ceremonies** surface status that automated systems could expose
  instantly.

## V-Bounce: humans as validators

Drawing on Crowdbotics research, humans shift from **primary implementers to validators and
verifiers**. The V-Model's implementation phase collapses from weeks to hours/days while humans
retain oversight rather than hands-on coding. Cited results: ~55.8% faster task completion and
70%+ efficiency in test generation. (Treat the figures as vendor-cited, not independently
verified.)

## AI-DLC — the proposed methodology

AWS's **AI-Driven Development Lifecycle** is offered as the concrete process. Three principles:

**The Reversed Conversation.** Instead of humans directing AI incrementally, AI analyses
intent, proposes the breakdown, and asks clarifying questions. Analogy: Google Maps — *humans
set the destination, AI provides the directions.*

**Three phases:**

1. **Inception (Mob Elaboration)** — *hours.* Converts Intents into Units and Stories through
   collaborative, shared-screen alignment. Replaces lengthy requirements phases.
2. **Construction (Mob Construction)** — *hours/days.* Generates domain designs, code, and
   tests; real-time clarification prevents hallucination and design degradation. Teams build in
   parallel after domain modelling.
3. **Operations** — *continuous.* Deployment, monitoring, maintenance.

**Bolts replace sprints.** Flexible, intent-driven execution cycles (hours/days) measured by
**business value delivered**, not story points.

## Vocabulary

| Term | Meaning |
|---|---|
| **Intents** | User goals needing translation into structured work |
| **Units** | Logical groupings of functionality |
| **Stories** | Granular, executable tasks |
| **Bolts** | Flexible execution cycles replacing fixed sprints |
| **Mob rituals** | Synchronous team-plus-AI collaboration sessions (Elaboration, Construction) |

## Landscape positioning

The methodology positions AI-DLC against lightweight spec tools — Spec Kit, BMAD, OpenSpec,
Kiro — claiming those handle *specifications* but not a *complete lifecycle* with formal
phases, design integration, and ritual frameworks.

## Relationship to the other notes here

This note is the **concrete, ceremony-level methodology**. It complements rather than repeats:

- [The Agentic SDLC](agentic-sdlc.md) — the *theory*: the cybernetic
  intent→spec→generate→evaluate→govern loop. AI-DLC is one concrete instantiation of that loop.
- [Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md) — the *staged adoption curve*.
  Running AI-DLC well looks roughly like operating at Levels 3–4.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — Bolts and continuous
  Mob validation are mechanisms for keeping change velocity within a system's safe absorption
  capacity.

### A note of caution

Much of this is vendor framing (AWS AI-DLC, Crowdbotics V-Bounce) with cited-but-unverified
metrics, and "Bolts/Units/Mob rituals" largely rename existing Agile concepts. The durable
insight is the shift — **humans as validators, ceremonies measured by value not effort, and
intent-driven cycles** — rather than the specific branded vocabulary.
