---
type: note
title: Enforced Architecture Rules for Agents and Humans
description: "Making architectural violations fail the build rather than documenting them: package classification, layer rules, and role-based rules as a three-tier hierarchy — because instructions in markdown do not bind an agent."
tags: [architecture, ai-engineering, system-design, agentic-workflows, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/skeleton-architecture.md
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/ai-native/agent-backpressure-loops.md
  - case-studies/openai-agent-first-harness.md
  - engineering/architecture/adr.md
  - engineering/architecture/overview.md
  - engineering/ai-native/light-and-dark-factories.md
source: "https://nick-tune.me/blog/2026-08-13-enforced-application-architecture-for-agents-and-humans/"
updated: 2026-08-23
---

# Enforced Architecture Rules for Agents and Humans

Nick Tune (August 2026) on enforcing application architecture **deterministically** instead of
describing it in skill files, ADRs and markdown that agents do not reliably follow. His
framing of the problem:

> AI does dumb stuff like that all the time **even with a million lines of markdown screaming
> at it not to**.

A practitioner experience report from a TypeScript NX monorepo, with working configuration.
He is explicit that it is in progress — the role-annotation layer in particular is something
he asks readers to "come back in 6 months" on.

These notes have asserted mechanically-enforced architecture in several places —
[Skeleton Architecture](skeleton-architecture.md), the golden principles in
[OpenAI's harness](../../case-studies/openai-agent-first-harness.md), domain leakage as a
fitness function in [Comprehension as an Architectural Characteristic](comprehension-as-architecture.md).
This is what the rules actually look like.

## Three tiers, in order of preference

| Tier | Rule shape | When |
|---|---|---|
| **1. Package classification** | A package matching `packages/{subdomain}/domain-model` must have exactly one root folder `/domain`, and cannot import other subdomains' domain models or use-cases | First — cheapest and broadest |
| **2. Layer rules** | For a given folder, which others may it import from | The default. *"Strive for broad, generic rules at the layer level"* |
| **3. Role rules** | `adapters` may import **only** `domain-port` from `/domain` — not `aggregate`, not `domain-service` | Last resort, where layers cannot express it |

The ordering is the guidance. Broad structural rules are cheap to define, cheap to understand
and rarely need exceptions; fine-grained role rules are powerful but carry the cost of
classifying every piece of code.

**Roles come from source annotations** — `/** @riviere-role domain-port-adapter */` — so the
check is on *what a file is*, not merely where it sits. That is what allows a rule to say
"this layer may import that concept but not this other one from the same folder."

Violations **fail the build**. Putting a `domain-model` at the root of `packages` with no
subdomain folder breaks it.

## The mechanism: unrepresentable, not discouraged

The load-bearing idea is that the constraint should make the mistake **impossible to express**
rather than merely against the rules:

> AI cannot implement an aggregate inside `value-object` because an `aggregate-repository`
> must return an `aggregate`. So it wouldn't be able to load it.

This is the **gate versus rule** distinction from
[Backpressure Loops for Coding Agents](../ai-native/agent-backpressure-loops.md), applied to
the import graph. A rule in a markdown file has an opt-out path an agent can reason around; a
build failure does not.

**He also closes the obvious escape route**, which is the part most constraint systems miss.
You might expect an agent to dodge the adapter restriction by putting logic into a
`domain-port` instead — but that role is itself tightly constrained, so it cannot. A
constraint system gets gamed unless the neighbouring roles are bounded too.

## What the rules encode

The domain-isolation rule is the one he rates highest:

> If you're only going to add one convention in your codebase, enforcing domain isolation is
> probably the best one.

Domain code cannot import HTTP controllers, database transactions or plumbing. The single
exception is **published language** — pure, versioned contracts such as schemas.

Inside `/domain` any sub-structure is allowed, deliberately: *"domain models should express
the business however necessary."* Use-cases get the opposite treatment — a whitelist of
feature-oriented folders (`/commands`, `/queries`, `/data-access`, `/adapters`) with **no
sharing between feature folders**, because orchestration should be "standardised and boring."

Subdomain isolation is enforced structurally: a `use-cases` package in one subdomain can reach
`domain` only in its **own** subdomain, and other subdomains only through published language.
That is [change locality](change-locality.md) made mechanical — the boundary is not a
convention that can drift, it is a build gate.

## The ADR stays alongside

The executable configuration is paired with an **ADR describing the same architecture for
humans**, kept aligned with it. Two views of one decision: the config binds the build, the
[ADR](adr.md) carries the rationale.

That pairing matters given
[Comprehension as an Architectural Characteristic](comprehension-as-architecture.md) — an
enforced rule prevents violation but explains nothing, so on its own it converts architectural
knowledge into an unexplained constraint. The ADR is what stops the enforcement becoming
folklore.

## The reported second-order benefit

Beyond consistency, he reports the setup improves **planning**: when starting a feature the
team discusses which new roles are needed and where parts of the solution will live.

> Not big up-front design, but getting the rough shape right and identifying tricky decisions
> early.

The vocabulary of roles and layers gives the design conversation something concrete to be
about — and it is the same "judgement upstream" placement argued from a different direction in
[Light and Dark Software Factories](../ai-native/light-and-dark-factories.md).

## His own verdict

Appropriately hedged, and worth carrying:

- **Package, domain and layer rules** — easy to set up and enforce. *"I find it hard to justify
  not adding those. If you can't set codebase standards at that level, I don't think you'll get
  far with agentic AI."*
- **Full role annotation** — still experimental. He believes it is right but is not claiming it
  yet.
- **A real trade-off**: adding constraints every time an agent writes poor code means *"trading
  off optimal code vs consistent boring code"* — he does not pretend that is free.

The tooling specifics (NX, the `riviere` configuration format) are one implementation. The
transferable part is the tier ordering and the annotation-based role check, which have
equivalents elsewhere — import-boundary linting, ArchUnit-style tests, dependency rules in a
build config.

## Relationship to other notes

- [Skeleton Architecture](skeleton-architecture.md) — an immutable human-designed skeleton
  constraining generated tissue; this is the same intent expressed as import rules rather than
  as inheritance and schema contracts.
- [Change Locality and Boundary Drift](change-locality.md) — subdomain isolation enforced at
  build time is a boundary that *cannot* silently drift, which is one answer to that note's
  problem.
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) — bounded contexts as
  theory; these rules are one way to make the context boundary real rather than aspirational.
- [OpenAI's Agent-First Harness](../../case-studies/openai-agent-first-harness.md) — its
  "golden principles" and layered dependency direction are the same practice at another
  organisation, described from the outside.
