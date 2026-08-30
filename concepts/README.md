---
type: index
title: Concepts
description: "Foundational concepts — CS fundamentals (algorithms, data structures, complexity, networking) and the underlying ideas that practice notes build on."
tags: [meta, ci-cd]
status: complete
updated: 2026-06-20
---

# Concepts

Foundational concepts — CS fundamentals (algorithms, data structures, complexity,
networking) and the underlying ideas that practice notes build on.

## Notes

- [CI vs Continuous Delivery vs Continuous Deployment](ci-cd-continuous-deployment.md) — the three-way distinction by what each one automates, and why a team might stop at Continuous Delivery
- [Clean Code and SOLID](clean-code-and-solid.md) — the hierarchy (Craftsmanship → Clean Code → SOLID), the five principles, and the modern over-abstraction caution
- [Control Plane and Data Plane](control-plane-data-plane.md) — the distinction several notes here borrow without defining: the data plane is the capability, the control plane is the bookkeeping that reconciles desired against actual state; static stability, cells and blast radius, and why GitOps is a control plane
- [Constraints as a Lens](constraints-as-a-lens.md) — hub unifying the three constraint senses (throughput, structure, selection)
- [Continuous Delivery](continuous-delivery.md)
- [Control and Complexity](control-and-complexity.md) — two incompatible philosophies of systems design (decomposition and control versus complexity and emergence), the table showing how the same practice serves different purposes under each, and hidden adaptations as the thing that vanishes when a control is automated away
- [The DevOps Capability Model (Accelerate / DORA)](devops-capability-model.md) — the 24 capabilities across 5 categories and the four delivery metrics; the canonical DORA/Accelerate reference
- [Optimal Stopping and the 37% Rule](optimal-stopping.md) — the secretary problem: sample 37% (1/e) without committing, then take the first option beating the benchmark; the assumptions it needs, why the popular hiring application is its weakest, and its durable value as a prior against both endless deliberation and premature commitment
- [Progressive Delivery](progressive-delivery.md) — extending continuous delivery with gradual, measured exposure (canary, blue-green, ring, flag rollout) gated on telemetry
- [Resilient Software Design](resilient-software-design.md) — why distributed systems demand designing for failure: failure modes, FLP/consensus, graceful degradation
- [Theory of Constraints](theory-of-constraints.md)
