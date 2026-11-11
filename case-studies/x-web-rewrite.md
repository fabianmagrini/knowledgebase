---
type: case-study
title: X's Web Rewrite — A From-Scratch Rebuild With Agents
description: "The repo's first agent-assisted big-bang rewrite that shipped, against a held result of 28-in-520 migration runs passing audit — plus an 'anti-slop' lint plugin, the first mechanical check for a failure mode these notes name four times and never enforce. Headline team size is disputed by X's own engineers."
tags: [ai-engineering, performance, architecture, agentic-workflows, refactoring, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/chatgpt-web-performance.md
  - case-studies/lovable-nextjs-migration.md
  - case-studies/github-copilot-rust-migration.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/ai-native/linters-over-ai-review.md
  - case-studies/openai-agent-first-harness.md
  - engineering/architecture/strangler-fig.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - concepts/progressive-delivery.md
  - engineering/ai-native/agentic-verification.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - case-studies/tano-eleven-x-pr-throughput.md
  - engineering/ai-native/harness-engineering.md
  - leadership/revised-rules-engineering-leadership.md
  - tools/claude-code-steering-mechanisms.md
  - case-studies/linear-performance-architecture.md
source: "https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch"
updated: 2026-11-12
---

# X's Web Rewrite — A From-Scratch Rebuild With Agents

X engineering (4 November 2026) on replacing **rweb** — the responsive web app that had served
x.com for most of a decade — with a new application built from scratch, with AI coding agents
doing much of the implementation.

> **Retrieval limitation, which bounds this whole note.** The canonical URL returns **403** to
> automated fetch, repeatedly and across URL variants. **This note is assembled from secondary
> sources** — a [technical write-up](https://blog.dragansr.com/2026/11/x-rewite-in-rust.html) and
> search indexing of the original — which agree on the substance. **The primary source has not
> been read here**, so nothing below is quoted verbatim from X, and the usual check on what a
> post concedes about itself could not be performed. Weaker footing than any other case study in
> these notes, and the figures are doubly removed: self-reported by X, then relayed.

## The team-size claim is disputed, and it is the headline

The number travelling in coverage — *"Five Engineers Rebuilt X.com With AI Agents"* — comes with
a contradiction attached:

| Source | Team size |
|---|---|
| The circulating figure | **~5 engineers**, first version in under six months |
| **X's Mridul Singhai** | **10–15 engineers** worked on it |
| The announcement thread | thanks roughly **a dozen** named engineers and designers |

**Both numbers come from X.** The charitable reconciliation is that five built the first version
and ten to fifteen contributed to the broader project, which is plausible and unverified. What
matters for these notes is that **the most quotable figure in the story is contested by the
company that produced it**, and a 2–3× range on the denominator changes what the result means
entirely.

This is the same shape as the counterfactual problem flagged in
[the Copilot Rust migration](github-copilot-rust-migration.md) — *"work that would have taken a
whole team a year or two"* is a comparison nobody ran — except here the *actual* team size is
also unsettled.

## Why it matters: the rewrite shape the repo has evidence against

**This is the first agent-assisted from-scratch rewrite in these notes that shipped**, and it
runs against the sharpest negative result held here.

[Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md)
reports **28 of 520** agent migration runs passing a full audit — roughly 5% — with *migration
blindness* as the failure mode. The two successes recorded since both avoided the big-bang shape
deliberately:

| Case | Shape | Why it worked, as stated |
|---|---|---|
| [Copilot runtime → Rust](github-copilot-rust-migration.md) | **In-place porting**, trunk always shippable, 135 releases in 14.5 weeks | *"the structural difference from a big-bang rewrite that gets audited once at the end"* — plus an interop-shim count driven to **zero** |
| [Lovable off Next.js](lovable-nextjs-migration.md) | **Strangler fig** with proxy routing and framework stickiness | Portability enforced by lint rule and a CI check |
| **X's rweb replacement** | **From scratch**, new application alongside the old | Not established from the readable material |

So either this is a second success with conditions the repo has not identified, or the
conditions it has identified are not the operative ones. **Recorded as a case to test rather
than a refutation**, for two reasons: the rollout is incomplete (below), and the verification
question is unanswered.

**The unanswered question is the important one.** A from-scratch rebuild faces exactly the
problem the Copilot migration solved with a shim inventory: how do you know the new thing does
what the old thing did? The Copilot team made that *"impossible to fake"* by driving a count to
zero.
[Agentic Verification](../engineering/ai-native/agentic-verification.md) names **differential
testing** — treat the legacy system as the oracle — as the technique for precisely this, and
rweb was available to serve as that oracle. **Whether it was used that way is not visible in the
secondary material**, and it is the first thing to look for if the primary source becomes
readable.

## The anti-slop lint plugin

The most portable mechanism, and the reason this note earns its place independent of the rewrite
claim. Their agent guardrails were reportedly three:

- an explicit **`AGENTS.md`** instruction file
- **custom oxlint plugins**, including an **"anti-slop" filter**
- **pre-commit hooks**

**"Slop" is named four times in these notes and mechanised in none of them.**
[Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) carries *slop
cannons*, [Revised Rules](../leadership/revised-rules-engineering-leadership.md) carries *slop
pull requests*, [Harness Engineering](../engineering/ai-native/harness-engineering.md) lists slop
as a named failure mode, and *slop grenades* arrives via Lütke. All four describe it; **this is
the first instance of a team writing a check for it.**

It is also `linters-over-ai-review`'s thesis implemented at scale — custom linters beat AI review
on cost, speed and fit — by a team that reached for exactly that rather than for a review agent.
And the combination is the same stack as
[OpenAI's agent-first harness](openai-agent-first-harness.md): a short instruction file plus
mechanically-enforced constraints plus linters, which is now the third independent arrival at
that arrangement. The distinction `claude-code-steering-mechanisms` draws holds here —
`AGENTS.md` is a *rule* the model may forget, a pre-commit hook is a **gate** it cannot.

What the filter actually matches is not described anywhere accessible, which is the detail that
would make it copyable.

## Architecture: three servers to one, response shape by requester

The legacy app used three servers for three audiences. The replacement consolidates them and
varies the response by who is asking:

| Requester | What it gets |
|---|---|
| Real users | fast-streaming HTML |
| Search crawlers | fully-rendered documents |
| Link-preview bots | metadata only |

**[ChatGPT's web performance architecture](chatgpt-web-performance.md) arrives at the same
place independently** — streaming SSR, render-first, prepaid bot defence, *"the network is the
enemy"* — and the bot-class split is more explicit here. Two of the largest logged-out-traffic
properties on the web converging on one shape is worth more than either account alone: when most
of your traffic is anonymous and much of it is not human, **the server has to know which kind of
requester it is answering before it decides what to render.**

Reported stack: Vite, React with streaming SSR and Suspense, Fastify, **Platformatic Watt** on
Node v26, Relay + GraphQL, TypeScript, Tailwind — plus **XDS**, a shared component library built
on Base UI. The link-preview card image generator was rewritten in **Rust**.

XDS is worth noting against
[Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md):
building the constraint layer *during* an agent-assisted rewrite is that note's argument applied
at the moment it is hardest to justify, since a component library is overhead until the second
consumer exists.

## Performance, and the rollout

**22 seconds → ~2.7 seconds** to first post on a profile over a throttled slow connection,
reported as **8–13×** faster overall. That joins a short list of measured frontend results here
beside [Anthropic's 3.1× geometric mean](anthropic-claude-ai-performance-sprint.md) and Linear's
local-first architecture — and the *slow connection* framing is the right one, since it is where
architecture shows up and where fast-network benchmarks hide it.

Rollout is the conservative part and the most transferable:

- **logged-out traffic first** — the population with no session state to migrate
- then **signed-in users country by country**, via edge routing and feature switches

That is [progressive delivery](../concepts/progressive-delivery.md) at an unusual
granularity, and it echoes the sequencing insight in
[Lovable's migration](lovable-nextjs-migration.md): session state is what makes a frontend
migration hard, so **the users without it go first**. Lovable's unit was the user's navigation
graph; X's is geography.

## What is not established

- **No verbatim primary source**, as above. Everything here is relayed.
- **Team size is contested by X's own engineers**, 5 against 10–15.
- **No equivalence or verification story.** The single most valuable idea from the comparable
  success — a count driven to zero — has no counterpart in the readable material.
- **The outcome is not known yet.** Signed-in migration is mid-rollout country by country, so
  this is a successful *launch*, not a completed replacement. The Copilot migration could point
  at zero remaining shims; this cannot yet point at anything equivalent.
- **No PR counts, authorship fraction, or cost figures** — nothing comparable to the
  instrumented detail that made the Copilot account checkable, and none of the
  [token-spend figures](tano-eleven-x-pr-throughput.md) now held elsewhere.
- **No incident account.** A decade-old application being replaced under live traffic without a
  single reported problem is either remarkable or unreported, and there is no way to tell which.
- **What the anti-slop filter checks** is undescribed, which is the one detail that would make
  the best idea in the piece reusable.

## Relationship to other notes

- [Brownfield Agentic Engineering](../engineering/ai-native/brownfield-agentic-engineering.md) —
  the 28-of-520 result this appears to cut against; read as a case to test, since the
  verification question is open.
- [Migrating the Copilot Runtime to Rust](github-copilot-rust-migration.md) — the better-evidenced
  success, and the contrast that matters: in-place porting with a measurable completion test
  against a from-scratch rebuild with none described.
- [Lovable's Migration Off Next.js](lovable-nextjs-migration.md) and
  [Strangler Fig](../engineering/architecture/strangler-fig.md) — the incremental alternatives;
  both chose not to do this.
- [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) — independent arrival at
  the same requester-aware serving architecture, at comparable anonymous-traffic scale.
- [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — its thesis
  implemented, and the first mechanical check for slop in these notes.
- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — the same instruction-file plus
  linters plus hooks arrangement, now arrived at three times independently.
- [Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md)
  — XDS as the constraint layer, built during the rewrite rather than after it.
- [Progressive Delivery](../concepts/progressive-delivery.md) — logged-out first, then
  country-by-country.
