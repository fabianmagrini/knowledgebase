---
type: case-study
title: Lovable's Migration Off Next.js
description: "A strangler-fig framework migration executed on a 42M-visitor site: proxy-worker routing with framework stickiness to avoid hard navigations, portability enforced by lint rules and platform adapters, agents drafting the PRs, and a candid OOM incident."
tags: [architecture, performance, refactoring, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/architecture/strangler-fig.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - languages-and-frameworks/go-agentic-language.md
  - case-studies/vercel-v0-instant-navigations.md
  - case-studies/chatgpt-web-performance.md
  - engineering/architecture/architectural-change-cases.md
source: "https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs"
updated: 2026-08-30
---

# Lovable's Migration Off Next.js

Lovable moved lovable.dev from Next.js on Vercel to **TanStack Start** running on Cloudflare
`workerd` workers, over roughly six months. The site reportedly serves **42M+ monthly visitors**
against a **910K+ line** non-generated codebase.

> **Read the provenance.** Lovable is describing migrating its own site *onto its own platform*,
> and says so: the stated motivations are dogfooding and demonstrating the platform can host a
> single high-traffic application. The **mechanism** below is specific and checkable. The
> **verdict on Next.js is not disinterested** — it is a framework comparison published by a party
> with a commercial stake in the conclusion, and should be read as their experience rather than
> as an evaluation.

## Framework stickiness — the frontend twist on strangler fig

The migration is a [strangler fig](../engineering/architecture/strangler-fig.md): a proxy worker
in front, routing each request to either Next.js or TanStack Start on feature flags, with
capabilities moved across one at a time. What the generic pattern does not cover is the
constraint that shaped this one.

| Navigation | Cost | When it happens |
|---|---|---|
| **Soft** — internal route change within one framework | ~1.5s | Normal operation |
| **Hard** — full document reload crossing frameworks | ~5s | Any request routed to the other framework mid-session |

Because the split runs through a live browser session, a facade that routes *per capability*
would make users pay a hard navigation every time they crossed the boundary. Lovable's answer is
**framework stickiness**: migrate whole **route groups** rather than individual routes, and keep
a user pinned to one framework within a group.

This is the generalisable lesson. In a backend strangler migration the facade can route freely,
because callers are stateless with respect to which implementation answers. On the frontend the
*client* holds state that the split can tear, so **the migration unit is bounded by the user's
navigation graph, not by the code's module graph.**

## Portability as an enforced property

The other half is making the code indifferent to which framework runs it — not as an aspiration
but as something CI can fail a PR over.

| Mechanism | What it does |
|---|---|
| `#shared/` directory | Where framework-agnostic code lives |
| **Lint enforcement** | Forbids framework imports from inside shared code |
| **Platform adapters** | Interface-based dependency injection via TypeScript aliases, so shared code calls an interface and each framework supplies the implementation |
| **Portability check** | Automated PR analysis verifying shared code stays compatible |

They targeted 90–95% framework-agnostic code and report ending at **3% framework-specific**
before removing Next.js.

This is
[branch by abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
applied at the framework boundary, and the notable part is the enforcement. An abstraction layer
that is merely *intended* to stay clean drifts as soon as one deadline makes a direct import
convenient; a lint rule plus a CI check converts the intention into a property of the build.
Getting to 3% over six months while the codebase itself grew **375K → 850K lines** is the
evidence that it held — most of that growth was new work written portable by default rather than
migrated afterwards.

Agents did much of the labour: rather than distributing the migration across teams, the author
reports using agents to draft production-ready PRs, later moving up a level to agents handling
planning and implementation in batches with the automated checks verifying compliance. The
enforcement machinery and the agent workforce are complementary — mechanical checks are what make
delegating volume to agents tolerable.

## The out-of-memory incident

The most useful section, and the least marketing-shaped. During the dashboard rollout at 20%
traffic, on a Friday afternoon:

- Unrelated **static JSON data** pushed a worker bundle past the **128MB isolate limit**
- Isolates began evicting after **fewer than 10 requests**, against a normal 500–10K
- A **0.1%** error rate cascaded to **50%** over **11 minutes**

The retrospective admission is the part worth keeping: they "ignored early warnings and accepted
a 0.1% error rate" and "did not measure initial memory use", which the author attributes to
optimism rather than a data-driven approach. A standing 0.1% error rate was treated as noise when
it was the signal, and the resource that failed was never baselined.

Isolate economics are the underlying mechanism: an isolate is a V8 sandbox heap, far cheaper than
a process, but **instantiation cost scales with bundle size** (4ms to ~1s). Bundle size is
therefore not just a download-time concern in this model — it governs how often the runtime can
afford to keep a worker resident.

## Reported figures

| Measure | Reported |
|---|---|
| Monthly visitors | 42M+ |
| Migration duration | ~6 months, ~2-month rollout |
| Codebase during migration | 375K → 850K lines |
| Framework-specific code at the end | 3% |
| Dev server startup | 10s / 1.5GB vs 70s / 8GB RAM |
| Production build | 12+ min → 6–9 min |
| Median TTFB | −49% |
| P90 response time | Initially **2× slower**, later −16% |

The P90 line is the one to keep visible. The migration made the tail *worse* before optimisation
work brought it back, and they published that rather than reporting only the median improvement.
Any similar migration should expect the same shape and budget for the recovery.

## The agent-legibility argument, already held here

Lovable's stated reason for preferring TanStack Start on agent grounds: agents perform more
reliably against a smaller, more consistent training corpus, while Next.js suffers **version
fragmentation across v12, v14 and v16 with conflicting best practices**, so agents emit
plausible code against the wrong API.

This is not a new argument in these notes — it is the **"ecosystem churn"** row of
[Go as an Agentic Language](../languages-and-frameworks/go-agentic-language.md), which makes the
same case generally: constant framework rewrites mean agents produce plausible-but-broken code
against stale APIs, and stability is an agentic virtue. Lovable is a second data point for a
held claim, supplied by an interested party. The convergence is worth noting; the source is not
independent confirmation.

## Relationship to other notes

- [Strangler Fig Pattern](../engineering/architecture/strangler-fig.md) — the pattern this
  executes. The addition is the frontend constraint: session state means the migration unit is
  the user's navigation graph, not the code's module graph.
- [Feature Flags and Branch by Abstraction](../engineering/practices/feature-flags-and-branch-by-abstraction.md)
  — the mechanism, at the framework boundary and mechanically enforced rather than merely
  intended.
- [Go as an Agentic Language](../languages-and-frameworks/go-agentic-language.md) — the general
  form of the agent-legibility argument Lovable makes for TanStack Start.
- [Vercel's Agent Loop for Instant Navigations](vercel-v0-instant-navigations.md) — the closest
  sibling in posture: a frontend platform vendor writing about its own product, with real
  mechanism inside a promotional frame. Also the counterpoint of interest, since Lovable is
  migrating *off* Vercel.
- [ChatGPT's Web Performance Architecture](chatgpt-web-performance.md) — the other high-traffic
  frontend case study here. Both treat startup and bundle size as governing constraints, but
  ChatGPT's is about the client's critical path where this is about server-side isolate residency.
- [Architectural Change Cases](../engineering/architecture/architectural-change-cases.md) — the
  anticipatory discipline this is the reactive counterpart to; the portability checks function as
  fitness functions for a change that was already underway.
