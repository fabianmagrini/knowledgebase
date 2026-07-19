---
type: note
title: Modern Engineering Values
description: "A practitioner's account (Christoph Nakazawa / cpojer) of how engineering values manifest now that coding agents write most of the code."
tags: [ai-engineering, culture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-augmented-engineering-team.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/practices/change-absorption-capacity.md
  - standards/open-knowledge-format.md
  - engineering/ai-native/trust-factory.md
  - reading/how-i-use-llms-2026.md
  - case-studies/portkey-product-engineer-company.md
  - reading/llm-maintained-wiki.md
  - reading/ownership-thorsten-ball.md
source: "https://cpojer.net/posts/modern-engineering-values"
updated: 2026-06-14
---

# Modern Engineering Values

A practitioner's account (Christoph Nakazawa / cpojer) of how engineering values manifest now
that coding agents write most of the code. The framing: agents produce code "as good as or better
than what I would write… in minutes instead of weeks", so the bottleneck has moved from producing
code to **exercising judgement and direction**. The values are surprisingly unchanged; what
changes is that engineers now *direct systems that produce code* rather than writing it directly.

> Context caveat: the author works on solo and small-team projects shipping 90–100% AI-written
> code (Vite+, Athena Crisis, Void, and others). Several positions below — pushing to main,
> avoiding PRs, owning the whole stack — are drawn from that high-velocity, low-coordination
> setting and do not necessarily transfer to large, multi-team organisations. See
> [Relationship to other notes](#relationship-to-other-notes).

## The six values

1. **Strong ownership.** Deep expertise and domain knowledge amplify an agent's effectiveness.
   Teams work best as small units (2–3 people) with clear boundaries and isolated repositories.
   Ownership spans architecture, product requirements, trade-offs, and long-term direction. Code
   review shifts from stylistic argument to *alignment* verification.

2. **Taste.** Keep a low tolerance for mediocre output — "everyone can generate a lot of bullshit
   all day long." Taste is discerning what deserves effort, and it becomes the **gating function**
   for acceleration: without it, agents fill the codebase with plausible-but-mediocre solutions.

3. **Strict guardrails and fast feedback loops.** Constrain style and correctness with linting,
   automated tests, and verification. Crucially, tooling must run on *changed files*, not the
   whole repository — "the difference between an agent completing their work in 1 minute or 60."

4. **Context in the repo.** Consolidate scattered context (wiki docs, implicit knowledge,
   production behaviour, commit history) into local repository documentation. Treat each agent
   session like onboarding a new employee — and use that documentation to inject organisational
   values and taste.

5. **Own your stack.** Reverse the historical dependency model. Where third-party libraries once
   reduced maintenance burden, agents now make building custom solutions economically viable.
   Owning core infrastructure (data libraries, UI frameworks, tooling) gives control over the
   product experience; external dependencies introduce unknown code and constraints.

6. **Option value.** Preserve future flexibility. Large-scale changes are cheap with agents, but a
   poor decision can create an inescapable constraint — "vibing yourself into a corner." Maximise
   the ability to adapt as requirements evolve.

## Supporting arguments

- **Velocity multiplied.** The author reports ~770 commits/month in 2026 versus ~328/month in
  2024 (~2.3× frequency, ~3× modifications). Treat the figures as one person's data, not a
  benchmark.
- **Quality paradox.** Agents "don't make the type of mistakes humans used to make"; hand-written
  code now attracts *more* scrutiny.
- **Coordination cost.** Without strong ownership, agents generate noise and coordination
  overhead rises proportionally.
- **Management stays technical.** Engineering management must remain domain-expert-level, not just
  outcome-focused.
- **Judgement is the scarce resource.** Rather than displacing engineers, a bottleneck on
  judgement increases demand for people who can exercise it.

## Workflow notes

Brief, illustrative of the values rather than prescriptive: force agents to write a failing test
before a fix; use `/review` cycles and change-walkthrough audits; "lazy prompting" ("I want to
build X, get context from Y and Z, make a proposal, ask questions"); run a few simultaneous
projects via spatial desktop organisation; push directly to main on single-person projects
(the author notes PR and collaboration phases slow agent velocity).

## Anti-patterns

- Running multiple agent sessions in the same project (worktrees/copies) — context-switching cost.
- Depending on mostly third-party code — restricts design control.
- Scattered context — forces agents to search inefficiently.
- Insufficient guardrails — inconsistent or unmaintainable output.
- Slow feedback loops (full-repo linting, missing tests) — multiply execution time.

## Relationship to other notes

- [The AI-Augmented Engineering Team](ai-augmented-engineering-team.md) — the operating-model
  counterpart; this note is the values/principles view from a solo/small-team practitioner.
- [The Agentic SDLC](agentic-sdlc.md) — shares "code is cheap, coherence is not" and the
  context-management discipline (here, *context in the repo*).
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — *strict guardrails and
  fast feedback loops* is the same idea: machine feedback the agent acts on, scoped to changed
  files for speed.
- [Quality-First AI Coding](quality-first-ai-coding.md) — *taste* and the `/review` and
  failing-test-first practices line up directly.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — *option value* and
  guardrails are mechanisms for keeping a system able to absorb agent-speed change.

**Tensions worth noting.** The *own your stack* and *push-to-main / avoid PRs* positions sit in
tension with [Composable Architecture](../architecture/composable-architecture.md) (which leans on
third-party and platform capabilities), [Code Review Policy](../practices/code-review-policy.md), and
[Federated PR Review](../practices/federated-pr-review.md) (which treat review as essential coordination in
multi-team settings). The article's stance is best read as optimised for small, autonomous,
expert teams rather than as a universal prescription.
