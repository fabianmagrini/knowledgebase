---
title: What Is Software Engineering? (Adapting to AI)
tags: [ai-engineering, ci-cd, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/practices/agile-in-the-age-of-ai.md
  - engineering/practices/ai-engineering-discipline.md
  - engineering/practices/ci-cd-ai-engineering.md
  - concepts/continuous-delivery.md
  - engineering/architecture/team-topologies.md
  - engineering/practices/ai-native-engineering-overview.md
  - reading/building-software-is-learning.md
source: "https://blog.colinbreck.com/adapting-to-ai-what-is-software-engineering/"
updated: 2026-06-27
---

# What Is Software Engineering? (Adapting to AI)

Colin Breck's essay argues that AI changes the **speed and economics** of software
engineering — how cheaply and quickly we can iterate and experiment — but **not
what defines good engineering**. Written from the perspective of operating
critical infrastructure (manufacturing, power, transportation), it is a grounded
counter to the idea that AI rewrites the fundamentals.

It is the engineering-discipline sibling of
[Agile in the Age of AI](../engineering/practices/agile-in-the-age-of-ai.md): same
"the fundamentals endure" stance, but argued through Dave Farley's definition of
the discipline rather than through Agile values.

## What software engineering is

Drawing on Farley's *Modern Software Engineering*, Breck defines it as *"the
application of an empirical, scientific approach to finding efficient, economic
solutions to practical problems in software"* — a process of **discovery and
learning**, not merely code production. Three pillars:

1. **Optimising for learning** — iteration, experimentation, feedback.
2. **Managing complexity** — modularity, abstraction, separation of concerns.
3. **Supporting tools** — automated testing, CI/CD, fast builds.

### Craft vs. engineering

The load-bearing distinction: **craft** produces one-of-a-kind items with high
variance and low repeatability; **engineering** is *scalable and repeatable
through controlling complexity and variance*. Breck's challenge to leaders: ask
whether your organisation actually practises engineering or craft — AI rewards the
former and amplifies the weaknesses of the latter.

## What endures

- **Modularity.** "As soon as there is coupling, there are constraints on how much
  work can be parallelised" — true for agents as much as humans.
- **Abstractions.** They define failure domains, security boundaries, and scaling
  units — independent of who writes the code.
- **Full-lifecycle ownership.** Owning development *through operations* keeps teams
  grounded in reality and focused on outcomes.

## What shifts

- **Build speed becomes an existential differentiator.** Organisations with
  seconds-fast build-test cycles will "far out-iterate" those measured in minutes
  or hours. Breck calls fast, scalable builds *the* most important investment — the
  feedback loop AI leverages (see [CI/CD as the control plane](../engineering/practices/ci-cd-ai-engineering.md)).
- **Duplication may beat shared libraries.** When rewriting code is cheap, the
  classic DRY trade-off shifts toward local duplication over shared coupling.
- **Information-hiding boundaries may move**, because an AI can hold far more
  context than a human can.

## The cost of integration is the killer

Breck's sharpest claim: *"the cost of integration is the killer, and this applies
equally to AI agents and humans."* Organisations with **many handoffs** will
perform far worse with AI — it is a structural problem AI *amplifies* rather than
solves. This is the same fracture-plane/Conway argument as
[Team Topologies](../engineering/architecture/team-topologies.md): low-coupling,
full-ownership teams convert AI into outcomes; handoff-heavy ones do not.

## The underappreciated frontier: operations

Breck notes that AI's largest leverage may be in **operations** — analysing logs,
incident response, continuous monitoring — which receives far less attention than
code generation. Full-lifecycle teams are positioned to capture it.

## The takeaway

- **Engineers:** invest in fast, scalable build systems first; master systems
  thinking, full-lifecycle responsibility, and deliberate abstraction — don't treat
  AI as a shortcut around disciplined practice.
- **Leaders:** minimise handoffs; build observability and testing infrastructure.
  The organisations that transform with AI won't be those throwing more AI at poor
  fundamentals — they'll be those with excellent CI/CD, automated acceptance tests,
  and fast feedback loops AI can exploit.

> Named references: Dave Farley's *Modern Software Engineering*, Margaret Hamilton
> (who coined "software engineering"), Boris Cherny (Claude Code), and a Stanford
> study on large-scale online experiments finding only ~33% of tested ideas
> improved their target metric.

## Relationship to other notes

- [Agile in the Age of AI](../engineering/practices/agile-in-the-age-of-ai.md) —
  the same fundamentals-endure thesis from the Agile/sustainable-pace angle.
- [AI Demands More Engineering Discipline](../engineering/practices/ai-engineering-discipline.md)
  — the complementary "discipline shifts to validating behaviour" argument.
- [CI/CD as the Control Plane](../engineering/practices/ci-cd-ai-engineering.md) and
  [Continuous Delivery](../concepts/continuous-delivery.md) — the fast-feedback
  infrastructure Breck names as the most important investment.
- [Team Topologies](../engineering/architecture/team-topologies.md) — the
  structural side of "the cost of integration is the killer".
