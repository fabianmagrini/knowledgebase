---
title: Managed Disruption
tags: [architecture, ci-cd, refactoring, decision-making]
topic: leadership
status: notes
related:
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/ci-cd-ai-engineering.md
  - leadership/protecting-mavericks.md
  - leadership/start-with-why.md
  - engineering/architecture/strangler-fig.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - concepts/theory-of-constraints.md
  - sre/incident-swarming.md
  - product/explore-vs-exploit.md
source: "https://gist.github.com/fabianmagrini/8d7a465df449ea54881c86f563ec6f6d"
updated: 2026-06-20
---

# Managed Disruption

**Managed disruption** is the intentional, structured introduction of innovation and
change into delivery work — while preserving stability, security, and compliance. It is
the discipline of evolving a regulated, legacy-heavy estate *from within delivery teams*
rather than freezing it or rewriting it big-bang.

> Planned, structured, and supported change that deliberately interrupts delivery flow to
> drive necessary evolution — without causing chaos.

It matters most in environments with heavy regulation, mission-critical legacy platforms,
high change-failure costs, and long-lived teams optimised for predictable throughput
(e.g. banking). The goal is to make disruption **expected, communicated, and supported**
rather than ad-hoc and destabilising.

## Why it exists

- Regulatory obligations make uncontrolled change expensive and risky.
- "Zombie" legacy platforms carry significant technical debt but cannot simply be paused.
- Teams must still modernise — cloud, APIs, AI, real-time payments — while delivering.
- Ad-hoc disruption breaks delivery flow and raises operational risk.

Managed disruption resolves this by treating change as a first-class, planned initiative
with guardrails, not a surprise.

## What it looks like for an engineer

| Type | Example | How it's managed |
|---|---|---|
| Technical upgrade | New build system, language version, framework refactor | Cross-team initiative with scope, timeline, feature flags, canary releases |
| Security / regulatory | New authentication flow to meet updated standards | Phased delivery coordinated with InfoSec and Compliance |
| Platform / tooling | Migrate CI/CD, adopt containerisation | Enablement team with support and rollback paths |
| Innovation / experiment | Trial AI pair programming, new APIs | Time-boxed spikes with success criteria and minimal blast radius |

The engineer's role is to be a **change agent within the team**: translating high-level
initiatives into sprint-sized tasks, introducing change safely (feature toggles, parallel
runs, dark launches, observability), adopting incrementally rather than big-bang, and
surfacing risk early.

## Enabling mechanisms

- Technical roadmaps and architecture review boards
- Innovation sprints / "platform enablement weeks"
- Tiger teams and guilds to lead change across teams
- Feature flags and shadow traffic to isolate impact

## Related techniques

Managed disruption is one label for the broader goal of balancing innovation with
stability. Adjacent approaches, by primary focus:

| Technique | Primary focus | Pace | Risk profile | Best for |
|---|---|---|---|---|
| **Managed Disruption** | Blending innovation within core teams | Deliberate, strategic | Moderate, controlled | Evolving core products safely |
| **Bimodal IT** | Org structure (Gartner) | Two-speed | Segregated (low Mode 1 / high Mode 2) | Protecting legacy while building new digital offerings |
| **Organizational Ambidexterity** | Business strategy | Parallel exploit + explore | Balanced | Sustaining present while exploring future |
| **Strangler Fig Pattern** | Technical architecture | Incremental, long-term | Low, carefully managed | Replacing critical legacy piece by piece |
| **DevSecOps** | Process & automation | Continuous, rapid | Low (automated guardrails) | Fast, secure, reliable delivery for any team |
| **Continuous Improvement (Kaizen)** | Cultural / process efficiency | Small, constant | Very low | Optimising existing workflows |
| **Innovation Labs / Skunkworks** | Isolated R&D | Rapid experimentation | High but isolated | Exploring breakthroughs without risking the core |
| **Intrapreneurship** | Cultural mindset | Variable | Variable | Empowering individuals as agents of change |

**Key distinction:** managed disruption innovates *inside* core delivery teams. Bimodal IT
and Innovation Labs deliberately *separate* innovation from delivery — which avoids
destabilising the core but creates a reintegration problem managed disruption sidesteps.
The Strangler Fig Pattern is the canonical *architectural* expression of the philosophy;
DevSecOps is the *how* (automated guardrails) that makes the "disruption" safe enough to
be "managed".

## Example

> A bank migrates all payment APIs from SOAP to REST. Instead of forcing every team to
> drop their work, it runs a managed-disruption programme: a platform team ships the new
> REST endpoints and tooling; delivery teams get a migration schedule three months ahead;
> engineers integrate the new client libraries behind feature flags and test in lower
> environments; rollout is phased with observability and defined rollback. No
> firefighting — a structured initiative with support.

## Notes / open questions

- "Managed disruption" lacks a clear single origin the way Bimodal IT (Gartner) does. It
  reads as a synthesised label rather than established industry vocabulary — treat the term
  as descriptive, not canonical.
