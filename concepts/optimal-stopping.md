---
type: note
title: Optimal Stopping and the 37% Rule
description: "The secretary problem: look at 37% of options without committing, then take the first one that beats everything seen — why 1/e, which assumptions it needs, and why the popular hiring application is the weakest one."
tags: [decision-making, reading]
topic: concepts
status: notes
level: intermediate
related:
  - product/explore-vs-exploit.md
  - concepts/theory-of-constraints.md
  - leadership/first-principles-thinking.md
  - engineering/architecture/agile-design-decisions.md
source: "https://read.perspectiveship.com/p/secretary-problem"
updated: 2026-08-03
---

# Optimal Stopping and the 37% Rule

The **secretary problem** is the canonical optimal-stopping result. You see candidates one at
a time, must accept or reject each immediately, and cannot go back. How long should you look
before committing?

The answer: spend the first **~37%** of your options purely observing — a **calibration
pool** — noting the best you see but rejecting all of them. Then take the first candidate
that beats that benchmark. With 12 candidates, look at 4, then commit to the next one better
than all four.

The 37% is **1/e ≈ 0.368**, and it is both the optimal proportion to sample *and* the
resulting probability of ending up with the single best option.

This is a classical result, not a recent finding; the note is filed from a newsletter
explainer that presents it clearly, but the mathematics is public domain. Brian Christian and
Tom Griffiths' *Algorithms to Live By* (2016) opens with a book-length treatment.

## Why there is an optimum at all

The rule sits between two failure modes, which is the durable intuition even if you never use
the number:

| Look too little | Look too much |
|---|---|
| You commit before you know what "good" looks like — your benchmark is uncalibrated, so you accept mediocrity confidently | The best candidate has probably already appeared and been rejected, and you are left taking whatever is last |

Sampling buys calibration; every additional sample costs you a chance that the best has
already gone by. 1/e is where those two curves cross.

## The assumptions, which matter more than the number

The 37% rule optimises exactly one thing: **the probability of selecting the single best
option**. It requires all of the following:

| Assumption | How often it holds |
|---|---|
| **No recall** — rejected options are gone permanently | Rarely; you can usually go back |
| **Offers always accepted** | No; candidates and sellers decline |
| **Only the best counts** — second place scores the same as last | Almost never; second-best is usually fine |
| **N is known in advance** | Often not |
| **Ordinal ranking only** — you can rank but not score | No; you usually have a sense of *how much* better |

That third row is the one that breaks it. If the objective is **maximising expected quality**
rather than **probability of getting the exact best**, the optimal threshold moves and the
shape of the advice changes — you should commit earlier, because a very good option in hand
beats a small chance at the perfect one. Most real decisions have that objective.

Which makes hiring — the application the rule is most often attached to, including in the
source article — the case where its assumptions fail hardest. Real hiring has recall, has
declined offers, has cardinal quality judgements, has no fixed N, and does not care whether
you got the theoretical best.

## What it is actually good for

Read as a procedure it is fragile. Read as a **prior**, it is durable:

- **Deliberate calibration is not indecision.** There is a principled reason to look without
  committing early on, and "we're still gathering signal" is a real phase rather than an
  excuse.
- **Set the switch point in advance.** The rule's actual discipline is deciding *before you
  start* when you will stop calibrating — which defuses the two ways search goes wrong, drift
  and premature commitment.
- **Roughly a third, not a half.** The useful takeaway is directional: commit sooner than
  feels comfortable. The instinct to keep looking is usually the more expensive error.

The formalism is doing less work here than the framing. Its value is as an argument that
there *is* an optimum — that both endless deliberation and snap commitment are mistakes with
a definable point between them.

## Relationship to other notes

- [Exploring vs Exploiting in Product Discovery](../product/explore-vs-exploit.md) — the same
  tension without the formalism, and at organisational rather than individual scale. Explore
  is the calibration pool; exploit is committing past the threshold. That note's
  **local-maxima** risk is the cost of switching too early, which the 37% rule quantifies for
  one very restricted case.
- [Agile Design Decisions](../engineering/architecture/agile-design-decisions.md) —
  **irreversibility** is precisely the condition that makes optimal stopping bite. Two-way-door
  decisions have recall, so the rule does not apply and you should just decide; one-way doors
  are where deliberate calibration earns its cost.
- [First-Principles Thinking](../leadership/first-principles-thinking.md) — a worked example
  of the payoff and the trap: deriving a decision rule from the structure of the problem, and
  then having to check whether that structure is the one you actually face.
