---
title: Factory Engineers, Not Product Engineers (Warp)
tags: [ai-engineering, agentic-workflows, leadership, reading]
topic: reading
status: notes
level: intermediate
related:
  - case-studies/portkey-product-engineer-company.md
  - engineering/practices/agentic-sdlc.md
  - reading/multi-agent-coding-coordination.md
  - engineering/practices/apex-framework.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/practices/ai-native-engineering-overview.md
  - engineering/practices/ai-factory.md
source: "https://www.warp.dev/blog/we-are-now-factory-engineers-not-product-engineers"
updated: 2026-06-27
---

# Factory Engineers, Not Product Engineers (Warp)

Notes on Warp's argument that the unit of engineering work is moving up a level:
from building a product to **building the system that builds the product** —
"it's to build the thing that builds that product." Where a product engineer
ships features, a **factory engineer** builds and optimises the automated software
"factory" that ships them.

It reads as a deliberate counterpoint to the
[product-engineer model](../case-studies/portkey-product-engineer-company.md):
both name a new engineer archetype, but draw the abstraction line in different
places — product engineer *owns the product end to end*; factory engineer *owns
the machine that produces it*.

## Product engineer vs. factory engineer

| | Product engineer | Factory engineer |
|---|---|---|
| Builds | The product | The system that builds the product |
| Success metric | Features shipped | % of changes shipped automatically; shipped output ÷ (inference cost + human time) |
| Human coding | The job | A *cost centre* and, ideally, the exception |

## The factory workflow

The proposed pipeline is a chain of specialised agents with one human checkpoint:

```txt
1. Triage agent      — assess automatable scope
2. Spec agent        — clarify ambiguities (if needed)
3. Implementation    — write the code
4. Code review agent — evaluate
5. Verification      — validate functionality
6. Human review      — the checkpoint
7. CI/CD
8. Deploy
9. Monitoring agent  — detect failures, closing the loop
```

This is the concrete, role-per-stage instantiation of an orchestrated agent
pipeline — the same shape as the
[multi-agent coding swarm](multi-agent-coding-coordination.md), framed as a
production line rather than a coordinated swarm.

## The reframes

- **Software as variable cost, not R&D.** Production shifts from an R&D expense to
  COGS, demanding measurable ROI: *does $1 on automation infrastructure generate
  >$1 of shipping capacity?*
- **Every human intervention is a process failure.** "Pulling stuff off the
  factory floor" — a manual change — is treated as process debt to post-mortem and
  automate away, not acceptable work.
- **Recursive self-improvement.** A well-designed factory records interventions,
  pattern-matches them, and optimises itself toward fuller automation.
- **Meta-engineering.** The skill becomes engineering the *system in which* coding
  agents operate effectively, and reframing token budgets as cost-centre
  accountability rather than unlimited interactive coding.
- **Metric shift.** From "how fast can my team code?" to "how efficiently can my
  *system* code?" — the same move from coding speed to system-level outcomes that
  [APEX](../engineering/practices/apex-framework.md) makes by measuring at the
  critical path.

## Vendor caveat

The piece is published by Warp to promote **Oz**, its agent-orchestration
platform, so the framing is directional marketing as much as analysis. The proof
points — Rectangle Health shipping 35K+ lines weekly via an AI teammate, and
`build.warp.dev` listing ~1,300 ready-to-implement issues — are vendor-reported
and unverified here. The reusable idea is the *factory-efficiency* lens and the
metric shift; treat the autonomy claims as aspiration.

## Relationship to other notes

- [The Product Engineer Company (Portkey)](../case-studies/portkey-product-engineer-company.md)
  — the matched debate: own-the-product vs. own-the-factory. Portkey keeps humans
  central to every change; Warp wants each human change to become rarer.
- [The Agentic SDLC](../engineering/practices/agentic-sdlc.md) — "the harness is the
  product" and the cybernetic loop; the factory is that idea pushed to an
  org-operating model.
- [Multi-Agent Coding Without Worktree Chaos](multi-agent-coding-coordination.md) —
  the agent-coordination machinery a factory runs on.
- [The APEX Framework](../engineering/practices/apex-framework.md) — the measurement
  discipline behind "factory efficiency" and continuous ROI.
- [The AI-Augmented Engineering Team](../engineering/practices/ai-augmented-engineering-team.md)
  — the operating model the factory framing radicalises.
