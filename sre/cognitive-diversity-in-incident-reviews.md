---
title: Cognitive Diversity in Incident Reviews
tags: [leadership, culture, decision-making, reading]
topic: sre
status: notes
level: intermediate
related:
  - sre/self-blame-in-incident-reviews.md
  - sre/incident-swarming.md
  - leadership/decision-facilitation.md
  - leadership/learning-organisation.md
source: "https://www.honeycomb.io/blog/leveraging-cognitive-diversity-tackle-system-complexity"
updated: 2026-07-11
---

# Cognitive Diversity in Incident Reviews

Nick Travaglini argues that **identity diversity does not reliably improve decisions
about complex systems** — what matters is **cognitive diversity**: genuinely
different mental models of how the system actually works. Two engineers with the same
title may hold contradictory theories of a failure; two people in different roles may
share nearly identical ones, shaped by the same incidents and organisational
knowledge. Composing a group for *demographic* difference is not the same as composing
it for *cognitive* difference, and only the latter improves reasoning about
sociotechnical complexity.

## Why complexity needs multiple models

A production system is too large and interconnected for any single engineer to hold a
complete picture. A group whose members hold genuinely different mental models can:

- build a more accurate representation of how the system behaves,
- surface interdependencies any one person would overlook, and
- better predict the outcome of an intervention before it ships.

The author notes that integrating AI models as system dependencies widens the gap
between individual understanding and actual behaviour: they introduce opaque,
probabilistic failure modes that ordinary distributed-systems expertise does not
anticipate — raising the value of assembling different mental models rather than
deferring to one.

## Practices

| Practice | What it means | Why it helps |
|---|---|---|
| **Staff by vantage point, not org chart** | Include people from different knowledge sources — load-testing experience, customer support, on-call intuition — rather than by title or team | Assembles genuinely different models instead of similar ones |
| **Separate before synthesising** | Ask for written individual analyses *before* group discussion | Prevents authority bias and makes cognitive differences visible rather than smoothed over |
| **Treat disagreement as signal** | Persistent disagreement reveals a gap in collective understanding, not a dispute to settle | Points at what the group does not yet understand |
| **Stress-test changes independently** | Present a proposed fix to diverse thinkers separately | Convergent predictions suggest robustness; divergent ones flag assumptions worth testing before deployment |

The author is explicit that the aim is **productive disagreement**, not maximum
difference — it takes human judgement to convene the right vantage points, and the
goal is a truer collective picture, not conflict for its own sake.

## Relationship to other notes

- [Self-Blame in Post-Incident Reviews](self-blame-in-incident-reviews.md) — the
  complementary failure and fix in the same review: self-blame *narrows* the inquiry
  to one person; cognitive diversity *widens* it across many mental models. Both are
  about keeping the systemic investigation open.
- [Swarming in Incident Response](incident-swarming.md) — swarming assembles varied
  expertise *during* an incident by self-selection; this note assembles varied
  cognition *after* one by deliberate composition. Both reject the single-vantage-point
  bottleneck.
- [Facilitating Technical Decisions](../leadership/decision-facilitation.md) —
  "separate before synthesising" and "disagreement as signal" are facilitation moves:
  surfacing independent reasoning rather than driving to a single authority's answer.
- [The Learning Organisation and AI Adoption](../leadership/learning-organisation.md)
  — voicing a divergent mental model requires the psychological safety that note
  describes; cognitive diversity only pays off where people feel safe disagreeing.
