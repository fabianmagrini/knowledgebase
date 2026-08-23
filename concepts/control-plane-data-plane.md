---
type: note
title: Control Plane and Data Plane
description: "The distinction several notes here borrow without defining: the data plane is the capability, the control plane is the bookkeeping that reconciles desired against actual state — and static stability is what keeps one failing from breaking the other."
tags: [architecture, system-design, observability, reading]
topic: concepts
status: notes
level: intermediate
related:
  - engineering/practices/gitops.md
  - concepts/resilient-software-design.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - case-studies/netflix-service-topology.md
  - case-studies/zalando-client-side-load-balancing.md
  - tools/dynamic-configuration-sidecar.md
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/rootly-pr-size-risk-labels.md
source: "https://www.allthingsdistributed.com/2026/08/on-building-scalable-control-planes.html"
updated: 2026-08-23
---

# Control Plane and Data Plane

Zak van der Merwe (AWS, August 2026) on building control planes at scale. Recorded here
because **several notes in this repo borrow "control plane" as a metaphor without the original
concept being written down** — [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md),
[Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md),
[The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md)
and others. This is what they are borrowing from.

An experience report, and partly an argument for AWS's DSQL — the architectural principles
hold independently of that, but the framing is not disinterested.

## The distinction

> The data plane is the set of core capabilities, the raw computing power, the hardware, the
> networking. **The control plane is the conduit between those capabilities and customers.**

| | Does |
|---|---|
| **Data plane** | The actual work — serving requests, running the container, moving the packets |
| **Control plane** | The **bookkeeping layer**: accepts intent, tracks desired versus actual state, and drives the data plane toward the desired one |

Launching an EC2 instance is a control-plane operation; the instance running your code is the
data plane. The asymmetry that follows is the important part: **the data plane runs constantly,
the control plane is touched only when something changes.**

## Static stability

The principle with the most carrying power, and not otherwise recorded in these notes:

> Running workloads must remain operational **regardless of control plane failures**.

This is a stronger claim than graceful degradation in
[Resilient Software Design](resilient-software-design.md). Degradation says the system should
survive failure in reduced form; static stability says an existing workload should not notice
at all. You may be unable to *launch* new instances while the control plane is down; the ones
already running must keep serving.

The design consequence is that the data plane must not depend on the control plane **at
request time**. Anything the data plane needs has to be pushed to it in advance, so that a
control-plane outage removes the ability to *change* things without removing the ability to
*run* them.

That failure separation is what makes the metaphor apt when this repo applies it to
AI-generated code: a design system or CI pipeline acting as a control plane should constrain
what gets built without being in the path of what already works.

## The thermostat, and why GitOps is a control plane

The described mechanism is a continuous loop: observe actual state, compare to desired state,
reconcile the difference. A thermostat.

That is exactly the model in [GitOps](../engineering/practices/gitops.md) — a declarative
desired state in Git, and an agent continuously reconciling the running system to match it.
Neither note previously said so, but **GitOps is a control plane**, with the repository as the
intent store and the operator as the reconciliation loop. Reading them together explains why
GitOps behaves the way it does under failure: if the reconciler stops, the cluster keeps
running whatever it was already running. Static stability, arrived at by a different route.

## Scaling one: the EC2 progression

The concrete arc, as reported — EC2 hosts grew from hundreds to millions, and the control plane
was scaled in stages:

1. A **MySQL primary with a hot standby**
2. **Read replicas** to absorb query load
3. **Sharding** into availability zones and **cells**

Cells are the blast-radius mechanism: partition the control plane so that a failure affects one
cell rather than the fleet. That term appears throughout this repo's AI case studies —
[Cloudflare](../case-studies/cloudflare-ai-code-review.md),
[Rootly](../case-studies/rootly-pr-size-risk-labels.md) — as a review-risk concept; this is the
infrastructure practice it was taken from.

He also names **"fire storms"** — cascading failure across a control plane, where recovery work
generates more load than the steady state, which is why blast-radius partitioning matters more
than raw capacity.

## Self-hosting

Run the control plane **on the service it controls**. The argument is that it surfaces rough
edges early: if your own team cannot operate comfortably on the primitives you ship, customers
will not either. The cost is a bootstrapping problem and a correlated-failure risk, which the
piece does not dwell on.

## The DSQL argument, and its stated limits

The through-line is that a database handling scaling, availability and consistency
automatically removes most of the work above — no manual sharding, no read-replica management,
"thousands of databases" managed automatically, Firecracker micro-VMs per connection.

The caveats are given honestly and are worth keeping alongside the claim:

- Foreign keys still under development
- **Single-node Postgres has lower latency** than a multi-zone architecture — distribution has
  a floor
- Migrating EC2's control plane would take **years**, so the advice is for new systems
- Speculative sharding adds time-to-market risk, which is the argument *for* deferring it

## Relationship to other notes

- [GitOps](../engineering/practices/gitops.md) — the reconciliation loop as a delivery
  practice; this note is the general form it instantiates.
- [Resilient Software Design](resilient-software-design.md) — failure modes and graceful
  degradation; static stability is the stricter sibling, and specific to the control/data split.
- [CI/CD as the Control Plane](../engineering/ai-native/ci-cd-ai-engineering.md),
  [Design Systems as the AI Control Plane](../engineering/architecture/design-systems-ai-control-plane.md),
  [The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md)
  — the three notes that borrow this vocabulary. The borrowing is sound: each describes a layer
  that governs what enters a system without performing the system's actual work.
- [Netflix's Service Topology](../case-studies/netflix-service-topology.md) and
  [Zalando's Client-Side Load Balancing](../case-studies/zalando-client-side-load-balancing.md)
  — production systems where the control/data split is doing visible work.
