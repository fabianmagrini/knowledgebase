---
title: Composable Architecture
tags: [architecture, microservices, system-design, api-design]
topic: engineering/architecture
status: notes
updated: 2026-06-20
related:
  - engineering/practices/engineering-playbook.md
  - engineering/architecture/c4-model.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/strangler-fig.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/architecture/team-topologies.md
  - engineering/architecture/micro-frontend-canvas.md
  - engineering/architecture/generative-ui.md
  - engineering/architecture/micro-frontend-principles.md
  - engineering/architecture/bounded-context-canvas.md
  - engineering/architecture/ddd-strategic-design.md
  - concepts/resilient-software-design.md
  - tools/containers/dynamic-configuration-sidecar.md
source: "https://gist.github.com/fabianmagrini/3b93d3db8189f663053489dd554d311d"
---

# Composable Architecture

An architectural paradigm where applications are assembled from independent, interchangeable, and reusable components — **Packaged Business Capabilities (PBCs)**. Each PBC delivers a specific business function (shopping cart, payment gateway, authentication) and can be developed, deployed, and scaled independently.

> "Building with Lego blocks" — not just a metaphor. Modularity at the component level enables flexibility at the business level.

## Core principles

| Principle | Description |
|---|---|
| **Modularity** | Break the application into independent, well-defined components. Each does one thing well. |
| **Autonomy** | Components are self-contained. Updates or replacements don't ripple through the system. |
| **Discoverability** | A catalog or registry makes available capabilities findable, preventing duplication. |

## Benefits

- **Agility** — add or replace capabilities without touching the whole system
- **Independent scaling** — scale the payment service during peak checkout without scaling everything
- **Fault isolation** — failure in one component doesn't cascade
- **Vendor freedom** — best-of-breed choices per capability; no single-vendor lock-in
- **Faster delivery** — reuse pre-built PBCs to accelerate new features

## Challenges

- Distributed system complexity: service discovery, inter-service communication, health monitoring
- Governance and API standardisation are mandatory — without them you get integration chaos
- Data consistency across services is hard (each service owns its data)
- Orchestration of business workflows that span multiple services

## Architecture layers

A mature composable system has distinct layers with clear, non-overlapping responsibilities.

### API Gateway

The single entry point for all clients. Handles **technical/infrastructure concerns only**.

Responsibilities:
- Authentication and authorisation (token validation)
- Rate limiting and traffic shaping
- Routing to the correct downstream service
- Logging and security scanning

The gateway must never contain business logic. Pushing orchestration into a gateway creates a bottleneck and buries business rules in infrastructure config that is hard to test.

### BFF / Experience API

A dedicated backend-for-frontend, one per client type (mobile app, web app, kiosk). Handles **experience-specific aggregation**.

Responsibilities:
- Aggregate data from multiple microservices into a single client-optimised payload
- Transform data shapes for the specific UI
- Insulate the client from backend refactoring

Without a BFF, the frontend must make multiple sequential calls and stitch the responses — high latency, fragile, and coupled to internal service structure.

### User Journey API (Orchestration Service)

A dedicated service per business workflow (checkout, loan application, onboarding). Handles **business process orchestration**.

Responsibilities:
- Execute multi-step workflows in the correct sequence
- Own the business rules of the workflow (not the core domain logic)
- Handle errors and compensating actions within the flow

Contrast with the BFF: the BFF knows *what a client needs*; the Journey API knows *how a business process works*.

### Relationship between the layers

```
Client
  └─► API Gateway (auth, routing)
        └─► BFF / Experience API (aggregation, client-tailored shape)
              └─► User Journey API (workflow orchestration)
                    └─► Core Microservices (single-domain business logic)
```

The layers are not always all required. Start simple; add layers when you feel specific pain.

| Scenario | Architecture |
|---|---|
| Simple journeys, few clients | `Gateway → BFF → Microservices` (BFF handles light orchestration) |
| Complex reusable journeys | `Gateway → BFF → Journey API → Microservices` |
| Omnichannel or API-as-product | `Gateway → Journey API → Microservices` (no BFF; journey is the product) |

**Triggers to add a Journey API:**
1. **Reusability** — same workflow needed by multiple BFFs (copy-paste is the warning sign)
2. **Complexity overload** — BFF is becoming a mini-monolith, mixing UI and workflow logic
3. **Conway's Law** — separate teams own the experience vs. the business process; align the architecture to the teams

## Shared services: what to share and what not to

The DRY instinct to share common code conflicts directly with the autonomy principle. Sharing the wrong things creates a **distributed monolith** — all the complexity of distributed systems with none of the independence.

### Safe to share (technical utilities, no business logic)

- Logging libraries
- Observability/tracing clients
- Security/auth client configuration
- Internal platform SDKs

### Never share

| Anti-pattern | Why it breaks composability |
|---|---|
| Shared business logic library | A change forces redeployment of all consumers — the same problem as a monolith |
| Shared domain model (e.g. `Customer` object across services) | Creates hidden coupling; schema changes cascade |
| Shared database tables | Prevents independent scaling; schema changes break multiple services; directly causes a distributed monolith |

If multiple services need the same business capability, the correct answer is: **make it a dedicated service (PBC)**, not a shared library. If that feels like overkill, embrace deliberate duplication rather than a wrong abstraction.

## UX Design System

The front-end equivalent of backend PBCs. Provides reusable UI components ("atoms" to "organisms") that mirror the modularity of the backend.

- Prevents UI rot when design language evolves — update design tokens once, propagate everywhere
- Creates a shared vocabulary between designers and developers
- Enables parallel team work: each team builds their module knowing it will compose correctly

Attempting composable architecture without a design system leads to consistent backend flexibility and chaotic, inconsistent frontend.

## GraphQL as the aggregation layer

GraphQL doesn't replace the *need* for an aggregation layer — it provides a standardised technology for implementing one.

A federated GraphQL server effectively *is* a BFF, but more powerful:
- Clients shape their own response — no over-fetching or under-fetching
- Schema additions are non-breaking; clients opt in to new fields
- One endpoint (`/graphql`) replaces dozens of BFF endpoints

**Apollo Federation pattern:**
```
Client
  └─► API Gateway (auth, basic routing)
        └─► Federated GraphQL Gateway (unified schema, aggregation)
              ├─► UserService (GraphQL subgraph)
              ├─► ProductService (GraphQL subgraph)
              └─► CheckoutJourneyAPI (REST, called via mutation resolver)
```

User Journey APIs remain essential in a GraphQL world: complex mutations (e.g. `checkout`) delegate to a dedicated Journey API rather than embedding orchestration logic in a resolver.

**Gateway implications with GraphQL:**
- Routing is trivial (everything goes to `/graphql`)
- Authorization moves inside the schema (per-field/per-type)
- Caching requires specialised strategies (HTTP-level caching no longer works simply)
- Query complexity analysis is needed to prevent expensive queries

## Developer experience progression

| Stage | Frontend DX | Backend DX |
|---|---|---|
| Monolith | Tight coupling; fear of change | High risk of breaking other teams |
| Basic microservices | API chaos; multiple calls to stitch | Improved autonomy but can bottleneck UI teams |
| + BFF | Tailored API; simple client logic | Core services insulated from UI churn |
| + Journey API | BFF offloads complex business flows | Clear process ownership; reusable across teams |
| + Federated GraphQL | Ultimate flexibility; client shapes its own query | Teams expose capabilities to the graph independently |

## Maintainability: building for change

Each layer is a firebreak — it absorbs a category of change and stops it spreading.

| Layer | What change it absorbs |
|---|---|
| Composable services | Replace/rewrite one service in any technology without touching others |
| Design system | Rebrand or update UI language in one place; propagates everywhere |
| API Gateway | Switch auth provider or security policy without touching microservices |
| BFF | Completely refactor backend; frontend requires zero changes |
| Journey API | Business rule changes are contained; not duplicated across BFFs |
| GraphQL schema | Additive changes are non-breaking; backend and frontend evolve independently |
