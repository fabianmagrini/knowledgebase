---
type: note
title: Finding Problems to Solve as a Staff Engineer
description: "Lalit Maganti's practice for sourcing staff-level work: absorb organisational noise passively, let problems accumulate until they resurface, find the common shape beneath separate requests, and pressure-test in proportion to confidence."
tags: [leadership, decision-making, reading]
topic: leadership
status: notes
level: intermediate
related:
  - leadership/senior-ic-role.md
  - leadership/raising-problems-without-complaining.md
  - engineering/architecture/over-engineering.md
  - leadership/principal-engineer-influence.md
  - leadership/first-principles-thinking.md
  - product/explore-vs-exploit.md
  - leadership/engineering-leadership-overview.md
source: "https://lalitm.com/post/find-problems-staff-engineer/"
updated: 2026-08-03
---

# Finding Problems to Solve as a Staff Engineer

Lalit Maganti (July 2026) describes how he sources staff-level work: not by being assigned it,
but by identifying problems the organisation has not yet articulated. [The Senior IC
Role](senior-ic-role.md) holds that senior ICs are responsible for *defining* the problem and
for bringing focus to neglected cross-cutting areas; this is the step before that — where a
problem comes from in the first place.

One practitioner's experience, no research. The scope limit is his own and matters: this comes
from infrastructure and developer-tools work at large technology companies with **bottom-up
autonomy**, and he says directly that it applies less in top-down hierarchical environments.
"Accumulate problems and choose your own" assumes latitude that many staff engineers do not
have.

## The practice

| | |
|---|---|
| **Listen as a sponge** | Absorb the ordinary noise — meetings, chat, presentations — rather than booking dedicated strategic-thinking time. The problems surface in the day-to-day traffic, not in a slot in the calendar. |
| **Dig beneath the request** | Ask *why* repeatedly. What arrives is usually a proposed solution; the problem is underneath it. |
| **Accumulate before acting** | Let problems pile up rather than acting on the first. What resurfaces across several teams over time is real; what does not, was noise. |
| **Find the common shape** | Separate teams asking for different specific features often share one underlying need. Solve that once instead of each request separately. |
| **Pressure-test proportionally** | Match the validation to your confidence: a low-stakes change, a throwaway prototype, or a full RFC and consultation round. |

**Accumulation is the discipline that does the most work.** It converts patience into a
filter: without acting on anything, repetition sorts genuine structural problems from
one-off frustrations. It is also the hardest to follow, because a visible problem creates
pressure to be seen responding to it.

His worked example of the common shape: multiple teams requesting different specific
personalisation features in Perfetto UI turned out to share one need — extensibility — which
was met once with macros and extension servers rather than feature by feature.

## The counter-example, which is the useful part

Maganti undercuts his own best heuristic. A caching proposal that unified several problems
turned out to be elegant rather than correct; the unified design failed, and splitting it into
two separate solutions — warm sessions and streaming export — worked.

> Being convinced by elegance can be misleading.

The instinct that detects a real common shape will just as happily manufacture a false one,
and the feeling of having found one is identical in both cases. What distinguishes them is
pressure-testing before commitment, and a willingness to abandon an idea you have already
been persuaded by.

This is the mirror of [Over-Engineering Is Solving the Wrong Problem](../engineering/architecture/over-engineering.md):
that note argues over-engineering is diligent work against wrongly-gathered requirements. The
caching example is exactly that failure caught early — a unification that would have been
"the correct answer to a problem nobody had", abandoned before it was built.

## Trust compounds

Solving a problem well buys earlier visibility into the next one: people bring you context
sooner, so the sponge collects better material. Problem-finding capability is therefore
self-reinforcing, and the first cycle is the expensive one. This is the sourcing-side view of
[Principal Engineer Influence](principal-engineer-influence.md), where influence accrues from
demonstrated judgement rather than position.

## Relationship to other notes

- [The Senior IC Role](senior-ic-role.md) — what the role is responsible for; this is how the
  work gets found before any of that begins.
- [Raising Problems Without Complaining](raising-problems-without-complaining.md) — the next
  step. Together the two make a sequence: find the problem, then raise it in a way that gets
  it acted on.
- [Over-Engineering Is Solving the Wrong Problem](../engineering/architecture/over-engineering.md) —
  the failure this practice is designed to avoid, and which the caching example illustrates
  from the inside.
- [First-Principles Thinking](first-principles-thinking.md) — "ask why repeatedly" is the same
  assumption-stripping move, applied to an incoming request rather than to an inherited
  constraint.
- [Exploring vs Exploiting in Product Discovery](../product/explore-vs-exploit.md) — sponge
  listening is exploration at individual scale: open-ended, agenda-less attention that
  surfaces problems no one has yet prioritised.
