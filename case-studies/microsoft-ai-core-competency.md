---
title: Microsoft's AI Strategy — Finding Core Competencies (Nadella)
tags: [ai-engineering, decision-making, leadership, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - leadership/plan-is-not-a-strategy.md
  - engineering/practices/agentic-ai-strategy-frameworks.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/model-routing-and-ai-gateways.md
  - product/explore-vs-exploit.md
source: "https://stratechery.com/2026/an-interview-with-microsoft-ceo-satya-nadella-about-finding-core-competencies/"
updated: 2026-07-05
---

# Microsoft's AI Strategy — Finding Core Competencies (Nadella)

In a Stratechery interview with Ben Thompson, Satya Nadella argues that Microsoft's advantage
in the AI era comes not from owning the frontier model but from being **"a trusted purveyor of
a platform"** that lets others create value. The recurring discipline: *"the world wants them
to do the one thing"* rather than chasing everything out of competitive envy. The claims below
are Nadella's framing of Microsoft's strategy, not independently established facts.

This is a **corporate-strategy** case study — an outlier among the engineering/org case studies
here — captured for its transferable mental models rather than Microsoft specifics.

## Core competency as discipline

Nadella frames core-competency focus as a hard-won organisational discipline: resist doing
everything simply because a competitor does. This is the same move as choosing **where to play
and where not to** in [A Plan Is Not a Strategy](../leadership/plan-is-not-a-strategy.md) —
strategy as an integrative set of choices, applied at the corporate level.

## The hill-climbing machine

The central mental model: enterprises want a **"hill-climbing machine"** — continuous AI
optimisation toward their own objectives, run on a shared **multi-tenant learning system**.

> "Your moat as a company is your tacit knowledge."

The strategic consequence: **private evals** (enterprise-specific benchmarks) and reinforcement-
learning environments become the most valuable IP a company can build — proprietary because they
encode tacit knowledge competitors can't copy. Microsoft positions itself to *host* that
optimisation rather than win the model race outright.

## Capital allocation

Nadella describes a **three-bucket** approach to capex, and defends a *lower* capital commitment
than peers as disciplined allocation rather than underinvestment:

| Bucket | Rationale |
|---|---|
| **Hyperscale infrastructure** | Broad customer base, not dependent on any single AI lab |
| **Microsoft's own application businesses** | Higher lifetime value than raw capacity |
| **Research compute (MAI models)** | End-to-end model capability of its own |

He argues frontier labs will eventually build their own infrastructure anyway, so prioritising
internal apps and research over raw Azure capacity is prudent — and warns against "easy money"
from speculative customers ("Neolabs") at the expense of longer enterprise relationships.

## Token capital and the efficiency lens

Nadella frames compute as **"token capital"** — computational capacity as a corporate asset
alongside human capital — measured at the system level as **tokens-per-dollar-per-watt**. The
argument: consumption-based pricing forces an optimisation discipline software previously
lacked, because agents impose a "real marginal cost." Enterprises will therefore ruthlessly
select models and configurations for efficiency rather than assume hardware improvement erases
waste.

## Business-model shift

The traditional per-seat SaaS licence is described as evolving toward **hybrid pricing** —
per-user entitlements *plus* consumption billing that reflects actual compute used by
autonomous agents. Microsoft concentrates agent development where token consumption is
economically justified and it has existing expertise: **coding, security, and knowledge work**.

## Model and harness independence

Two deliberate structural choices:

- **MAI models built from scratch** (not distillation) to keep end-to-end control, while
  incorporating OpenAI IP via reverse knowledge distillation. Nadella frames independent model
  capability as prudent diversification, acknowledging Microsoft may have been "lulled to sleep"
  by early OpenAI advantages — while noting the partnership runs to 2032.
- **Harness independence** — GitHub Copilot and security platforms are model-agnostic, letting
  OpenAI, Anthropic, and Microsoft models compete behind one interface. This is the commercial
  expression of the [harness](../engineering/practices/harness-engineering.md) idea: own the
  orchestration layer, rent the model.

## Relationship to other notes

- **[A Plan Is Not a Strategy](../leadership/plan-is-not-a-strategy.md)** — "do the one thing"
  and the capital-allocation choices are where-to-play / how-to-win decisions; this is that
  framework observed in a real corporate strategy.
- **[Agentic AI Strategy Frameworks](../engineering/practices/agentic-ai-strategy-frameworks.md)**
  — the private-evals-as-moat and hill-climbing ideas are the enterprise-strategy layer above
  those planning frameworks.
- **[Harness Engineering](../engineering/practices/harness-engineering.md)** — model-agnostic
  harness independence is the business rationale for "own the harness, rent the model."
- **[Exploring vs Exploiting in Product Discovery](../product/explore-vs-exploit.md)** — the
  hill-climbing machine is continuous exploitation toward a firm's objective; core-competency
  focus is a deliberate narrowing of the exploration space.
