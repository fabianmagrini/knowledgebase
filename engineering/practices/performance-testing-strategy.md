---
title: Performance Testing Strategy
tags: [testing, performance, observability]
topic: engineering/practices
status: notes
related:
  - engineering/architecture/composable-architecture.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/release-confidence.md
  - concepts/resilient-software-design.md
  - tools/containers/postgresql-ha-kubernetes.md
  - case-studies/linear-performance-architecture.md
  - engineering/architecture/thin-shell-startup-performance.md
source: "https://gist.github.com/fabianmagrini/dbf422910023dc8460f1331dd27c6f21"
updated: 2026-06-20
---

# Performance Testing Strategy

Flat load tests against isolated endpoints don't reveal how a distributed system behaves
under real use. Effective performance testing is **layered and system-aware**: it mirrors
real user journeys and real failure modes, and it measures each tier where it actually
breaks.

## Define metrics first

Decide what "fast enough" means before testing, on two axes:

- **User-centric** — page load (LCP), interaction latency (INP), layout stability (CLS),
  navigation/transition time, error rates. These are what users feel.
- **System-centric** — P95/P99 latency, throughput (RPS), saturation (CPU, memory,
  connections), and queue depth / work-loop lag. These are what infrastructure feels.

Tie targets to percentiles, not averages — the tail is the experience.

## Test layer by layer

| Layer | What to test | Key tactic |
|---|---|---|
| **UI / composition** | Bundle size, time-to-mount, render cost | Test the *composed* page (shell + multiple components), not parts in isolation — interference only shows when they run together |
| **Aggregation tier** (BFF / gateway) | Fan-out latency, serialization cost, work-loop blocking | Test **fan-out amplification**: one user request can trigger many downstream calls — this tier is the usual choke point |
| **Services** | DB latency, N+1 queries, cache effectiveness, circuit breakers | Add **failure injection**: timeouts, 5xx, retry storms, cascading failure |
| **End-to-end** | Real journeys (login → browse → search → checkout) | Drive whole flows, not endpoints at arbitrary RPS |

## Use realistic traffic shapes

- **Ramp-up** — exposes cold-start behaviour.
- **Steady state** — the baseline.
- **Spike** — sudden bursts; tests elasticity and shedding.
- **Soak** — hours of load; surfaces memory leaks and slow degradation.

Shape the mix too: realistic read/write split (e.g. 80/20), hot endpoints vs. cold paths,
and geographic latency if the system is global.

## Observability is a prerequisite

You cannot tune what you cannot see. **Distributed tracing** across the whole request path
(UI → aggregation → services) is what turns "it's slow" into "this hop is slow." Metrics +
traces + a dashboard are part of the test rig, not an afterthought.

## Shift left — bake it into CI/CD

| Stage | Check |
|---|---|
| **PR** | Bundle-size budgets, micro-benchmarks |
| **Pre-merge** | Component-level load tests |
| **Pre-prod** | Full-system load test |
| **Post-deploy** | Synthetic monitoring |

A budget that fails the build stops regressions cheaply; a perf test run only before release
finds them too late.

## Applied: MFE + BFF + NestJS on Kubernetes

Concretely, for the [composable architecture](../architecture/composable-architecture.md)
stack (React microfrontends, a Node/TypeScript BFF, NestJS services, on Kubernetes):

- **Microfrontends** — measure bundle size and time-to-mount per MFE, but load-test the
  **shell composing several MFEs** at once. Tools: Lighthouse, WebPageTest.
- **BFF** — the prime suspect. Test **1 request → 5–20 downstream calls** fan-out;
  instrument **Node event-loop lag** under aggregation load. Tools: k6, Artillery; profile
  with Clinic.js / 0x.
- **NestJS services** — hunt N+1 queries, validate caching and circuit-breaker behaviour;
  inject timeouts/500s/retry storms. Chaos: Chaos Mesh, Gremlin.
- **Journeys** — Playwright (with load extensions) or k6 browser mode for real flows.
- **Kubernetes** — set resource **requests/limits** correctly: **CPU throttling causes
  latency spikes even at moderate utilization**. Test HPA scale-up latency and watch for
  thrashing; measure pod cold-start and readiness/liveness probe impact.
- **Tracing** — OpenTelemetry → Jaeger, with Prometheus + Grafana for system metrics.
