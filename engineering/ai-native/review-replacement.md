---
type: note
title: Replacing Code Review With Upstream Verification
description: "The far end of the review spectrum — review declared obsolete rather than tiered or partly automated — plus the same Faros dataset these notes already hold, read to the opposite conclusion."
tags: [ai-engineering, code-review, testing, governance, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/agentic-code-review.md
  - case-studies/intercom-ai-pr-approval.md
  - case-studies/rewind-ai-pr-approval.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/tdd-in-the-agent-loop.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - concepts/progressive-delivery.md
  - concepts/control-and-complexity.md
  - engineering/ai-native/substitution-myth-in-code-review.md
  - engineering/ai-native/accountability-for-unread-code.md
  - reading/state-of-tech-2026.md
  - engineering/ai-native/dora-ai-capabilities.md
  - case-studies/meta-forum-ai-native-build.md
  - case-studies/tano-eleven-x-pr-throughput.md
  - engineering/practices/database-migration-strategies.md
  - reading/fintech-engineering-handbook.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/architecture/reversibility-decays.md
  - case-studies/rootly-pr-size-risk-labels.md
source: "https://www.latent.space/p/reviews-dead; https://swizec.com/blog/how-do-we-auto-approve-and-merge-60p-of-prs"
updated: 2026-11-08
---

# Replacing Code Review With Upstream Verification

Ankit Jain (March 2026, guest essay on Latent.Space) argues that manual code review cannot
scale with AI-generated output and should be replaced by verification moved upstream to
specifications.

> Human-written code died in 2025. Code reviews will die in 2026.

**Provenance worth noting:** Jain is CEO of Aviator, which sells merge-queue and code-review
tooling. The essay argues against the category his company operates in — either unusually
candid or a repositioning, and either way not a disinterested vantage point.

## The same data, the opposite conclusion

The most useful thing here is not the argument but the citation. These notes already carry
**Faros** data through [Dark Factories Examined](dark-factories-examined.md):

| Source | Faros figures cited | Reading |
|---|---|---|
| Kacharov, via [Dark Factories Examined](dark-factories-examined.md) | 22,000 developers: **+31.3%** unreviewed merges, **+242%** incidents, agents opening under 1% of PRs | Review has quietly collapsed and nothing replaced it — **this is the alarm** |
| Jain, here | 10,000+ developers across 1,255 teams: **98%** more PRs merged, **91%** longer review time | Review is the bottleneck throttling delivery — **this is the thing to remove** |

Same dataset, same observed phenomenon, opposite conclusions. One treats the failing guardrail
as the problem to fix; the other treats the guardrail as the problem itself.

The disagreement is really about a prior: whether the 242% incident rise is *the cost of losing
review* or *the cost of not having replaced it properly yet*. Kacharov's evidence is stronger
on that point — those incidents occurred in teams that stopped reviewing without building
anything in its place, which is his **accidental** dark factory rather than an argued one.

Jain's supporting argument is fair, though: review was never the real safety net. Teams have
relied on **feature flags and rollbacks** for years, which is
[progressive delivery](../../concepts/progressive-delivery.md) doing work that review was
credited with.

### Two further datasets

Both from Gergely Orosz's [*What is happening with code reviews?*](https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews)
(September 2026; paywalled past its third section), and both broadening the evidence beyond the
single Faros dataset above.

**Platform-wide.** GitHub reports "the number of PRs opened has increased fivefold" across three
years, with "PRs and commits nearly doubled *just* in that period alone" — the acceleration
concentrated in the most recent stretch. Cited from GitHub's own August 17 outage postmortem,
which is odd provenance but not a vendor's selected sample: it is platform-load context in an
incident writeup. This is the broadest population these notes hold on the volume question.

**One team, with a confound worth naming.** The Duckbill Group (a 15-person startup) reports:

| Measure | Reported |
|---|---|
| PRs merged | 353 → 684 (80/wk → 154/wk, **+94%**) |
| Merged within 1h | 28% → 45% |
| Merged within 24h | 76% → 80% |
| Human-reviewed, median merge time | **26h** |
| No human review, median merge time | **1h** |

**The 26h-versus-1h gap is not the cost of human review**, and should not be read that way.
Duckbill route changes to human review by risk category, so the two populations are *selected to
differ* — the reviewed set is the set someone judged risky, and the article does not state that
the groups are comparable in size or risk. The defensible reading is narrower and still useful:
**once you triage, the untriaged majority merges quickly**, which is a claim about what fraction
of changes are genuinely low-risk rather than about review latency. It supports risk tiering (as
in [Rootly](../../case-studies/rootly-pr-size-risk-labels.md)), not review removal.

## The five replacement layers

| Layer | Status in these notes |
|---|---|
| **Multiple agent options ranked deterministically** | **New** — best-of-N generation with a deterministic picker |
| **Deterministic guardrails** — tests, type checks, contract verification | Held: [Linters Over AI Review](linters-over-ai-review.md), [Enforced Architecture Rules](../architecture/enforced-architecture-rules.md) |
| **Human-authored acceptance criteria** (BDD) | Held: [Spec-Driven Development](spec-driven-development.md), [Comprehension as an Architectural Characteristic](../architecture/comprehension-as-architecture.md) |
| **Permission systems** bounding agent scope | Held: [AI Gateway Control Plane](ai-gateway-control-plane.md), [Securing AI Agent Skills](../security/agent-skill-security.md) |
| **Adversarial verification** — separate coding and verifying agents | Held: [Harness Design Experiments](harness-design-experiments.md), [Loop-Driven Development](loop-driven-development.md) |

**Best-of-N ranking is the genuinely new one.** Generate several candidate solutions in
parallel and let a deterministic ranker choose, rather than iterating a single candidate. That
differs from the evaluator–optimizer pattern in
[Building Effective Agents](../../reading/building-effective-agents.md), which refines one line
of work — here the selection pressure comes from *comparison between candidates*, which needs a
ranking function good enough to order them. Whether such a ranker exists for most work is not
addressed.

He frames the stack as a **Swiss-cheese model**: no layer is complete, but the holes do not
line up. That is a useful name for something
[Securing AI Agent Skills](../security/agent-skill-security.md) argues without naming — every
control has a category it structurally cannot see, so the answer is overlap rather than picking
the best single control.

## Where the spectrum now sits

These notes have accumulated a full range of positions on one question:

| Position | Source |
|---|---|
| Only human approvals count toward merge | [Code Review Policy](../practices/code-review-policy.md) |
| Tiered by risk; a human owns the merge | [Agentic Code Review](agentic-code-review.md) |
| ~19% auto-approved, accountability moves to the author | [Intercom](../../case-studies/intercom-ai-pr-approval.md) |
| ~40% auto-approved, under compliance controls | [Rewind](../../case-studies/rewind-ai-pr-approval.md) |
| ~16% achieved, **60% targeted**, review pushed both upstream and downstream | [Swizec Teller](https://swizec.com/blog/how-do-we-auto-approve-and-merge-60p-of-prs) (November 2026), below |
| **Review replaced outright by upstream verification** | this note |

Better read as a spectrum than a debate. The practical question for any team is where on it
they sit and why — and the observation worth carrying is that every middle position retains
something both endpoints lack: **a named human accountable for a specific change.**

### The fourth data point, and the direction it adds

Teller — already a source here for
[custom linters over AI review](linters-over-ai-review.md), from a team handling 2,900 PRs and
10 reviews a day — describes pushing further along the same axis. **Read the figure carefully**:
*"Getting to ~16% auto-approved and merged PRs helped but it's not enough. How can we do 60%?"*
The 19% and 40% above are reported current states; **this is 16% achieved and 60% aspired to**,
and belongs in the table as a direction rather than a measurement. No company is named and no
time period is given for either number.

**What it adds is a third stage the five layers above do not have:**

> 1. **Before implementation** Engineers + Stakeholders review architecture, constraints, and
>    product direction
> 2. **During implementation** Agents + automated checks review correctness, contracts,
>    conventions, and safety
> 3. **After implementation** Engineers + users review actual behavior, UX, and usefulness

Every one of this note's five replacement layers is **upstream** — best-of-N ranking,
deterministic guardrails, acceptance criteria, permissions, adversarial verification. Stage 3
moves review **downstream into observed behaviour with users**, which is a position these notes
did not hold. Paired with Laycock's shift-left in
[The Substitution Myth in Code Review](substitution-myth-in-code-review.md), the shape becomes
clearer than either alone: **judgement moves both left and right, and the code-level review in
the middle is what gets squeezed out.** Whether stage 3 can carry the weight is the open
question — behaviour review catches what users notice, which is a different and smaller set than
what a reviewer reading a diff would catch.

**The exclusion list is the most portable line in the piece:**

> It won't merge anything that touches **migrations, public interfaces, or finance**.

Three categories named by *what they can damage* rather than by diff size or a risk score — and
each is independently evidenced in these notes. Migrations:
[Tano's blocking migration](../../case-studies/tano-eleven-x-pr-throughput.md) that stopped the
ingestion pipeline writing, and
[Database Migration Strategies](../practices/database-migration-strategies.md) on why stateful
change is the hardest part of delivery. Finance: Tano's agent parsing currency minor units as
floats, and [the fintech handbook](../../reading/fintech-engineering-handbook.md)'s *"no invented
data"*. Public interfaces: [contract testing](../practices/api-contract-functional-testing.md)
and [Reversibility Decays](../architecture/reversibility-decays.md), where an exported surface is
the thing whose exit cost only rises. **A three-item denylist that matches where this repo's own
recorded failures actually happened** is worth more than a scoring rubric nobody can calibrate.

Risk itself is tagged *"by bugbot or a human"* — the same mechanism as
[Rootly's risk labels](../../case-studies/rootly-pr-size-risk-labels.md), with no rubric given.

Two smaller things. His name for review's residual purpose is good: *"Code review then mostly
becomes about finding **desire paths in our architecture** so we can build tools for common
problems"* — turning repeated review findings into linters, which continues his earlier argument
and is the feedback loop `linters-over-ai-review` describes without naming. And his stated limit
is the right one: *"I don't think 100% is feasible. Some things are high risk, need coordinated
deploys, or just more feedback before they're ready"*, with mentoring junior engineers as the
other case requiring humans.

> **A collision worth not conflating.** He uses **"meat proxying"** to mean *himself* pasting a
> PR link into Claude and saying "fix this" — a human as manual transport for work that should be
> automated. [Accountability for Unread Code](accountability-for-unread-code.md) already carries
> the phrase from Steve Huynh in a different sense: *"managers being meat proxies for a
> conversation between two prompts"*, a human relaying between models while contributing no
> judgement. Same words, opposite complaints — one wants the human removed from the pipe, the
> other objects to the human having become one.

## The tension in his own argument

Jain concedes that LLMs are **"not great at following commands"** and **"unreliable at
self-verification"** — then proposes BDD acceptance criteria (layer 3) and agent-based
adversarial verification (layer 5) as the replacement for review.

Both inherit the weakness he has just named. If a model does not follow commands reliably, a
specification is a command it may not follow; if it is unreliable at self-verification, a
verifying agent is a model verifying a model. Commenters raised the difficulty of writing
specifications precisely enough, and
[TDD Inside the Agent Loop](tdd-in-the-agent-loop.md) points the same way — a practice whose
value depends on a human performing it does not necessarily survive being handed to an agent.

The layers that *don't* inherit the problem are the deterministic ones — guardrails and
permissions — which is the same conclusion [Linters Over AI Review](linters-over-ai-review.md)
reaches from cost and
[Enforced Architecture Rules](../architecture/enforced-architecture-rules.md) from correctness.
Read charitably, the essay is strongest where it is least novel.

## Relationship to other notes

- [Dark Factories Examined](dark-factories-examined.md) — the same Faros data read as evidence
  of collapse rather than of bottleneck; the pair is worth more than either alone.
- [Agentic Code Review](agentic-code-review.md) — the tiered middle position this argues past.
- [Linters Over AI Review](linters-over-ai-review.md) — agrees on moving checks upstream and
  making them deterministic, without concluding that review dies.
- [Spec-Driven Development](spec-driven-development.md) — the upstream artefact this proposal
  depends on, and where the cost of producing one is discussed.
