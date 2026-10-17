---
type: case-study
title: Anthropic's Scion — Source Control at Agent Scale
description: "Replacing Git when merged changes went 2,500 to 30,000 a day in four months: the inversion where distribution became the liability because every client was already online, changesets over packfiles, and the merge-queue serialisation they gave up to get throughput."
tags: [ai-engineering, architecture, ci-cd, system-design, git, reading]
topic: case-studies
status: notes
level: advanced
related:
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/trunk-based-development.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - case-studies/linear-ci-rework.md
  - case-studies/anthropic-ai-native-teams.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - case-studies/cursor-agent-swarm-economics.md
  - case-studies/github-copilot-rust-migration.md
  - tools/git.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - engineering/practices/release-confidence.md
  - languages-and-frameworks/go-agentic-language.md
source: "https://www.anthropic.com/engineering/redesigning-source-control"
updated: 2026-10-18
---

# Anthropic's Scion — Source Control at Agent Scale

Anthropic's engineering blog (October 2026; Nick G., S.G., R.K., Dan C., Garrett H., Ben L.,
Colin M., Joe P.) on building **Scion**, a version control system to replace Git internally,
plus **Antique**, its accompanying code review tool.

> **Declaring an interest.** These notes are maintained with Claude, which is Anthropic's
> product. Worse than the usual conflict: Claude is both the **cause** of the problem described
> and the **tool credited with solving it**, so the piece is self-interested in two directions
> at once. Every figure is self-reported and, unlike
> [GitHub's Rust migration numbers](github-copilot-rust-migration.md) — which could in principle
> be checked against a repository — **none of this is independently verifiable**. Scion is
> internal and unreleased.

## The number that forced it

> In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we
> merged over 30,000 per day.

A **12× rise in four months**, and the hardest change-volume figure in these notes. The scale
that follows from it:

| | |
|---|---|
| Main-branch history | almost **100 GB** |
| Working copy | over **25 GB** *compressed* |
| CI checkouts | *"on the order of 25 million code checkouts per day"* |
| Naive fetch cost | *"over 600 PB of git traffic per day"* |

[Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) frames the
absorption ceiling as a property of the codebase, the tests and the team. This is the same
ceiling reached at a layer that note does not consider: **the version control system itself**.
Worth adding to the list of things that have to scale when code production gets cheap, because
it is the one nobody budgets for.

It is also the same 30,000-a-day figure that
[Cursor's agent swarm economics](cursor-agent-swarm-economics.md) treats as an **anti-metric** —
commit volume as evidence of churn rather than progress. Both readings are available here, and
the piece only takes one of them. Read side by side, the useful observation is that whatever
commit volume means about productivity, it is unambiguously **infrastructure load**.

## The inversion: distribution became the liability

The sharpest idea in the piece, and the part that generalises:

> nearly all of our clients were agents and jobs that are online by definition. The properties
> that make git excellent for distributed, offline work were actively undermining our ability to
> scale.

Git's defining virtue — every clone a complete, independent replica — is a cost when no client
ever needs independence. They record trying the conventional escapes first, which is what makes
the argument credible rather than merely assertive: *"Git offers tools for working with a slice
of a repository, such as shallow clones, sparse checkouts, and promisor remotes… We've used all
of them — at our peak, we operated several hundred internal git mirrors to deal with the
load."* The failure mode was drift and fragility: *"Seeds fell further from the tip of main
between refreshes, and it took more and more care to keep operations that depend on history,
like diff and blame, working on partial clones."*

This is a design choice made for human clients being re-evaluated for machine ones, which is the
same move as [Go as an Agentic Language](../languages-and-frameworks/go-agentic-language.md)
makes about build times — any per-iteration property a human absorbs a few times an hour
compounds at machine frequency. Here the property is not slow, it is *redundant*, and the
redundancy is what costs 600 PB a day.

Their six design principles follow directly from the client population:

- **Clients are always online**
- **Client-server asymmetry**
- **Comprehensive source control service powers novel applications**
- **Everything must be horizontally scalable**
- **Commits must be cheap, incremental, lock-free**
- **Working copy is optional, sparse by design**

## Changesets instead of packfiles

> A changeset stores most of what you'd expect from a commit in git. But where a git commit
> stores a pointer to the tree, a changeset stores a list of the files that changed relative to
> its first parent, along with content-addressed pointers to the compressed file contents.

The consequence is the point: *"This structure lets us accept changesets with very high
throughput because there are no packfiles to accept, no locking or cross-server
coordination."* Write cost scales with **the size of the change**, not the size of the
repository. Derived structures — blame, path history, skip lists — are computed recursively from
the changeset log rather than stored, and the log itself is a write-ahead log.

Serving is three tiers, each absorbing nearly everything:

> the client talks over a socket to a daemon, scion-daemon, that stores objects for the whole
> node. Each daemon starts from a periodically refreshed snapshot, then talks only to the tree
> and blob cache servers in its region, called scion-cache. When a cache is missing an object,
> it asks the authoritative scion-servers.

With *"a cache hit rate of over 99%"* at **every** tier. Checkout is a recursive request for the
trees and blobs a client wants, rather than Git's negotiation over what the client already has —
which is the client-server asymmetry made concrete: the server knows, so the client does not
have to tell it.

Prior art is credited rather than claimed: Google's **Piper**, Meta's **Sapling** and its
**Mononoke** server, and the **Bonsai** data model.

## The trade-off they name, which is the most useful part

> We haven't been able to effectively replicate the industry standard of a global repository
> lock on the merge queue, so instead, we've invested in post-merge and pre-deploy automated
> testing. This does mean that concurrent changes can conflict.

They **gave up pre-merge serialisation and moved verification downstream**, and they say what it
costs. That is worth holding carefully against
[Trunk-Based Development](../engineering/practices/trunk-based-development.md), which asserts
"small batches, fast feedback, no merge queues" as a *principle*:

| | Why no merge queue |
|---|---|
| **Trunk-based development** | A chosen model — small batches make serialisation unnecessary |
| **Scion** | A **capacity constraint** — serialisation was unachievable at 30,000 merges a day |

Arriving at the same architecture by necessity rather than by design is not the same as choosing
it, because the batches here are not small. The cost lands as conflicts between concurrent
changes, and the compensating control is testing *after* the fact — which is
[release confidence](../engineering/practices/release-confidence.md) carrying load that a merge
queue would otherwise carry. Anyone reading this as validation of a queue-free trunk should note
that Anthropic would apparently have preferred the lock.

## What it cost, and what it bought

Claimed results, all self-reported:

- *"Our Scion infrastructure footprint is now 200x smaller than our previous git mirroring
  infrastructure in terms of CPU and memory requirements."*
- *"CI and research jobs check out code two orders of magnitude faster (in seconds rather than
  minutes)."*
- *"CI alone realized a 25% CPU capacity win."*

That last figure is directly comparable to [Linear's CI rework](linear-ci-rework.md), where
setup overhead was found to cap parallelism — checkout *is* setup overhead, and this is the same
bottleneck attacked at the source-control layer instead of the pipeline layer.

**The honest scope limit**, which is what stops the piece reading as a template:

> Scion is by no means a suitable replacement for git for general use.

> The concepts we've outlined here really only make sense for truly enormous monorepos, with
> either tens of thousands of engineers or swarms of agents prolifically writing code.

And the sentence carrying the real price: *"it requires its own code review, code search, and
CI."* **Leaving Git means leaving its ecosystem.** This is a three-system commitment at minimum
— hence Antique, built alongside Scion by the same people. Any organisation reading the 200×
figure should read that clause next to it.

## The claims to hold at arm's length

**Seven people, five months, 10× growth.** *"A team of seven people built both Scion and Antique
(our code review tool)"* and *"fully migrated to them in five months"*, *"while the volume of
code merged per day increased by 10x."* Extraordinary if accurate, and the counterfactual nobody
ran — the same framing problem as the Copilot migration's "a whole team a year or two".

**Claude's role in building it.** *"We started building Scion around the same time as Claude
Mythos Preview and Claude Tag became available internally. Both of these releases simultaneously
amplified the need for Scion and meaningfully accelerated how quickly we could build it."* The
concrete example is a rewrite of the ingestion pipeline: *"We asked it to rewrite the whole
thing, and with no further instructions, it produced a version that consumed 20x less memory and
was 4x faster, while preserving all of the implicit invariants."*

And then: *"All of the engineers who worked on this system would now rate Claude as better at
writing code than them."*

That last one is an **unmeasured self-report by employees about their employer's product**, and
it should be read as a statement of sentiment rather than a finding. It is also in tension with
the rest of the repo's better evidence:
[Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md) records
agent-productivity effects scattering from **−19% to +40.5%** across studies, and
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
holds the 14%-of-570 figure on how little agent output is actually read. A single team's
confidence in a tool is not evidence about the tool; it is evidence about the team's experience
of it, which is worth having and worth labelling.

## What the piece does not cover

- **No cutover mechanics.** A five-month replacement of the system every engineer and every
  agent depends on, with nothing on how they switched, what ran in parallel, how they verified
  equivalence, or whether they could have gone back. The most striking absence given the
  blast radius.
- **No incidents.** Not one failure, regression or outage across the migration — which is either
  remarkable or unreported, and the piece gives no way to tell which.
- **No cost figures.** The 200× footprint reduction is relative; no absolute spend, and nothing
  on what seven engineers for five months plus two new systems cost against it.
- **No comparison against the prior art it cites.** Piper, Sapling and Mononoke are credited as
  influences, but there is no account of why an existing system — Sapling is open source — was
  not adopted or extended instead. For a reader deciding what to do, that is the missing section.
- **Nothing on the social consequences.** A VCS without Git's ecosystem means no familiar
  tooling, no transferable skills, and onboarding against an internal system. Not mentioned.

## Relationship to other notes

- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) — the
  absorption-ceiling argument, extended to a layer it does not consider. Version control is part
  of the delivery system that has to scale when code production gets cheap.
- [Trunk-Based Development](../engineering/practices/trunk-based-development.md) — "no merge
  queues" as a principle versus as a capacity constraint, and why the distinction matters.
- [CI Speed When Agents Write the Code](../engineering/ai-native/ci-speed-with-ai-agents.md) and
  [Linear's CI Rework](linear-ci-rework.md) — checkout as setup overhead; the same parallelism
  bottleneck attacked below the pipeline rather than inside it.
- [Cursor's Agent Swarm Economics](cursor-agent-swarm-economics.md) — commit volume as an
  anti-metric. The same count read as infrastructure load rather than as throughput.
- [Anthropic's AI-Native Team Structure](anthropic-ai-native-teams.md) and
  [the claude.ai Performance Sprint](anthropic-claude-ai-performance-sprint.md) — the other two
  self-reported Anthropic accounts here; read together for a consistent house framing, and treat
  the figures with the same caution.
- [Migrating the Copilot Runtime to Rust With Agents](github-copilot-rust-migration.md) — the
  closest comparison for provenance: a company reporting on itself using its own agent, but with
  checkable numbers and an unusually self-critical limitations section. The contrast is
  instructive about what this piece leaves out.
- [Git](../tools/git.md) — the model being left behind, and why its distributed design was the
  thing that broke.
