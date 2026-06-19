---
title: Microfrontend Architecture Principles
tags: [architecture, system-design, microservices]
topic: engineering/architecture
status: draft
level: intermediate
related:
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/architecture/composable-architecture.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/thinking-in-constraints.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/software-design-principles.md
  - concepts/clean-code-and-solid.md
  - engineering/architecture/bounded-context-canvas.md
updated: 2026-06-19
---

# Microfrontend Architecture Principles

The Single Responsibility Principle is a fine starting point, but at scale a
microfrontend program succeeds or fails on a handful of *architectural* principles
that determine whether it accelerates delivery or becomes a distributed monolith.
Where [The Micro-Frontend Canvas](micro-frontend-canvas.md) is the *tool* for
deciding one boundary, these are the *principles* a good boundary must satisfy.

At this scale, bounded contexts, explicit contracts, and team ownership do more
for maintainability than strict adherence to all five SOLID principles. SOLID and
the other [code-level design principles](../practices/software-design-principles.md)
support the architecture; they do not drive it.

## The principles

1. **Bounded contexts (most important).** Borrowed from Domain-Driven Design: a
   microfrontend should own a **business capability**, not a technical slice.
   `Payments`, `Accounts`, `Home Loans` — not `Header`, `Table`, `Form`, `Button`.
   A useful rule: *if a Product Owner can describe it, it can probably be a
   microfrontend.*

2. **Team autonomy.** One team should build, test, deploy, and monitor its
   microfrontend independently. If deploying Payments requires a shell change, then
   a shared-library change, then a platform release, it is not autonomous. The
   platform should provide guardrails, not dependencies.

3. **Explicit contracts.** Microfrontends communicate through contracts, not
   implementation details. Publish typed interfaces (a `UserContext`, a
   `NavigationProvider`); never reach into `window.someInternalState` or
   `import { internalStore } from "another-mfe"`. **Treat other MFEs like external
   systems.**

4. **Loose coupling.** One MFE should not know how another works internally. Depend
   on a *published contract*, not on another MFE's code. Fewer inter-MFE
   dependencies means teams move more independently.

5. **High cohesion.** Everything inside a microfrontend should belong together —
   payment screens, payment validation, payment APIs in `Payments`; not payments
   *and* notifications *and* customer profile *and* settings. This is where SRP
   applies, at the domain level.

6. **Shared-nothing by default.** Over-sharing is one of the biggest mistakes:
   shared component / state / utility / API / hooks / business-logic libraries
   until *everything* is shared. Share only the genuinely cross-cutting:
   **design system, authentication, platform services, infrastructure.**
   Everything else stays local until duplication becomes painful.

7. **Consumer-driven evolution.** Changes must not break consumers. Don't rename
   `User.id` to `User.customerId` and break every MFE — add `customerId?` alongside
   `id` and evolve the contract gradually. Version contracts; deprecate, don't
   delete.

8. **Consistent user experience.** The architecture must be invisible to users —
   no Team A / Team B / Team C visual seams. Shared elements typically include
   navigation, the design system, typography, spacing, accessibility, and
   authentication. (This is the usual argument for **shell-owned navigation** in
   large organisations.)

9. **Independent deployability.** The principle that usually *justifies*
   microfrontends. The test: *can the Payments team deploy today without
   coordinating with any other team?* If not, you likely have a distributed
   monolith — investigate why.

10. **Minimise cross-team coordination.** Optimise for organisational scalability.
    If every change needs the Accounts, Payments, Platform, and Architecture teams,
    it will grind to a halt. Design interfaces so most decisions stay inside one
    team.

11. **Platform over governance.** Prefer paved roads to committees: *make the right
    thing easy and the wrong thing hard.* Shared CI/CD templates, design-system
    packages, security and observability SDKs, MFE starter kits, architecture
    linting. Teams follow standards because it is easier, not because they were
    told to.

12. **Conway's Law alignment.** Systems mirror the organisations that build them.
    If the org has Accounts, Payments, and Customer teams, the microfrontends
    should likely mirror those domains. *If your architecture fights your org
    structure, the org usually wins* — team boundaries are an architectural
    [constraint](thinking-in-constraints.md), not a detail.

## A pre-creation checklist

Before creating a new microfrontend, ask:

1. Does it represent a **business capability**?
2. Can a **single team** own it end-to-end?
3. Can it be **deployed independently**?
4. Does it expose **explicit contracts**?
5. Can it **evolve without breaking consumers**?
6. Is it **highly cohesive**?
7. Does it **minimise cross-team coordination**?
8. Would a **user** recognise it as a meaningful area of the product?

If most answers are "yes", it is probably a good boundary.

## Prioritising at scale

The principles are not equally weighted. For a large organisation — say a bank with
10–20 delivery teams — the ones that most determine success are, in order:

1. Bounded contexts
2. Team autonomy
3. Explicit contracts
4. Independent deployability
5. Platform over governance
6. Consistent user experience
7. Loose coupling

These seven tend to decide whether a microfrontend program accelerates delivery or
collapses into a distributed monolith. The remaining principles matter, but they
are largely *consequences* of getting these right.

## Relationship to other notes

- [The Micro-Frontend Canvas](micro-frontend-canvas.md) — the design tool that
  operationalises these principles for a single boundary (business capability,
  contracts, shared dependencies, governance).
- [Composable Architecture](composable-architecture.md) — the paradigm (packaged
  business capabilities, BFF) these boundaries are composed within.
- [Design Systems as the AI Control Plane](design-systems-ai-control-plane.md) —
  the shared design system that delivers principle 8, and the embodiment of
  "platform over governance" (principle 11).
- [Thinking in Constraints](thinking-in-constraints.md) — Conway's Law as the
  organisational constraint that bounds viable boundaries (principle 12).
- [Modern Web Engineering Playbook](../practices/engineering-playbook.md) — the
  wider web-engineering context for microfrontends and BFFs.
