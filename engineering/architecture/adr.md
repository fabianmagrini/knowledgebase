---
title: Architectural Decision Records (ADRs)
tags: [architecture, documentation, system-design, decision-making]
topic: engineering/architecture
status: notes
related:
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adrs-in-an-agentic-world.md
  - engineering/architecture/design-docs.md
  - engineering/architecture/c4-model.md
  - engineering/practices/code-review-policy.md
  - leadership/architecture-decision-forum.md
  - engineering/architecture/strangler-fig.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/thinking-in-constraints.md
source: "https://gist.github.com/fabianmagrini/76071cbc06aa1a5eafd19a7fb5ea2457"
updated: 2026-06-17
---

# Architectural Decision Records (ADRs)

An **ADR** is a short, version-controlled document that captures a single significant
architectural decision, its context, and its consequences. ADRs replace lengthy design
documents with lightweight, durable records — decisions treated as code artifacts, living
in the repo and reviewed like code.

They are the natural home for **Type 1 (one-way door)** decisions — see
[Agile Design Decisions](agile-design-decisions.md) — and for documenting deliberate,
prudent [technical debt](agile-design-decisions.md#technical-debt-as-a-tool).

## Structure

| Field | Captures |
|---|---|
| **Title** | The decision, e.g. "Use OAuth2 for Authentication" |
| **Status** | Proposed / Accepted / Deprecated (/ Superseded by ADR-NNN) |
| **Context** | What problem are we solving? What were the constraints? |
| **Decision** | What did we choose? |
| **Consequences** | The trade-offs — e.g. "More secure, but requires an external identity provider." |

## Why they work

- **Durable rationale.** Six months later the *why* survives, not just the *what* — the
  context and rejected alternatives are preserved.
- **Version-controlled.** Lives beside the code; changes go through review; history is
  auditable.
- **Lightweight.** Cheap enough to actually write, so decisions get recorded rather than
  lost in chat or meetings.
- **Status over deletion.** Superseded decisions are marked Deprecated, not erased — the
  trail of *how the architecture evolved* stays intact.

## Practice

- Write an ADR when a decision is consequential or hard to reverse, not for every choice.
- Number them sequentially (`adr-0001-...`) in a `docs/adr/` directory.
- Keep each to one decision; link related ADRs rather than bundling.
- Reference the relevant ADR from code reviews and design discussions.
