---
type: note
title: Prioritisation as a Symptom
description: "The argument that prioritisation difficulty is an artefact of coupling and slowness rather than a skill to improve — and that speed and stable domain ownership are the structural substitutes."
tags: [decision-making, leadership, reading]
topic: product
status: notes
level: intermediate
related:
  - product/explore-vs-exploit.md
  - engineering/architecture/team-topologies.md
  - leadership/revised-rules-engineering-leadership.md
  - leadership/mission-to-metrics.md
  - case-studies/portkey-product-engineer-company.md
  - reading/building-software-is-learning.md
  - leadership/plan-is-not-a-strategy.md
source: "https://staysaasy.com/strategy/2026/07/16/the-best-prioritization-is-no-prioritization.html"
updated: 2026-08-03
---

# Prioritisation as a Symptom

The argument (Stay SaaSy, July 2026) is that effort spent improving prioritisation is usually
misallocated. Scoring frameworks such as RICE rest on estimates nobody can check; because you
never run the counterfactual, a prioritisation decision can never be shown to have been the
right one. Meanwhile the planning itself consumes real time and attention.

The reframe worth keeping: **prioritisation difficulty is a symptom of how the organisation is
built, not a skill to get better at.** Two structural properties determine how hard it is, and
both are more tractable than the deciding.

Opinion and experience rather than research — the strongest empirical claim offered is that
no winning companies move slowly. The original is written with some deliberate irreverence;
what follows is the argument rather than the tone.

## Substitute 1 — speed

> The better you are at moving fast, the worse you can be at prioritisation.

If shipping something is cheap, getting the order wrong is cheap too: you find out sooner and
the next thing follows quickly. Sequencing matters most when each attempt is expensive. The
recommendation is to move effort out of deciding what to build and into being able to build
it quickly.

This is the same mechanism as
[Building Software Is Learning](../reading/building-software-is-learning.md), from the other
end. Thorsten Ball argues you cannot know the right thing upfront, so compress the feedback
loop; this argues that once the loop is compressed, knowing the right thing upfront matters
less. Both make speed a substitute for foresight.

**Where the argument is weaker than it sounds.** "Cut prioritisation time and spend it on
being faster" treats speed as a dial that can simply be turned. A team that could move faster
generally would, and the article does not say where that capacity comes from. The defensible
version is narrower and still useful: **investments in delivery speed compound, while
investments in prioritisation accuracy do not** — so at the margin, speed is the better place
to put effort.

## Substitute 2 — stable domain ownership

The second is organisational. Give teams permanent ownership of a domain, and the hard
comparisons mostly stop arising:

| | The question becomes |
|---|---|
| **Without stable ownership** | "Is feature X more valuable than reliability work in a different area?" — a cross-domain comparison with no common unit |
| **With stable ownership** | "Within this domain, what matters most — support load, this feature, cost, reliability?" — a comparison between things a single team understands |

What remains genuinely cross-domain converts into a **resourcing** decision: how many people
does each domain get. That is a question about hiring and headcount rather than a debate about
relative value.

This half is well covered elsewhere and is not original here:
[Team Topologies](../engineering/architecture/team-topologies.md) (stream-aligned teams sized
by cognitive load), Larson's fourth rule in
[Revised Rules of Engineering Leadership](../leadership/revised-rules-engineering-leadership.md)
(durable teams accumulating domain context), the *exhaustive without overlap* property in
[From Mission to Metrics](../leadership/mission-to-metrics.md), and the end-to-end ownership
model in [Portkey](../case-studies/portkey-product-engineer-company.md). The contribution here
is connecting it to prioritisation cost specifically.

## It relocates the trade-off, it does not remove it

The title oversells the claim. Converting cross-domain prioritisation into headcount
allocation does not eliminate the decision — it moves it into a **slower, more consequential
forum**. Rebalancing teams is a heavier action than reordering a backlog, happens on a longer
cycle, and is harder to reverse.

That may well be an improvement: the decision becomes concrete (people and budget) rather than
speculative (estimated reach and impact), and it is made deliberately rather than re-litigated
every planning cycle. But it is a *relocation*, not a saving, and the approach depends on
domains that genuinely decompose. Where they don't — where the valuable work keeps crossing
team boundaries — the cross-domain comparisons return, and the boundaries themselves are then
the thing to fix.

## Relationship to other notes

- [Exploring vs Exploiting in Product Discovery](explore-vs-exploit.md) — the allocation
  question this note tries to dissolve; the 70-20-10 split there is a prioritisation heuristic
  of exactly the kind being argued against, and the two are worth reading together.
- [Team Topologies](../engineering/architecture/team-topologies.md) — the team-design theory
  that makes substitute 2 work, and the source of the constraint (cognitive load) that decides
  whether a domain is ownable by one team.
- [A Plan Is Not a Strategy](../leadership/plan-is-not-a-strategy.md) — a related scepticism
  about planning artefacts standing in for judgement, though Roger Martin's remedy is a
  sharper strategy rather than faster delivery.
