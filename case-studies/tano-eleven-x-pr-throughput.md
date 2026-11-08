---
type: case-study
title: Tano — One Engineer's 11× Throughput, and What It Cost
description: "The same engineer measured across three companies, which removes the inter-person confound every other throughput figure here carries — and the only account that itemises the costs: shared context lost at 30 PRs a day, thrashing above the three-project ceiling, and 'not living up to my potential with AI'."
tags: [ai-engineering, code-review, culture, observability, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/activity-metrics-obsolete.md
  - engineering/ai-native/substitution-myth-in-code-review.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/dora-ai-capabilities.md
  - engineering/ai-native/agile-in-the-age-of-ai.md
  - case-studies/intercom-ai-pr-approval.md
  - case-studies/rootly-pr-size-risk-labels.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/meta-forum-ai-native-build.md
  - case-studies/anthropic-ai-native-teams.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/practices/database-migration-strategies.md
  - reading/fintech-engineering-handbook.md
  - engineering/practices/change-absorption-capacity.md
  - case-studies/ramp-inspect-agent-platform.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/modern-engineering-values.md
  - engineering/ai-native/review-replacement.md
source: "https://newsletter.pragmaticengineer.com/p/how-software-engineering-is-changing"
updated: 2026-11-08
---

# Tano — One Engineer's 11× Throughput, and What It Cost

Neil Kakkar, framed by Gergely Orosz (November 2026). The winning essay of a $10,000 competition
from 125 submissions, and not paywalled.

**The headline is not what makes this worth recording.** "AI-native company ships much faster
with near-zero human review" is held four times already —
[OpenAI](openai-agent-first-harness.md), [Ramp](ramp-inspect-agent-platform.md),
[Meta](meta-forum-ai-native-build.md), [Rootly](rootly-pr-size-risk-labels.md). Two things are
new: the **shape of the measurement**, and the fact that it is **the only one of the five that
itemises what was given up.**

## One engineer, three companies, one measurer

> I'm shipping **11x more PRs at Tano** than at PostHog, where I shipped **2.4x** as many as I
> did at Bloomberg.

| Company | PRs/month | Context |
|---|---|---|
| **Bloomberg** | baseline (~8) | 20,000-person fintech, 3 years |
| **PostHog** | *"8 to 20 pull requests (PRs) per month"* | pre-AI startup, 4 years, 10 → 200 people |
| **Tano** | *"200+ PRs per month"* | AI-native, ~10 people, 8 months, first engineer |

**Why the shape matters.** Every other throughput figure in these notes is cross-company and
therefore confounded — and the objection is one
[Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) now carries
from Orosz himself: baseline output is **culturally set**, so *"cross-company PR comparisons are
partly measuring culture rather than AI."* A single person measuring themselves across three
employers removes the inter-person confound and isolates the organisational change.

It does not remove the others, and the note should be clear about that: PR counts measure
different-sized units in each setting, and **200+ agent-written PRs are not commensurable with 20
hand-written ones.** The author says as much — *"I couldn't write 100k+ lines of code a month by
hand"* — which concedes that the unit changed, not only the rate.

**Orosz's own framing undercuts the denominator**, and it is to his credit that he says so:

> PostHog is as 'AI-pilled' as it gets now, and output is increasing significantly. In this
> article, I treat it as a 'pre-AI baseline.'

So the 11× is measured against a snapshot that no longer exists. The comparison is historical,
not current.

## The costs, itemised — which is why this note exists

### Shared context, lost concretely

> Code reviews used to be one of my favourite things at PostHog. I had a feed of every PR coming
> in and I read them all. Reading helped me keep context of what everyone was working on, and I
> could jump in to help where needed… At Tano, we are merging about **30 PRs a day**… Having no
> time to read all PRs means **missing context across the business**.

**This is the strongest evidence in these notes for
[The Substitution Myth in Code Review](../engineering/ai-native/substitution-myth-in-code-review.md)**,
and it is strong precisely because it is not an argument against the arrangement. Allspaw
enumerates review's non-detection functions — bidirectional cognition, contextual knowledge,
calibrated attention — and the usual objection is that they are asserted rather than observed.
Here a practitioner who **chose** the trade accounts for what went with it, unprompted.

It also answers something
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
raises from the measurement side: if only **14% of 570** review comments concerned defects, then
removing review deletes the other 86% — *teaching, context, better approaches, norms*. This is
what the 86% feels like when it goes.

Code review at Tano is *"optional once you have a handle on the codebase"*, with the gate being
when *"human PR review comments go down to zero"* — three weeks for him, *"going up to eight
weeks"* depending on experience. Worth noting as the most explicit onboarding-to-autonomy
threshold in these notes: a measured condition rather than a tenure rule.

### Thrashing, from above the ceiling

*"At any one time, I'm working on 3-5 different things"* — and:

> I'm spending more time switching between tasks and getting bugs fixed, than focusing on my own
> sprint goals.

[Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) reports roughly
**three parallel agents** as comfortably manageable, and
[Anthropic's team structure](anthropic-ai-native-teams.md) reports 4–5 concurrent projects per
*team*. This is one engineer at 3–5 concurrently, reporting the failure mode the ceiling exists
to describe — *"reacting to everything"* rather than executing a plan. The word he uses is
**thrashing**, borrowed from scheduling: a system spending more time switching than working.

### The psychological cost, stated plainly

> Sometimes I do feel that I'm not living up to my potential with AI; it's here, waiting to be
> used, waiting to build more things with, waiting for direction, and I'm *sleeping*? **The sense
> of not doing enough while working harder than ever feels overwhelming.**

His guardrails are mundane and the better for it: leave the laptop at the office, stop at 6pm,
prioritise personal projects explicitly.

**Hold this directly against [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md)**,
where burnout and friction *"basically stayed at zero"* across ~5,000 respondents. These notes
should carry both without resolving them: a survey mean and one person's account answer different
questions, and the mean can be flat while the tail is not. It is also the pressure
`agile-in-the-age-of-ai` predicts when it insists sustainable pace is the thing that does not
change — here as a lived report rather than a principle.

## Tokenmaxxing, with a real budget

> **Tokenmaxxing** is the idea of using as many AI tokens as possible, often with no regard for
> the actual productivity gains of doing it.

A useful name for a failure mode the repo has the conditions for and no word for. Against it,
Tano's actual constraint: *"there is no 'infinite' AI budget. Everyone has one 20x Claude Max plan
subscription, and that's it"* — and the counterfactual that makes it concrete, *"if we were paying
API rates, my usage would come to **$8,000+ per month**."*

That figure sits **above the top of the measured range** folded into `activity-metrics-obsolete`
(**$150–$3,000** per developer per month, ~20× spread), which makes it the highest per-engineer
consumption recorded here — and it is consumption at subscription pricing, not spend. The
seat-versus-API gap is the interesting part: a flat subscription is a *cap*, and the cap is doing
the budget governance that the $500M-spend cautionary case in
[the AI gateway note](../engineering/ai-native/ai-gateway-control-plane.md) lacked entirely.

## Design commoditisation

Nothing in these notes covers this, and it is a real consequence of generation getting cheap:

> With AI, I observe early-stage startups discounting design work… AI designs are very similar to
> a lot of other designs out there… At Tano, it's what we've ended up with, and we're taking steps
> to figure out what our brand should look like.

Generated interfaces converge because the generators share training data, so **differentiation
becomes a deliberate cost rather than a by-product**. That is the same shape as *taste as the
gating function* in [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md)
— cheap generation makes selection the scarce skill — pointed at brand rather than code.

## The two failures, which are specific enough to learn from

| Failure | What happened |
|---|---|
| **Currency handling** | *"the agent decided to take these minor units, parse them as floats, and multiply by 100"* — **without checking existing utilities** |
| **Database migration** | *"a blocking migration that blocked writes, and our ingestion pipeline stopped saving new posts"* |

The first is [Fintech Engineering Handbook](../reading/fintech-engineering-handbook.md)'s
money-representation discipline broken not by ignorance of the rule but by **not consulting the
codebase** — the agent reimplemented what already existed, which is a context failure rather than
a reasoning one. The second is
[Database Migration Strategies](../engineering/practices/database-migration-strategies.md)
exactly: the stateful change is the hardest part of continuous delivery, and a blocking migration
on a large table is its canonical instance.

Their stated posture: *"We're willing to make the trade-off between automated agent review &
moving quickly and fixing things as they break… because we can do forward fixes on these issues
quickly."* An explicit, owned trade — which is the honest version of the configuration
[Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) measures at
**+31.3% unreviewed merges and +242% incidents** when it arrives *by default* rather than by
decision.

## The figure to discount

> The revert rate is **6x lower** at Tano **because we fix things forward most of the time, rather
> than revert.**

**The causal clause is in the sentence, and it invalidates the metric.** A lower revert rate
produced by a policy of not reverting measures the policy, not the quality of the changes.
[Intercom's AI PR approval](intercom-ai-pr-approval.md) already holds the general lesson — its
headline revert comparison *"does not demonstrate what it is used to suggest"* because the
populations differ by selection — and this is a cleaner instance, since the confound is stated
rather than hidden. Forward-fixing is a legitimate strategy; it is not evidence about defect
rates.

No baseline period or method is given for the 6×, either.

## What bounds this account

- **~10 people, first engineer, eight months.** The smallest organisation in any of these
  accounts by an order of magnitude. Near-zero human review at ten people with one codebase is a
  different proposition from the same policy at Bloomberg's 20,000.
- **Orosz's generalisability caveat**, which is the right one: *"I wonder if this new generation of
  'AI-native' startups have this temporary advantage of iterating much faster than companies that
  are only a few years older than they are… The last thing you want to do is to break your
  business by being careless!"*
- **Self-reported throughout**, from a competition entry — the incentive is to make the shift
  vivid. The costs section is what makes it credible, since nothing in the prize structure
  rewarded including it.
- **No quality measurement.** Volume, revert rate (discounted above) and time-to-merge are all
  process metrics. Nothing on defect escape, rework, or
  [the verified-outcome definition](meta-forum-ai-native-build.md) Meta uses — which is what
  would turn 11× into evidence rather than a count.
- **The 11× is a PR count**, the proxy `activity-metrics-obsolete` exists to reject. Carried as a
  description of a changed working life rather than a productivity measurement, which is roughly
  how the author presents it.

## Relationship to other notes

- [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) — the
  culture-sets-the-baseline confound this measurement design sidesteps, and the spend range this
  exceeds.
- [The Substitution Myth in Code Review](../engineering/ai-native/substitution-myth-in-code-review.md)
  and [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
  — review's non-detection functions, reported as a felt loss by someone who chose to give them up.
- [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md) — burnout flat across ~5,000
  respondents against one engineer's "not living up to my potential"; hold both.
- [Agile in the Age of AI](../engineering/ai-native/agile-in-the-age-of-ai.md) — the ~3-agent
  ceiling and sustainable pace, reported from above the line.
- [Intercom's AI PR Approval](intercom-ai-pr-approval.md) — why revert-rate comparisons mislead;
  here the confound is stated in the same sentence as the claim.
- [Meta's Forum](meta-forum-ai-native-build.md) and
  [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — the same arrangement at larger
  organisations, with definitions of done this account lacks.
- [Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) — the engineered
  version of near-zero review, chosen deliberately, against the accidental version with its +242%.
- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) — 30 PRs a
  day into a ten-person company is the absorption question posed at a different scale.
