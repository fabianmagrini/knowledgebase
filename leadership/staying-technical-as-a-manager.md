---
type: note
title: Staying Technical as a Manager
description: "Karol Wojciszko argues managers should code a small, fixed fraction of their week — not to ship, but to keep first-hand contact with what their engineers experience."
tags: [leadership, ai-engineering, culture, reading]
topic: leadership
status: notes
level: intermediate
related:
  - leadership/engineering-manager-role.md
  - leadership/revised-rules-engineering-leadership.md
  - leadership/learning-culture-ai-agents.md
  - leadership/engineering-leadership-overview.md
  - engineering/ai-native/scaling-ai-adoption.md
  - engineering/ai-native/cress-context-engineering.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/ai-native/ai-native-engineering-overview.md
source: "https://karolwojciszko.substack.com/p/how-to-stay-technical-as-a-manager"
updated: 2026-07-26
---

# Staying Technical as a Manager

Karol Wojciszko argues that engineering managers should spend a small, *fixed* share of
their week writing code in their team's stack — his figure is **5–10%, roughly four hours**
— for the sake of first-hand contact with the daily reality of the work, not to deliver
features. Treat the percentage as his prescription rather than a researched benchmark; the
argument stands on the mechanism, not the number.

## The middle path

He frames the note against two positions he considers extremes:

| Position | His objection |
|---|---|
| "Managers shouldn't code at all" | Without hands-on work, a manager cannot genuinely understand where the pipeline hurts, why estimates slip, or what the team is actually complaining about. |
| "Managers must stay deeply technical" | Competing with full-time engineers on depth is unrealistic and displaces the work only a manager can do. |

The middle path is deliberate, bounded exposure. The point is **empathy through
experience** — knowing the friction directly rather than through status reports.

His enabling claim is an AI-native one: unfamiliarity with the team's language is no longer
a reason to stay out, because a model can "translate the unfamiliar into the familiar"
through analogy to a stack the manager already knows. This is what makes a 5% time budget
plausible where it previously wasn't.

## Structured scarcity

A recurring, *calendared* slot — his example is every other Friday — survives schedule
disruption in a way that ad-hoc intention does not. A manager's week is the first thing to
be colonised by other people's urgency, so an unbooked commitment to "code sometimes"
reliably decays to zero.

He also rejects **"steal time"** as a framing for this. Describing it as time stolen from
the real job concedes that the coding is illegitimate; he treats it as part of the role.

## Choosing the right task

The selection criteria are the most transferable part of the piece. A suitable task has:

- **No attached deadline** — the manager's availability is unreliable by design
- **A single service or project** — avoids paying the context cost of several systems
- **No blocking dependencies** — nobody waits on a part-time contributor
- **Self-contained scope**
- **A built-in backlog**, ordered easiest to hardest, so difficulty ramps with familiarity

The common thread: pick work where a manager's unpredictable availability cannot become
someone else's problem.

## The working loop

His six-step flow for actually doing the task:

| Step | Purpose |
|---|---|
| 1. Learn the project by asking a model questions | Orientation before commitment |
| 2. Run it, touch it, deliberately break it | Build a mental model from behaviour, not docs |
| 3. Brainstorm an implementation plan before coding | Decide the *why* explicitly, and record it |
| 4. Self-review, requiring the model to explain its choices | Guards against accepting unexamined output |
| 5. Verify the thing works — not just that tests pass | The green checkmark is not the goal |
| 6. Go through the team's real code review process | Experience the process you own |

Two habits he stresses within this: challenge the model's architectural suggestions against
the patterns already in the codebase, and don't chase perfect understanding of the project
before starting — the task is the vehicle for understanding.

## On the tooling advice

The second half of the article gives specific agent-workflow guidance — assigning cheaper
models to learning and analysis and stronger ones to implementation, tuning thinking effort,
starting a fresh session per task, archiving sessions by feature, keeping the context window
under roughly 60–70% to avoid **context rot** (accumulated session history degrading output
quality), and using token-compression tooling.

The *principles* here are durable and covered in more depth elsewhere in these notes — see
[CRESS Principles for Context Engineering](../engineering/ai-native/cress-context-engineering.md)
for context hygiene and [Model Routing and AI Gateways](../engineering/ai-native/model-routing-and-ai-gateways.md)
for matching task difficulty to model cost. The *specific* tier assignments in the article
are a mid-2026 snapshot and date quickly as model generations turn over; take the shape of
the advice rather than the model names.

## Relationship to other notes

- [The Engineering Manager Role](engineering-manager-role.md) — the four pillars of what a
  manager is for. This note addresses a dimension that framing leaves out: how the manager
  stays in contact with the technical work itself.
- [Revised Rules of Engineering Leadership](revised-rules-engineering-leadership.md) — the
  same argument at executive altitude, where Will Larson holds that CTOs must become
  "substantially more technical and less bureaucratic". Both claim technical currency is
  becoming *more* load-bearing for leaders as AI accelerates execution, not less.
- [A Learning Culture for AI-Augmented Teams](learning-culture-ai-agents.md) — the team-level
  counterpart; a manager who has used the tools is better placed to lead that shift.
- [Scaling AI Adoption in the SDLC](../engineering/ai-native/scaling-ai-adoption.md) —
  adoption as an organisational programme, where this note is the individual leader's habit.
