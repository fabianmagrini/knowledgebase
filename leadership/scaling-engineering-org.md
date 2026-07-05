---
title: Scaling an Engineering Organisation (20/50/200)
tags: [leadership, culture, decision-making, reading]
topic: leadership
status: notes
level: intermediate
related:
  - engineering/architecture/team-topologies.md
  - engineering/practices/team-topologies-agentic-platform.md
  - engineering/practices/ai-augmented-engineering-team.md
  - leadership/all-hands-meetings.md
  - leadership/engineering-leadership-overview.md
source: "https://greenido.dev/2026/06/11/what-changes-at-20-50-and-200-engineers/"
updated: 2026-07-05
---

# Scaling an Engineering Organisation (20/50/200)

Ido Green argues that scaling an engineering organisation is about **ownership clarity, not
headcount**. The force that reshapes structure at each threshold is the **coordination tax** —
the compounding overhead of meetings, handoffs, and dependencies — and the job at every stage
is to keep decision-making and accountability clear as that tax rises. The 20/50/200 figures
are illustrative thresholds from the author's experience (Google, Netflix, Meta, JFrog), not
hard rules.

## The three stages

| Stage | Mindset | What changes | Key move |
|---|---|---|---|
| **~20 — optimise for builders** | Speed is the edge; process is friction | Engineers talk to customers directly; end-to-end ownership (build, deploy, on-call, incidents) | **No platform team yet** — coordination cost exceeds the cost of duplication |
| **~50 — the coordination tax arrives** | Communication must become intentional, not organic | Dependencies materialise; planning gets harder; process becomes necessary | Every new process must name the **specific problem** it solves |
| **~200 — scaling ownership is the job** | Leadership manages *systems of teams*, not software | Org design rivals technical architecture in importance | Platform teams now justified (author suggests ~80–100 engineers) |

> "At 20 engineers, the cost of coordination is often higher than the cost of duplication."

## Cross-cutting ideas

- **Coordination tax.** Overhead that compounds with scale — the thing structure exists to
  manage. The premature-platform-team anti-pattern is paying it before it's due.
- **Ownership close to the work.** Builders should feel the consequences when systems fail; that
  feedback is what keeps accountability real. This is the same principle
  [Team Topologies](../engineering/architecture/team-topologies.md) encodes as aligning team
  boundaries to the systems they run.
- **Process as symptom / organisational theatre.** Process applied as a band-aid for unclear
  ownership creates *perceived* control without solving the root problem. Ask "what problem are
  we solving?" before adding a gate or a meeting.
- **Platform team as product, not gatekeeper.** A well-designed platform team has internal
  customers (engineers), measures success by whether they move faster, and acts as an
  accelerator — the same reframing in
  [Team Topologies for the Agentic Platform](../engineering/practices/team-topologies-agentic-platform.md).
- **On-call as the maturity diagnostic.** Green's claim: to gauge how mature an org really is,
  skip the dashboards and look at on-call. Healthy cultures treat incidents as learning feedback
  loops; unhealthy ones treat them as punishment.

## The AI-era twist

Green argues AI *magnifies* the need for ownership rather than reducing it:

> "When code generation becomes nearly free, you need stronger ownership models, not weaker
> ones, because the volume of code requiring review, maintenance, and architectural coherence
> goes up dramatically."

The bottleneck shifts from **code production to code confidence** — reviewing, understanding,
and maintaining changes while preserving architectural integrity. This is the org-structure
counterpart to the recomposition in
[The AI-Augmented Engineering Team](../engineering/practices/ai-augmented-engineering-team.md),
where value moves from typing to judgement and system design. The public-company transition
(JFrog) adds a further constraint: optimising for **speed *and* predictability** at once, which
Green frames as harder than pure startup scaling.

## Relationship to other notes

- **[Team Topologies and Socio-Technical Architecture](../engineering/architecture/team-topologies.md)**
  — the model (team types, cognitive load, Conway, platform teams). This note narrates *when*
  those forces bite as headcount grows and *when* a platform team is worth its coordination cost.
- **[Team Topologies for the Agentic Platform](../engineering/practices/team-topologies-agentic-platform.md)**
  — shares the platform-team-as-product reframing and the AI-era ownership argument.
- **[The AI-Augmented Engineering Team](../engineering/practices/ai-augmented-engineering-team.md)**
  — the same "AI makes ownership matter more" thesis, viewed as role recomposition rather than
  org scaling.
- **[Engineering Leadership — Overview](engineering-leadership-overview.md)** — the leadership
  map; this sits under *People & change*.
