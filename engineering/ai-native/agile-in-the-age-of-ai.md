---
title: Agile in the Age of AI
tags: [ai-engineering, culture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-dlc-methodology.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/change-absorption-capacity.md
  - leadership/learning-organisation.md
  - leadership/revised-rules-engineering-leadership.md
  - engineering/ai-native/trust-factory.md
  - reading/multi-agent-coding-coordination.md
  - reading/what-is-software-engineering-ai.md
source: "https://miren.dev/blog/agile-in-the-age-of-ai"
updated: 2026-06-20
---

# Agile in the Age of AI

The argument is that Agile's principles stay valid when AI coding agents become co-authors, but
their application has to evolve because the participants and the pace have changed. The core idea
persists — build communication loops between the people who want software and the people who make
it — but humans now direct AI rather than writing the code directly. This is a recontextualisation
of Agile, not its replacement.

> This is a deliberate counterpoint to [AI-DLC and the Reimagined SDLC](ai-dlc-methodology.md),
> which argues that Agile ceremonies become obsolete and should be replaced. Read together, they
> bracket the debate: replace the ceremonies vs. keep the principles and let human pace bind.

## What changes

**The role shifts.** Developers move from authors to editors/directors. The stakeholder→author
feedback loop gains a nested loop: human and AI going back and forth on implementation.

**Sync points intensify.** Agile always emphasised checkpoints; AI's speed raises the stakes. An
agent can produce a thousand-line diff in minutes, which risks shallow review when a change
exceeds what can be meaningfully discussed in a single meeting.

**Review is collaboration, not a gate.** Review is reframed as being about *shared understanding*
rather than catching bugs — it keeps humans involved to build team coherence and repeatable
process, not primarily for defect detection. This echoes the "review for intent" stance in the
[code review policy](../practices/code-review-policy.md).

## What does not change: sustainable pace

The article leans on the Agile Manifesto's commitment that "Agile processes promote sustainable
development… maintain a constant pace indefinitely", and warns that an always-on AI makes overwork
easy to disguise as productivity.

- **Cognitive load is real.** The author reports managing about three parallel agents comfortably;
  beyond that, coherence dissolves. This is offered as a check on the idea of scaling to dozens of
  concurrent agents.
- **A sustainable baseline.** The author's personal observation: functioning well at 70–80% effort
  indefinitely, with roughly two-week bursts at 100% before recovery is needed.
- **Output ≠ value.** "Output isn't value. Effort isn't progress. The work still has to be worth
  doing." Tool speed should not be conflated with human capacity.

## Distinctive heuristic: unit of work = meeting scope

A right-sized change is one you could meaningfully discuss in a single meeting — substantial, but
coherent enough for full cognitive engagement during review. This becomes the discipline that
keeps AI-generated diffs within human comprehension.

## Concrete practices

- **Anchor work to issue tracking** (the author uses Linear), with written definitions before
  starting.
- **Right-size pull requests** to single-discussion coherence.
- **Mandatory human review** as a collaboration point, not gatekeeping.
- **Pace-first scheduling** — if the work is done by noon, the day ends.

### How the ceremonies evolve

- **Standups** still matter, but now track AI agent state alongside human work.
- **Sprint reviews** need tighter definition-of-done anchoring to resist AI-generated scope creep.
- **Retrospectives** should examine sustainable pace and cognitive load, not only velocity.
- **PR reviews** require deliberate sizing discipline to stay within human comprehension.
- **Pairing** shifts from pair programming to human–AI iteration with human review gates.

## Anti-patterns

- Rubber-stamp approvals when PR volume overwhelms review capacity.
- Managing an unsustainable number of concurrent agents.
- Letting tool speed justify more output rather than better outcomes.
- Treating review as theatre rather than a synchronisation mechanism.

## Relationship to other notes

- [AI-DLC and the Reimagined SDLC](ai-dlc-methodology.md) — the opposing framing (replace Agile
  ceremonies). The two notes together map the spectrum of the debate.
- [The Agentic SDLC](agentic-sdlc.md) — shares the "feeling fast, delivering slow" and
  output-is-not-value cautions at the lifecycle level.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — sustainable pace is the
  human-side analogue of keeping change velocity within a system's safe absorption capacity.
- [The Learning Organisation and AI Adoption](../../leadership/learning-organisation.md) — the
  cognitive-load and sustainable-pace concerns connect to slack and psychological safety.
