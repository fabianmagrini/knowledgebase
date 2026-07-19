---
type: note
title: Own the Outer Loop
description: "Agents run the inner execution loop; humans own the outer accountability boundary — constraints, sampling, audit, ownership, and governance."
tags: [ai-engineering, agentic-workflows, governance, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/ai-engineering-discipline.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/loop-driven-development.md
  - reading/ownership-thorsten-ball.md
source: "https://addyo.substack.com/p/own-the-outer-loop"
updated: 2026-07-11
---

# Own the Outer Loop

Addy Osmani argues that as coding agents become more capable, human oversight should
move *outward*: stop occupying the agent's execution loop, and instead own the
**accountability boundary** around it. The obligation grows with the leverage — before
a change reaches production, "someone must be able to explain exactly what changed, why
it was safe."

## Inner loop vs outer loop

| | Owned by | Contains |
|---|---|---|
| **Inner loop** | Agents | Investigate → implement → verify, repeated continuously with minimal interruption |
| **Outer loop** | Humans | Defining constraints, sampling review, retaining audit evidence, and the production ownership decision |

The outer loop is where humans keep the final verdict. Osmani's caution is a
**trust–verification gap**: he cites the Sonar 2026 report that ~42% of committed code
is now AI-generated or assisted, while organisations lack consistent verification —
distrust of AI code that is not operationalised into process. *(These figures are
author-cited from third-party research.)*

## Three hidden costs of delegation

Osmani names three costs, each supported by a cited study:

- **Cognitive surrender** — accepting AI output uncritically (a Wharton study is cited
  for 73% accepting incorrect suggestions with *increased* confidence).
- **Cognitive debt** — understanding erodes as work is delegated (an Anthropic RCT is
  cited: ~50% vs 67% on comprehension). This is the [comprehension-debt](loop-driven-development.md)
  caution seen from the accountability side.
- **Orchestration tax** — steering, sorting, and verifying multiple agents cannot itself
  be automated, and human attention does not parallelise.

## What humans own: five loops

Rather than sit in the inner execution loop, humans should control:

1. **Constraints** — what inputs and rules bound the work.
2. **Sampling** — how much to review (review high-stakes decisions and dangerous
   assumptions first, not everything).
3. **Audit** — what evidence is retained.
4. **Ownership** — responsibility for the production boundary.
5. **Governance** — the pre-deployment decision (moved *before* acceptance, not after).

## Quality → Verdict → Answerability

The evidence flow across the accountability boundary:

| Stage | What it is |
|---|---|
| **Quality** | Pre-deployment checks that produce evidence |
| **Verdict** | The human production decision: ship, block, redirect, narrow, or reject |
| **Answerability** | The demonstrable capacity to explain that decision if later questioned |

Osmani proposes making this concrete with **accountability contracts**: record the
checklist understood when a change was accepted, the evidence behind the decision, who
was responsible, and the system's status after any block. Practical corollaries:
grant agents *just enough autonomy* to stay controllable, make production change
**opt-in**, and treat human attention as a first-class architectural constraint.

## Relationship to other notes

- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — the *mechanism*
  layer beneath this note: machine-readable sensors that keep the inner loop correcting
  itself. Backpressure is how the outer loop's constraints are enforced inside the inner
  loop; this note is the human-governance framing around it.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — Osmani's "just enough
  autonomy" and agency ladder are the dial; this note is about who holds it and stays
  answerable for where it is set.
- [AI Demands More Engineering Discipline](ai-engineering-discipline.md) — the shift from
  reviewing code to validating behaviour; answerability and audit are the accountability
  expression of that discipline.
- [Agentic Code Review](agentic-code-review.md) — review as the new bottleneck; the
  sampling and verdict loops here are the governance view of that same reviewing role.
- [Loop-Driven Development](loop-driven-development.md) — the loop anatomy and the
  comprehension-debt / cognitive-surrender cautions this note reframes as accountability
  costs.
