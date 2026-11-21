---
type: note
title: Predictability vs Outcomes
description: "Cagan retracting his own outcomes-versus-output framing — outputs are a means, so opposing them to outcomes is a category error — and naming predictability as the real competitor, with a structural reason: a team that cannot choose what to build has nothing but predictability left to promise."
tags: [decision-making, leadership, culture, reading]
topic: product
status: notes
level: intermediate
related:
  - leadership/start-with-why.md
  - product/prioritisation-as-a-symptom.md
  - product/explore-vs-exploit.md
  - product/modelling-business-impact.md
  - product/four-abstraction-levels-of-refinement.md
  - engineering/architecture/team-topologies.md
  - leadership/scaling-engineering-org.md
  - leadership/managed-disruption.md
  - leadership/plan-is-not-a-strategy.md
  - leadership/mission-to-metrics.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - case-studies/tano-eleven-x-pr-throughput.md
  - engineering/practices/regulated-service-release-process.md
  - leadership/protecting-mavericks.md
  - leadership/landing-the-plane.md
  - leadership/new-leader-credibility.md
  - engineering/architecture/over-engineering.md
  - engineering/practices/database-migration-strategies.md
  - engineering/ai-native/dora-ai-capabilities.md
  - concepts/positive-friction.md
source: "https://www.svpg.com/predictability-vs-outcomes/"
updated: 2026-11-21
---

# Predictability vs Outcomes

Marty Cagan (SVPG, October 2026) correcting a framing he did more than anyone to popularise.

> we can't achieve outcomes without output, so outcomes *versus* output is not really a
> trade-off… Increasingly I have come to see the root cause as the desire for
> **predictability**. The real trade-off is the relative priority of outcomes versus
> predictability.

**This matters here because the repo asserts the corrected framing in three places and has never
examined it.** [Start With Why](../leadership/start-with-why.md) states *"outcomes over outputs"*
as a principle; [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md)
warns against *"letting tool speed justify more output rather than better outcomes"*; and
[The AI-Augmented Engineering Team](../engineering/ai-native/ai-augmented-engineering-team.md)
says teams should value *"outcomes over output"*.

The correction is a real one rather than a quibble. **Output is a *means*, so setting it against
outcomes is a category error** — nobody achieves an outcome without shipping something.
Predictability is a genuine competitor because it is a thing an organisation can choose
*instead*: you can have a reliable forecast of what will ship, or a decent chance of it working,
and optimising hard for the first costs you the second.

Henrik Kniberg's formulation, which these notes did not hold, is the compact version:

> **100% predictability = 0% innovation.**

That is something the repo argues at length elsewhere —
[Exploring vs Exploiting](explore-vs-exploit.md)'s local-maxima risk from over-exploiting,
[Protecting Mavericks](../leadership/protecting-mavericks.md), the deliberate-disruption argument
in [Managed Disruption](../leadership/managed-disruption.md) — without a line that states it in
seven words.

> **Provenance.** A short conceptual essay with **no evidence, data or case examples**. Cagan is
> a founder/partner at SVPG, which sells the alternative operating model and two books on it
> (*INSPIRED*, *TRANSFORMED*), so the piece argues for the thing he teaches. The self-correction
> is the credible part: it costs him a slogan he owns.

## The mechanism is structural, not attitudinal

The strongest passage, and the reason the reframe is more than vocabulary:

> most companies are implicitly making a different choice. To them, predictability is the clear
> priority, and outcomes are a hoped-for consequence of shipping what was promised. Especially in
> organizations still running the project model, where their feature teams are set up **"to serve
> the business,"** and so they aren't in a position to take responsibility for outcomes.

**A team that cannot choose what to build cannot be accountable for whether it worked** — so
predictability is the only thing it has left to promise. Read that way, "we optimise for
predictability" is not a cultural failing to be exhorted away; it is the rational response to an
accountability structure, and the structure is what has to change.

That is [Prioritisation as a Symptom](prioritisation-as-a-symptom.md)'s argument in another
register: difficulty is an artefact of how the organisation is built rather than a skill to
improve, and the remedy there — **stable domain ownership**, so comparisons happen inside a team
that understands them — is exactly the condition a team needs before outcomes can be its
responsibility. It is also the inverse-Conway logic in
[Team Topologies](../engineering/architecture/team-topologies.md): a team aligned to a stream
can own an outcome; a team aligned to a request queue can only own delivery.

And it sharpens a constraint already recorded.
[Scaling an Engineering Organisation](../leadership/scaling-engineering-org.md) carries JFrog's
demand to optimise for **speed *and* predictability** at once. Cagan's framing says what that
costs: whatever was going to come from discovery.

## He concedes the case against himself

Worth carrying, because it keeps this a *priority* argument rather than an anti-planning one:

> Predictability is not inherently a bad thing. In fact, there are certain situations where real
> predictability is absolutely necessary, and we've long had techniques for managing those cases.

The repo holds those situations concretely —
[regulated service release](../engineering/practices/regulated-service-release-process.md),
[database migration strategies](../engineering/practices/database-migration-strategies.md) where
a stateful change cannot simply be retried, and the committed delivery endgame in
[Landing the Plane](../leadership/landing-the-plane.md). **He names no technique**, which is the
piece's largest gap given he asserts the techniques exist.

The honest position is that predictability is a **constraint satisfied where required**, not a
default to maximise — the same shape as
[Over-Engineering Is Solving the Wrong Problem](../engineering/architecture/over-engineering.md):
structure justified by constraints rather than adopted on principle.

## The AI connection he names and does not develop

> We have never had the problem of abundant output yet scarce outcomes more than we do today.

He points at it and moves on, and it is the most useful thing in the piece for these notes,
because **the reframe explains why weeks of accumulated AI figures are unsatisfying: they are all
output measures.**

| Figure held here | What it measures |
|---|---|
| [Tano's 11× PRs/month](../case-studies/tano-eleven-x-pr-throughput.md) | output, with **no quality measurement at all** |
| Ramp's 75%, Rootly's 80%, OpenAI's ~3.5 PRs/engineer/day | output, conditioned on nothing |
| GitHub's fivefold PR growth | output, platform-wide |
| [DORA's rising delivery instability](../engineering/ai-native/dora-ai-capabilities.md) | the cost side, and the only one pointing at consequences |

[Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) already rejects
these proxies and proposes six diagnostics, and
[Modelling Software's Business Impact](modelling-business-impact.md) supplies the value side with
NPV categories. **What Cagan adds is why the output measures feel beside the point rather than
merely crude**: output was never the variable in tension, so measuring more of it cannot settle
the question. Meta's *"verified, production-ready outcomes"* is the closest thing in these notes
to a measure that resists the complaint, and even that conditions on *shipping correctly* rather
than on *the change having worked*.

There is a second-order version worth naming, which he does not. If cheap generation makes output
abundant, **predictability gets cheaper too** — you can more credibly promise to ship the agreed
list — so the pull toward the predictability pole strengthens exactly when discovery would pay
most. That is the mechanism behind
[Modelling Business Impact](modelling-business-impact.md)'s observation that the constraint moves
to **customer absorption capacity** once engineering stops being the bottleneck.

## Where the argument is weakest

**The SAFe passage.**

> That is the only explanation I have for the many companies that adopted SAFe over the years. It
> is a model that very clearly is optimized for predictability, and makes no serious attempt at
> achieving outcomes.

*"The only explanation I have"* is a rhetorical move rather than an analysis, and *"makes no
serious attempt"* is asserted about a framework he opposes commercially. **The structural
argument above stands entirely without it** — if feature teams set up to serve the business
cannot own outcomes, that holds regardless of which scaling framework they run. Recorded as
attributed opinion.

He also invokes Steve Jobs's *Lost Interview* on the *"disease"* of believing a great idea is 90%
of the work, and the Agile Manifesto as having tried to capture the same point. Both are
illustrative rather than evidential.

## What the piece does not cover

- **No evidence of any kind** — no data, no case, no measurement.
- **No technique for the cases where predictability is genuinely required**, despite asserting
  that such techniques exist and are long-established. That is the actionable half, and it is
  missing.
- **Nothing on who is asking.** Predictability is usually demanded by the people funding the
  work, and an argument addressed to product leaders does not say what to do when the party
  wanting a forecast holds the budget. [Modelling Business Impact](modelling-business-impact.md)
  is the better guide there: it works the finance-function route explicitly.
- **No account of trust as the real currency.** A team with a track record of outcomes gets
  granted latitude; one without it gets asked for dates. The piece treats the choice as made at
  the top rather than earned, and
  [New Leader Credibility](../leadership/new-leader-credibility.md) suggests the sequencing runs
  the other way.

## Relationship to other notes

- [Start With Why](../leadership/start-with-why.md) — holds *"outcomes over outputs"* as a
  principle; this is the author of that framing saying it names the wrong trade-off.
- [Prioritisation as a Symptom](prioritisation-as-a-symptom.md) — difficulty as structural rather
  than skill-based, and stable domain ownership as the precondition for owning outcomes at all.
- [Exploring vs Exploiting](explore-vs-exploit.md) — Kniberg's line is the compressed form of its
  over-exploitation risk.
- [Team Topologies](../engineering/architecture/team-topologies.md) — stream-aligned teams can own
  outcomes; teams aligned to a request queue can only own delivery.
- [Scaling an Engineering Organisation](../leadership/scaling-engineering-org.md) — JFrog's
  speed-*and*-predictability demand, now with its cost named.
- [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) and
  [Tano](../case-studies/tano-eleven-x-pr-throughput.md) — the output measures this reframe
  explains the unsatisfactoriness of.
- [Modelling Software's Business Impact](modelling-business-impact.md) — the outcome side with
  actual machinery, and the better answer on how to talk to whoever is funding the work.
- [A Plan Is Not a Strategy](../leadership/plan-is-not-a-strategy.md) — Roger Martin on planning
  artefacts standing in for judgement; predictability is what the plan is really buying.
- [Regulated Service Release Process](../engineering/practices/regulated-service-release-process.md)
  — a case where predictability is the requirement, which his concession points at and does not
  address.
