---
type: case-study
title: Datadog's Continuous Formal Spec Validation
description: "A TLA+-to-Rust transpiler producing runtime monitors from formal specs, answering two absences these notes recorded: how a specification is maintained against drift, and who checks it. A year of undetected drift, 0.01% conflicting placements, and two of them enough to crash recovery."
tags: [testing, system-design, observability, architecture, reading]
topic: case-studies
status: notes
level: advanced
related:
  - case-studies/anthropic-formal-verification-at-scale.md
  - engineering/architecture/runtime-architecture-verification.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/ai-native/agentic-verification.md
  - languages-and-frameworks/rust-for-agentic-development.md
  - concepts/resilient-software-design.md
  - reading/fintech-engineering-handbook.md
  - tools/postgresql-ha-kubernetes.md
  - engineering/architecture/cell-based-architecture.md
  - engineering/architecture/agents-as-distributed-systems.md
  - case-studies/airbnb-database-workload-replay.md
  - engineering/practices/release-confidence.md
  - case-studies/github-copilot-rust-migration.md
source: "https://www.datadoghq.com/blog/engineering/continuous-formal-spec-validation/"
updated: 2026-11-21
---

# Datadog's Continuous Formal Spec Validation

Nicolas Couvrat (Datadog, November 2026) on **FETCh** — a *Formal Execution Trace Checker* that
compiles TLA+ specifications into Rust runtime monitors, which consume production telemetry and
flag divergence between the specification and what the system actually does.

**This answers two absences these notes recorded eight days ago.**
[Formal Verification at Scale With LLMs](anthropic-formal-verification-at-scale.md) closes with:

> **Nothing on maintenance.** A 600,000-line proof is an artefact that breaks when the code
> changes, and proof repair under ordinary development churn is not discussed.
>
> **Nothing on specification review.** If the semantics are the trusted base, who checks them,
> and how? The authors identify this as the load-bearing assumption and do not say how to
> discharge it.

Datadog's entire subject is both of those. Where the Anthropic work **establishes** a property
against a specified machine, this is about what happens to a specification over the following
year — and it is the first note here where the **spec-reality gap is measured rather than
conceded.**

## A year of drift, and why nothing caught it

The Husky event database had TLA+ specifications that were accurate when written. Then:

> A year earlier, we had added special cases in which we intentionally skipped deduplication and
> allowed conflicting placements to improve balancing. **What we missed was that those placements
> were still being persisted.**

Note the shape: the change was *deliberate and reasoned*, and the drift was a **second-order
consequence** nobody traced. This is not a case of an undocumented hack — it is a considered
decision whose implications outran the model of the system.

Why a year passed:

> The conflicting placements were harmless during normal operation. They would have caused
> problems only during a specific and relatively rare failure scenario involving placement data
> loss. **That's not a scenario we can realistically exercise through conventional test suites.**

And the asymmetry, which is the number to remember:

> We estimate that **fewer than 0.01%** of placements conflict. Even at that rate, **two
> conflicting placements are enough to cause our backfill system to crash**.

> The backfill system is designed to recover from placement data loss, but it does not tolerate
> placement conflicts… a placement data-loss event would have prevented the backfill system from
> recovering correctly.

**The latent defect was in the recovery path**, which is the path you need working when things
are already bad. [Resilient Software Design](../concepts/resilient-software-design.md) argues
resilience must be designed in because failure is normal and partial; this is the sharper
corollary — **the recovery mechanism is itself code that can be silently wrong, and it is the
hardest code to exercise.** A 0.01% rate is invisible to sampling and sufficient for total
failure, which is the combination no amount of green CI reveals.

## Observable versus model-checkable, bridged by refinement

The conceptual contribution, and the part that transfers regardless of tooling. One specification
cannot serve both purposes:

| | Needs |
|---|---|
| **Model-checkable** | *"bounded inputs to remain tractable — for example, a set of two clients and three events"*, and must describe **how** things happen, *"by modeling a network as a queue of incoming requests—so that all possible executions can be explored"* |
| **Observable** | *"unbounded inputs because a real system can process a continuous stream of requests"*, and *"should declare **what is allowed, not how it happens**"* |

Those are contradictory requirements, which is why specs written for a model checker cannot
simply be pointed at production. The bridge is TLA+ refinement:

> A specification B **refines** a specification A if every behavior allowed by B is also allowed
> by A. This relationship allows us to bridge the gap between observable and model-checkable
> specifications: We can define an observable specification A that describes real-world behavior
> and a model-checkable specification B that refines A by introducing the bounds needed for
> tractable analysis.

So **one formal foundation serves three purposes**: observable through generated runtime
monitors, model-checkable through a refinement, and provable with theorem provers such as
Isabelle or Zenon. They are explicit that these are complementary rather than substitutes — the
monitor checks production against the permissive spec, the model checker proves the bounded
version forbids what it should.

That sharpens the formality spectrum in
[Spec-Driven Development](../engineering/ai-native/spec-driven-development.md), whose top rung is
*"machine-checkable — TLA+, Lean"* for *"critical algorithms and protocols"*. The implicit
picture there is a spec written once and checked once. **This is the top rung running
continuously**, and the refinement relationship is what makes a single spec usable both ways.

## How the monitor is derived

> FETCh relies on the general structure of TLA+ specifications to generate Rust monitors. A
> specification contains variables that track system state and a `Next` formula that describes
> the allowed state transitions. FETCh maps those concepts directly to a monitor that maintains
> the state variables and defines one function for each action in `Next`.

> For each incoming event, the monitor identifies the corresponding function, checks its
> preconditions, and applies the state update. **If a precondition is violated, the system has
> performed an action that the specification does not allow.**

The scaling work is the engineering, and three mechanisms are worth recording:

- **Process-local monitoring** — routing-service validation scoped per pod via `fetch:per_proc`
  annotations, so the monitor never has to track trillions of event IDs globally. The same
  instinct as [cell-based architecture](../engineering/architecture/cell-based-architecture.md):
  **bound the state a component must hold by bounding what it is responsible for.**
- **`FetchMap` and `FetchSet`** abstractions, RocksDB-backed where placement state is too large
  for memory.
- **Modular specifications** — `Router.tla` and `PlacementStorage.tla` validated independently
  rather than as one global model.

## The overhead, which is what makes it practice rather than research

> In the sidecar running alongside our routing service, we measured **p90 overhead of about 2%
> CPU and less than 0.2% memory** across thousands of pods processing tens of millions of events
> per second.

Across **more than 1,300 routing-service pods**. And for the state too large to monitor inline:

> Batch validation of placement overlap processed several days of data containing several million
> placements in **around an hour by using 1 CPU and a few gigabytes of memory**.

**This is the cost figure the Anthropic formal-verification note had no equivalent of.** That
work reports ~33 lines of Rocq per instruction and no cost, compute or duration figures at all.
Here the ongoing cost of continuous formal validation is 2% CPU — which reframes the usual
objection. The expensive part of formal methods is evidently **writing and maintaining the
specification**, not running the check.

## It extends an argument these notes already hold

[Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
holds that *"structure is checkable statically; topology is not"* — a violation static analysis
structurally cannot see, because *"a `fetch()` creates no module dependency to see."*

**This is the same argument one layer deeper, for behaviour rather than topology.** A
specification violation creates no artefact a static check or a test can observe: the code
compiles, the types hold, the tests pass, and the system is doing something its own model
forbids. The only place the violation exists is in the **sequence of states a running system
passes through**, so the monitor has to live in production.

It also puts a mechanism behind a failure mode
[Agents as Distributed Systems](../engineering/architecture/agents-as-distributed-systems.md)
names and leaves unanswered: *"infrastructure metrics such as latency and error rate may remain
stable, while user-facing quality deteriorates."* That note asks for quality to become a
first-class reliability concern and offers no way to measure it. **A runtime monitor derived from
a formal specification is one answer** — not for model quality, but for the class of silent
degradation where behaviour diverges from intent while every operational signal stays green.

And it belongs beside [Airbnb's replay rig](airbnb-database-workload-replay.md) as the second
instance of *verification that runs against production reality rather than against a test
double*. Airbnb compares two implementations on recorded traffic; Datadog compares one
implementation against a formal statement of what it may do. Both find the thing no suite finds,
and for the same reason: **the oracle is external to the code under test.**

## Their stated limitations

Quoted because they bound the claim precisely, and the second is the significant one:

> The FETCh transpiler supports only a subset of TLA+ and **currently checks preconditions only
> against the current state**. Monitoring a distributed system with FETCh also requires
> engineering effort to instrument it. Validating global state at production scale remains
> challenging and often requires system-specific solutions.

Checking only against current state means **no temporal properties** — "eventually X" and
"always eventually Y", which is much of what TLA+ exists to express, is outside what the monitor
can enforce. So this catches *safety* violations (something forbidden happened) and not
*liveness* failures (something required never happens).

Their read on why formal methods stay niche is also honest and matches the repo's experience of
the field: *"Their syntax is often unfamiliar to software engineers, much of their tooling
originated in academia, and choosing the right level of abstraction requires a deep
understanding of both the system and the modeling framework."*

## What the piece does not cover

- **No false-positive account.** How often a monitor fires because the *specification* is wrong
  rather than the implementation is the operational question for anyone adopting this, and it is
  not addressed. The Copilot migration's *"incorrect test oracles"* failure class applies
  directly: a wrong spec is a wrong oracle, and here it is the oracle with authority.
- **FETCh does not appear to be open source**, so none of this is independently checkable —
  unlike the Anthropic work, which published its semantics and a subset of its proofs.
- **Datadog on Datadog**, with all figures self-reported. Mitigated by the fact that the
  headline finding is a **bug in their own system that survived a year**, which is the credible
  direction for self-reporting.
- **Nothing on who writes the specification**, or how a team acquires the skill their own
  adoption paragraph says is scarce.
- **No account of spec maintenance cost** — ironically, given the note's subject. If the spec is
  the trusted base, the labour of keeping *it* correct is the thing a reader needs priced, and
  only the monitor's runtime cost is given.

## Relationship to other notes

- [Formal Verification at Scale With LLMs](anthropic-formal-verification-at-scale.md) — the two
  recorded absences this answers: specification drift over time, and the cost of checking
  continuously. Read as a pair: one establishes a property, this keeps it true.
- [Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
  — *"structure is checkable statically; topology is not"*, extended to behaviour.
- [Spec-Driven Development](../engineering/ai-native/spec-driven-development.md) — its formality
  spectrum's top rung, running continuously rather than checked once.
- [Agentic Verification](../engineering/ai-native/agentic-verification.md) — the oracle thread; a
  formal spec is an oracle independent of the implementation by construction.
- [Airbnb's Database Workload Capture and Replay](airbnb-database-workload-replay.md) — the other
  instance of verification against production reality; differential testing there, formal
  monitoring here.
- [Agents as Distributed Systems](../engineering/architecture/agents-as-distributed-systems.md) —
  silent degradation with every operational metric flat; this is a mechanism for detecting the
  deterministic version of it.
- [Resilient Software Design](../concepts/resilient-software-design.md) — the recovery path as
  code that can be silently wrong, and the hardest to exercise.
- [Fintech Engineering Handbook](../reading/fintech-engineering-handbook.md) — *"invariants —
  assertions about money that must always hold; fail loudly when broken"*. Same discipline, with
  a formal specification as the source of the invariants rather than hand-written assertions.
- [Highly Available PostgreSQL on Kubernetes](../tools/postgresql-ha-kubernetes.md) — Datadog's
  other engineering account here, and a consistent house interest in failure paths.
