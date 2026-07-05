---
title: Agentic AI Architecture (InfoQ eMag)
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: reading
status: notes
level: intermediate
related:
  - reading/building-effective-agents.md
  - reading/agentic-sdlc-survey.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/cress-context-engineering.md
source: "https://www.infoq.com/minibooks/agentic-ai-architecture/"
updated: 2026-07-05
---

# Agentic AI Architecture (InfoQ eMag)

A **signpost note**, not a full summary. InfoQ's *Agentic AI Architecture* is a multi-chapter
eMag (reviewed by Rafał Gancarz, July 2026) framing agentic AI as an emerging **software
architecture paradigm** — the shift in focus from cloud-native/microservices optimisation to
architecting AI-driven systems. This note records the collection's structure and where it
overlaps the existing notes; the individual chapters would each merit their own capture from the
full text.

## Chapters

| Chapter | Author | Theme |
|---|---|---|
| From Microservices to Agents | Mallika Rao | Agents as the next evolution of distributed systems; **decision decomposition** paralleling microservice functional decomposition; new failure modes and observability needs |
| The Evolution of Agentic Harnesses | Karthik Ramgopal | Maturation of agent harnesses through design patterns: **chains → graphs → code** |
| A Systemic Approach to Memory, Knowledge, and Context | Adi Polak | **Context engineering** as a discipline; knowledge-layer quality; hallucination reduction |
| An Agentic AI Architecture Framework for Enterprises | Subash Natarajan & Ahilan Ponnusamy | A **three-tier** framework for design and delivery; industry-specific patterns; enterprise adoption |
| Current Challenges and Future Opportunities | Rafał Gancarz | Cross-industry architectural implications and required systemic adaptations |

## Where it overlaps existing notes

Much of this ground is already covered in the knowledge base, which is why this is a signpost
rather than a fresh deep-dive:

- **[Building Effective Agents](building-effective-agents.md)** — Anthropic's composition-pattern
  reference (workflows vs agents); the closest analogue to the eMag's harness/architecture
  chapters.
- **[Agentic AI in the SDLC — A Research Survey](agentic-sdlc-survey.md)** — the academic
  six-layer agent architecture, adjacent to the "microservices → agents" framing.
- **[Harness Engineering](../engineering/practices/harness-engineering.md)** — the anatomy of the
  harness program that the "chains → graphs → code" maturation describes at a pattern level.
- **[CRESS Principles for Context Engineering](../engineering/practices/cress-context-engineering.md)**
  — directly covers the memory/knowledge/context chapter's territory.

## If revisited

The genuinely distinct material worth capturing from the full text: the **distributed-systems
framing** (agents as the successor to microservices, with decision decomposition) and the
**chains → graphs → code** harness-maturation model. Both are TOC-level here; a proper note would
need the chapter contents.
