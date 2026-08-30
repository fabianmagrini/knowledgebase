---
type: note
title: Runtime Architecture Verification
description: "Some architectural violations exist only while the system runs — a fetch() creates no module dependency — so conformance needs call-graph diffing beside static rules, with scoring kept deterministic and the model confined to interpretation."
tags: [architecture, system-design, observability, governance, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/architecture/enforced-architecture-rules.md
  - concepts/control-and-complexity.md
  - engineering/architecture/comprehension-as-architecture.md
  - engineering/architecture/change-locality.md
  - engineering/architecture/architectural-change-cases.md
  - case-studies/netflix-service-topology.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/architecture/data-readiness-for-agents.md
source: "https://www.linkedin.com/pulse/you-cant-govern-what-see-luca-mezzalira-quige/"
updated: 2026-08-30
---

# Runtime Architecture Verification

Luca Mezzalira (August 2026) argues that as agents accelerate code generation, architectural
drift arrives faster than review can catch it — *"six people writing by hand produce drift you
can read carefully, while the same six with agents produce more change in a week than anyone
will read"* — and that no single class of signal is sufficient, because each is "blind in a
different direction."

> **Provenance.** The article carries an explicit disclosure: *"Built on Google Cloud with
> Gemini Enterprise Agent Platform, in partnership with Google Cloud."* Roughly half of it is a
> GCP reference implementation — ADK, Agent Runtime, Memory Bank, Cloud Run, Cloud Trace,
> SPIFFE workload identity, Gemini Pro 2.5. **This note deliberately does not carry that half**,
> which is vendor architecture that will date. The two ideas below are separable from it and
> hold on their own.

## The violation static analysis structurally cannot see

The load-bearing finding, and the reason this note exists separately from
[Enforced Architecture Rules](enforced-architecture-rules.md).

The stated architecture said a service may only publish messages to reach another. Checkout
needed current stock before confirming an order, so **it called inventory over HTTP and waited
for the answer**. Every static check passed.

> "The drift that actually hurt lived in an edge no node-level instrument can resolve, because a
> `fetch()` creates no module dependency to see."

It was caught by **comparing the source-level dependency graph against actual call graphs
derived from traces** — the edge appearing as *"checkout to inventory over HTTP, marked
runtime-only because no import anywhere corresponds to it"*, or as he puts it, *"a dependency
the running system had and the source did not, found by comparing what the code says with what
the system does."*

**Why this is a real limit rather than a gap in tooling.** The dominant approach in these notes
is to make a violation *impossible to express* — an import rule that fails the build. That works
precisely because the violation is an import. A synchronous HTTP call to a URL is not an import,
carries no static reference to the thing it couples to, and is indistinguishable at the source
level from a call to any external service. No amount of import-graph rigour reaches it. The
class of violations that live in *behaviour* rather than in *structure* needs an observational
instrument, not a stricter rule.

The general shape: **structure is checkable statically; topology is only checkable at runtime.**
Anything expressed as a string at the call site — a URL, a queue name, a feature-flagged branch,
a dynamically resolved handler — is invisible to the compiler and visible to a trace.

## Deterministic scoring, interpretive model

The second transferable idea, and the sharper statement of a division of labour the repo argues
elsewhere:

> "The single most important decision … is that the agent does not compute the score … The
> arithmetic is deliberately simple … no model call anywhere in it."

| Layer | Job | Property that matters |
|---|---|---|
| **Deterministic scoring** | Compute a health number from violations, with published weights | Pure functions, reproducible, auditable — the same input always scores the same |
| **Model reasoning** | Interpret heterogeneous signals, explain what a violation would cost, state its own blind spots | Synthesis, not arithmetic |
| **Runtime observation** | Diff actual call graphs against source dependencies | Sees what neither of the above can |

His summary of the split is the line worth carrying: *"the tools found the violations while the
model made them mean something … explained what the violation would cost."*

The reason to keep models out of scoring is not accuracy but **governance**. A number that a
model produced cannot be reproduced, cannot be diffed across commits, and cannot be argued with
on its own terms — which disqualifies it as a gate even when it happens to be right. Confining
the model to explanation keeps the auditable part auditable while still getting the thing models
are actually good at.

## Relationship to other notes

- [Enforced Architecture Rules for Agents and Humans](enforced-architecture-rules.md) — **the
  pairing, and a genuine qualification.** That note argues for making violations unrepresentable
  in the import graph, and its case is strong for everything that *is* an import. This supplies
  the boundary: a class of coupling exists only while the system runs, so an unrepresentable-by-
  construction strategy is necessary and not sufficient. Read together, they say encode what you
  can statically, then observe for the rest.
- [Control and Complexity](../../concepts/control-and-complexity.md) — the theoretical form of
  the same finding, reached independently. Hebert objects that proposals to replace practices
  with automated barriers rarely ask "how static barriers may qualitatively differ from more
  adaptive ones". This is a concrete instance: the static barrier satisfied its stated purpose
  while the system's actual behaviour walked around it. Observing the running system is the
  complexity-side instrument.
- [Comprehension as an Architectural Characteristic](comprehension-as-architecture.md) — both
  treat an architectural property as something to measure rather than assert. That note supplies
  fitness functions for shared understanding; this one for stated-versus-actual topology.
- [Change Locality and Boundary Drift](change-locality.md) — boundary drift that a build gate
  cannot catch, because the crossing leaves no structural trace.
- [Netflix's Service Topology at Scale](../../case-studies/netflix-service-topology.md) — the
  same artefact (a runtime dependency graph from traces) built at scale for a different purpose:
  operational topology rather than conformance. Useful as evidence that the input this approach
  needs is buildable well beyond a demo.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — the premise
  they share: agent-speed change requires verification capacity to rise with it, since review
  throughput cannot.
