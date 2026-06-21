---
title: GitOps
tags: [ci-cd, git, observability, security]
topic: engineering/practices
status: notes
level: intermediate
related:
  - concepts/continuous-delivery.md
  - concepts/ci-cd-continuous-deployment.md
  - concepts/progressive-delivery.md
  - engineering/practices/trunk-based-development.md
  - concepts/devops-capability-model.md
  - concepts/resilient-software-design.md
  - engineering/practices/rollback-and-roll-forward.md
  - engineering/practices/database-migration-strategies.md
  - tools/git.md
source: "Weaveworks / Alexis Richardson — GitOps (2017); OpenGitOps (CNCF) — https://opengitops.dev"
updated: 2026-06-21
---

# GitOps

GitOps is an operating model for delivery and infrastructure in which **a Git
repository is the single source of truth for the desired state of a system, and an
automated agent continuously reconciles the running system to match it.** You don't
push changes *to* an environment; you change the declared state in Git, and a
controller pulls and converges the environment toward it.

Coined by Weaveworks (Alexis Richardson) in 2017 and now stewarded as the CNCF
**OpenGitOps** project, it is best understood as a concrete implementation of
[continuous delivery](../../concepts/continuous-delivery.md) for declarative
systems — Kubernetes most of all — where the "deploy" step becomes a reconciliation
loop rather than a scripted push.

## The four principles (OpenGitOps)

1. **Declarative** — the entire system is described declaratively (desired state,
   not the steps to get there).
2. **Versioned and immutable** — that desired state is stored in Git, giving an
   immutable, append-only history with full audit trail.
3. **Pulled automatically** — software agents pull the declared state from Git;
   credentials live in the cluster, not in a CI server pushing inward.
4. **Continuously reconciled** — agents constantly observe actual state, detect
   **drift** from desired state, and converge — self-healing against manual
   tampering or partial failures.

## The reconciliation loop

GitOps is a closed control loop, the same shape as
[progressive delivery](../../concepts/progressive-delivery.md)'s observe-and-promote:

```text
desired state in Git  ──pull──▶  agent compares  ──diff?──▶  apply to converge
        ▲                              │                          │
        └────── git commit/revert ─────┘      actual cluster state ┘
                                              (continuously observed)
```

Because the agent watches *actual* state, GitOps corrects **drift** — someone
`kubectl edit`s a resource by hand and the controller reverts it to what Git says.
The repository is not just a deployment trigger; it is a continuously enforced
contract.

## Push vs pull delivery

The defining GitOps choice is the **pull model**, which contrasts with the
traditional push pipeline:

| | Push (classic CI/CD) | Pull (GitOps) |
|---|---|---|
| Who applies the change | CI job runs `kubectl apply` / `terraform apply` | In-cluster agent pulls and applies |
| Where credentials live | In the CI system (broad, outward-facing) | In the cluster (scoped, never leaves) |
| Drift detection | None — fire-and-forget | Continuous reconciliation |
| Source of truth | The pipeline run | The Git repository |

The pull model is the security argument for GitOps: the CI system never needs
production cluster credentials, shrinking the blast radius of a compromised
pipeline.

## Why it matters

- **Rollback is `git revert`.** Recovering a bad change is a version-control
  operation with a known-good prior state, not a frantic manual fix — a direct lift
  to the [DORA](../../concepts/devops-capability-model.md) *time to restore* metric.
- **Auditability for free.** Every change to production is a reviewed, attributable
  commit. This is why GitOps fits regulated and high-risk contexts well.
- **Disaster recovery.** The cluster can be rebuilt from the repository; the
  declared state *is* the backup. A form of designing for failure — see
  [Resilient Software Design](../../concepts/resilient-software-design.md).
- **Consistency at scale.** Many clusters/environments reconcile against the same
  declared state, eliminating snowflake drift.

## Tooling

The dominant Kubernetes-native controllers are **Argo CD** (UI-forward, app-centric)
and **Flux** (CNCF-graduated, composable, GitOps Toolkit). Both implement the pull
loop; both pair with progressive-delivery controllers (Argo Rollouts, Flagger) so a
reconciled change can also roll out gradually. **Terraform / OpenTofu** bring a
GitOps-adjacent model to broader infrastructure, though classic Terraform pipelines
are often push-based.

## Caveats

- **It assumes declarative targets.** GitOps shines for Kubernetes and IaC; it fits
  awkwardly around imperative or stateful steps (one-off migrations, data
  backfills) that don't reduce to a desired-state document.
- **Secrets need a strategy.** Plaintext secrets must never sit in Git; GitOps
  relies on sealed secrets, external secret operators, or a vault the agent reads
  from.
- **Repository structure is a real design problem.** App-of-apps, per-environment
  branches vs directories, and monorepo-vs-polyrepo layout all have trade-offs that
  compound as the fleet grows.

## Relationship to other notes

- [Continuous Delivery](../../concepts/continuous-delivery.md) and
  [Continuous Deployment](../../concepts/ci-cd-continuous-deployment.md) — GitOps is
  one *implementation* of these for declarative systems; "keep everything in version
  control" and "deploy is automated" are CD principles GitOps makes literal.
- [Progressive Delivery](../../concepts/progressive-delivery.md) — the reconciliation
  loop and the exposure-control loop compose: reconcile the new state in, then widen
  exposure under telemetry.
- [Trunk-Based Development](trunk-based-development.md) — the same "Git is the
  integration point" discipline extended from application code to infrastructure and
  configuration.
