---
title: Architecture
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
- [Agile Design Decisions and Principles](agile-design-decisions.md) — continuous design, reversibility and blast-radius frameworks, delegation, emergent architecture, technical debt
- [Architectural Decision Records (ADRs)](adr.md) — lightweight, version-controlled records of significant decisions
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) — the design system as constraint layer and platform for AI-generated UI
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
- [Generative UI](generative-ui.md) — producing UI with AI at build time (generated components) and run time (LLM-assembled interfaces); patterns, the whitelisted component registry as safety boundary, risks, and when to use it
- [Event Storming](event-storming.md) — the collaborative DDD discovery workshop: the three levels (big picture → process → software design), the sticky-note grammar, and how clusters of domain events surface bounded contexts
- [Team Topologies and Socio-Technical Architecture](team-topologies.md) — Conway's Law and the inverse manoeuvre, the four team types, three interaction modes, cognitive load and fracture planes
