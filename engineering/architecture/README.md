---
type: index
title: Architecture
description: "Notes on software architecture, system design, and distributed systems."
tags: [meta, architecture, system-design]
status: complete
updated: 2026-06-20
---

# Architecture

Notes on software architecture, system design, and distributed systems.

**Start here:** [Architecture — Overview](overview.md) — a map of how these notes fit together.

## Notes

- [C4 Model](c4-model.md) — four-level architecture diagramming with PlantUML and Structurizr DSL examples
- [Composable Architecture](composable-architecture.md) — PBCs, API Gateway, BFF, User Journey API, GraphQL federation, DX and maintainability progression
- [Caching Reference Data APIs](caching-reference-data-apis.md) — cache patterns for slow-moving lookup data (long TTL + ETag, versioned datasets, Redis cache-aside, event invalidation, stale-while-revalidate) and a recommended enterprise topology
- [Agile Design Decisions and Principles](agile-design-decisions.md) — continuous design, reversibility and blast-radius frameworks, delegation, emergent architecture, technical debt
- [Architectural Decision Records (ADRs)](adr.md) — lightweight, version-controlled records of significant decisions
- [ADRs in an Agentic World](adrs-in-an-agentic-world.md) — how agentic coding shifts the ADR from a pre-authorisation gate to a post-exploration record: the Pareto flip, spikes-as-options, evidence over rhetoric, and agents drafting ADRs
- [Writing an Effective Design Doc](design-docs.md) — the design doc as an artifact: when it's worth writing, how much to invest, a selective component catalogue (goals/non-goals, scenarios, SLOs, alternatives considered, trust boundaries), and concrete practices; the larger up-front cousin of the ADR
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) — the design system as constraint layer and platform for AI-generated UI
- [Skeleton Architecture](skeleton-architecture.md) — structural guardrails for AI-generated code: an immutable human-designed skeleton (base classes, contracts, security context) constrains AI-generated tissue, enforced by the Template Method pattern, schema-first contracts, and compile-time topology checks (ArchUnit); the general-code sibling of the design-system control plane
- [Strangler Fig Pattern](strangler-fig.md) — incremental legacy modernisation behind a facade, without a big-bang rewrite
- [Architectural Change Cases](architectural-change-cases.md) — anticipating future change: structured change cases that extend ADRs forward, with t-shirt costs, fitness functions, and evolutionary-architecture framing
- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — a single-page tool for designing and validating micro-frontend boundaries before coding (business capability, boundaries, dependencies, communication, governance)
- [Domain-Driven Design: Strategic Design](ddd-strategic-design.md) — the problem-space theory: subdomains (core/supporting/generic), bounded contexts, ubiquitous language, the big ball of mud, and the eight context-mapping relationship patterns
- [Bounded Context Canvas](bounded-context-canvas.md) — the DDD domain/service-layer canvas for designing one bounded context (purpose, strategic classification, ubiquitous language, inbound/outbound communication, business decisions); the backend sibling of the micro-frontend canvas
- [Microfrontend Architecture Principles](micro-frontend-principles.md) — the principles a good microfrontend boundary must satisfy at scale (bounded contexts, team autonomy, explicit contracts, independent deployability, platform over governance, Conway's Law), with a pre-creation checklist
- [The Micro-Frontend Shell as Platform Runtime](microfrontend-shell-platform.md) — the host shell as a platform runtime, not a layout wrapper: the catalogue of shell-owned services (routing, session, entitlements, navigation, remote registry, config, telemetry, HTTP, …), the typed `ShellPlatform` contract, and what to keep *out* of the shell
- [Thin Shell + Platform Runtime Remote](thin-shell-platform-runtime.md) — the packaging variant: keep the shell a thin bootloader (kernel loader) and extract the platform services into a separately deployed runtime remote, with a versioned platform contract, startup sequence, and the distributed-monolith risk
- [Thin-Shell Startup Performance](thin-shell-startup-performance.md) — the performance trade-off of the extracted-runtime model: the startup waterfall, fat-vs-thin shell comparison, platform-core/deferred split, shared-singleton dependencies, prefetch-on-intent, and the critical-path target
- [Thinking in Constraints](thinking-in-constraints.md) — surfacing, classifying, and challenging the constraints that bound a solution; constraints as the architect's primary input
- [Over-Engineering Is Solving the Wrong Problem](over-engineering.md) — over-engineering reframed as a requirements failure rather than a design failure: enough constraints leave exactly one solution, internal libraries and tools are products too, and the diagnostic is asking why things are built the way they are
- [Enforced Architecture Rules for Agents and Humans](enforced-architecture-rules.md) — making violations fail the build instead of documenting them: package classification, layer rules, and annotation-based role rules as a three-tier hierarchy, with the escape routes closed so the constraint cannot be gamed — because markdown instructions do not bind an agent
- [Data Readiness for Agents](data-readiness-for-agents.md) — human scepticism was invisible labour in every data pipeline and agents supply none of it: data contracts with freshness keyed to successful refresh rather than content change, the domain/semantic/capability model split, "retrieved text informs, it never gates", and contract breaches overriding model confidence as the escalation gate — plus the lethal trifecta and EU AI Act logging duties
- [Runtime Architecture Verification](runtime-architecture-verification.md) — the limit on static enforcement: a synchronous HTTP call violating a publish-only rule passes every static check because a `fetch()` creates no module dependency, so conformance needs runtime call-graph diffing beside import rules — plus keeping scoring deterministic and confining the model to explaining what a violation costs *(partnered with Google Cloud — the GCP implementation is not carried here)*
- [Change Locality and Boundary Drift](change-locality.md) — the understanding needed for a change should be proportional to its scope; boundaries are provisional hypotheses that go stale as product, teams and platforms move, with excess cognitive load as the diagnostic rather than a design budget. Offload the toil, not the judgement
- [Comprehension as an Architectural Characteristic](comprehension-as-architecture.md) — shared understanding as a quality attribute that decays silently: Naur's *Programming as Theory Building* as the grounding, GenAI removing the comprehension that used to be a by-product of implementation, and concrete fitness functions (truck factor, Degree of Authorship, onboarding time) treated as investigation triggers rather than gates
- [Reversibility Decays](reversibility-decays.md) — two-way doors lock behind you: the exit cost of a decision only ever rises as dependencies accumulate, so optionality is a running cost rather than a property assessed once — and cheap regeneration collapses only the rebuild half of that cost, never the un-wiring half
- [Primitives Over Opinionated Frameworks](primitives-over-frameworks.md) — which dependencies to keep once implementation labour is cheap: retain unopinionated primitives, drop the opinion layer, own the thin layer between — plus the cases (accessibility-critical components, commodity UI, teams without agentic workflows) where that is the wrong call
- [Generative UI](generative-ui.md) — producing UI with AI at build time (generated components) and run time (LLM-assembled interfaces); patterns, the whitelisted component registry as safety boundary, risks, and when to use it
- [Event Storming](event-storming.md) — the collaborative DDD discovery workshop: the three levels (big picture → process → software design), the sticky-note grammar, and how clusters of domain events surface bounded contexts
- [Team Topologies and Socio-Technical Architecture](team-topologies.md) — Conway's Law and the inverse manoeuvre, the four team types, three interaction modes, cognitive load and fracture planes
