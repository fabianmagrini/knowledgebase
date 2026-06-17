---
title: Theory of Constraints
tags: [decision-making, ci-cd, ai-engineering]
topic: concepts
status: draft
level: intermediate
related:
  - concepts/continuous-delivery.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/practices/change-absorption-capacity.md
  - leadership/managed-disruption.md
  - engineering/architecture/thinking-in-constraints.md
source: "Eliyahu M. Goldratt — The Goal (1984) and Theory of Constraints (1990)"
updated: 2026-06-17
---

# Theory of Constraints

The Theory of Constraints (ToC), introduced by Eliyahu Goldratt in *The Goal*,
rests on a single idea: **every system has exactly one constraint that limits its
throughput at any given time.** Effort spent improving anything other than the
constraint produces no gain in overall output — it only creates the illusion of
progress (more local efficiency, more inventory, more work-in-progress) while the
system's actual rate of delivering value stays flat.

The constraint is the bottleneck. An hour lost at the bottleneck is an hour lost
for the whole system; an hour saved anywhere else is a mirage.

## The five focusing steps

ToC prescribes a cycle for raising throughput:

1. **Identify** the constraint — the one resource or stage that sets the pace.
2. **Exploit** it — get the most out of the constraint without new investment
   (eliminate idle time, stop feeding it defective work, protect it from
   starvation).
3. **Subordinate** everything else to the constraint — non-bottleneck stages run
   at the constraint's pace, not their own maximum. Running them faster just piles
   up inventory in front of the bottleneck.
4. **Elevate** the constraint — if it still limits throughput, invest to increase
   its capacity (more people, automation, a structural change).
5. **Repeat** — once a constraint is broken, a new one emerges elsewhere. Go back
   to step 1, and beware inertia: yesterday's rules may now be the limit.

The deep point of step 5 is that **the constraint always moves**. Optimisation is
never finished; it relocates.

## Why local optima don't add up

A system is a chain, and a chain is only as strong as its weakest link.
Maximising the output of every link independently does not maximise the chain —
it usually makes things worse by burying the constraint in unfinished work. This
is why **work-in-progress limits** and **small batches** raise throughput: they
subordinate the fast stages to the slow one and shorten the feedback loop. It is
the same flow logic that underpins lean management and
[Continuous Delivery](continuous-delivery.md) (see the *Accelerate* lean-management
capabilities — make flow visible, limit WIP, work in small batches).

## ToC in software delivery

Software delivery is a value stream — idea → design → code → review → test →
deploy → release — and at any moment one stage is the constraint. Classic
examples: a manual QA gate, a shared staging environment, a single approver, a
flaky test suite that everyone waits on. ToC says: find that stage, and stop
optimising the others until it is fixed.

- A faster IDE or more code generation does nothing if **review** is the
  bottleneck — the extra code just queues.
- Subordinating means the team's WIP is paced by the constraint, not by how fast
  individuals can start new work.
- Elevating a review bottleneck might mean automating checks so humans review
  less — the logic behind
  [Code Review Policy](../engineering/practices/code-review-policy.md) and
  CI gates.

## The AI-native bottleneck shift

This is where ToC earns its place in an AI-assisted engineering practice. For
decades, **writing code** was treated as the constraint, and most tooling aimed
to make developers type faster. AI coding agents largely break that constraint —
and, exactly as step 5 predicts, the bottleneck moves downstream to **review,
testing, integration, and the human judgement needed to keep change safe.**

- [The AI-Augmented Engineering Team](../engineering/practices/ai-augmented-engineering-team.md)
  describes this re-balancing of where human effort is the limit.
- [Backpressure Loops for Coding Agents](../engineering/practices/agent-backpressure-loops.md)
  is, in ToC terms, subordination made explicit: agents are throttled to the pace
  the verification stage can absorb, instead of flooding it.
- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md)
  is the same constraint viewed as a property — how much change the downstream
  system can take in before quality degrades.

The practical takeaway: when you adopt AI to remove the coding constraint, **find
the new constraint before celebrating.** Throughput is set by wherever the work
now queues, not by how much code you can generate.

## Related ideas

- **Drum-buffer-rope** — Goldratt's scheduling mechanism: the constraint sets the
  drum (pace), a buffer protects it from starvation, and a rope ties the release
  of new work to the constraint's consumption. Modern WIP-limited / pull systems
  are a generalisation of this.
- **Theory of Constraints vs Lean vs Six Sigma** — Lean attacks waste, Six Sigma
  attacks variation, ToC attacks the bottleneck. They are complementary lenses on
  the same flow problem.
