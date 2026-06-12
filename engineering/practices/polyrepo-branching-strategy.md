---
title: Polyrepo Branching Strategy
tags: [git, microservices, ci-cd, distributed-systems]
topic: engineering/practices
status: notes
updated: 2026-06-11
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/federated-pr-review.md
  - tools/git.md
---

# Polyrepo Branching Strategy

Use **trunk-based development per repo**, with **release branches only where needed**, and coordinate cross-repo change through **contracts, feature flags, and progressive rollout** rather than long-lived shared branches.

## 1. Default: trunk-based per service repo

Each microservice repo has:

```text
main
  ├── short-lived feature branches
  ├── release/v1.42.x   optional
  └── hotfix/v1.42.3    optional
```

| Branch      | Purpose                                                          |
| ----------- | ---------------------------------------------------------------- |
| `main`      | Always releasable. All PRs merge here quickly.                   |
| `feature/*` | Short-lived, ideally less than 1–3 days.                         |
| `release/*` | Only for services needing controlled production release windows. |
| `hotfix/*`  | Emergency production fixes, merged back to `main`.               |

Avoid long-lived environment branches (`dev`, `sit`, `uat`, `prod`) — they create drift, merge pain, and slow delivery.

## 2. Coordinate polyrepo change with a change set

For changes across many repos, create a lightweight **change set ID**:

```text
CHANGE-1234-add-customer-risk-score
```

Each repo gets its own PR tagged with the change set ID:

```text
customer-api: CHANGE-1234 add risk score to response
risk-service: CHANGE-1234 expose score endpoint
frontend-bff: CHANGE-1234 map score into customer summary
```

Track them together in Jira/ADO/GitHub project — not by forcing one mega-branch.

## 3. Use contracts to decouple release order

> **Producers must be backward compatible before consumers depend on them.**

Safe rollout sequence:

```text
Step 1: Add new optional field to API/event
Step 2: Deploy producer
Step 3: Deploy consumers that use it
Step 4: Observe
Step 5: Later remove old field/behaviour
```

Contract tooling:

```text
OpenAPI contracts
AsyncAPI contracts
Avro/JSON Schema
consumer-driven contract tests
schema compatibility checks
```

This avoids lockstep deployment across repos.

## 4. Feature flags for multi-repo changes

Code merges to `main` before the feature is live. Use flags for:

```text
new API behaviour
new frontend flow
new orchestration path
new downstream integration
new event publishing behaviour
```

Typical rollout pattern:

```text
main contains the code → flag off in prod → deploy safely
→ turn on for internal users → pilot cohort → all users → remove flag
```

## 5. Branch-by-abstraction for big refactors

For large architectural changes, avoid long-running branches. Instead:

```text
old implementation
new implementation behind interface
runtime switch / feature flag
gradual migration
remove old implementation
```

Example:

```text
PaymentClient
  ├── LegacyPaymentClient
  └── NewPaymentClient
```

Multiple teams continue merging to `main` throughout the migration.

## 6. Release model by service criticality

| Repo type                   | Strategy                                |
| --------------------------- | --------------------------------------- |
| Low-risk internal service   | Pure trunk-based, no release branches   |
| Customer-facing service     | Trunk + optional release branch         |
| Regulated/high-risk service | Trunk + release branch + approval gates |
| Shared library              | Trunk + semantic versioning             |
| API contract repo           | Trunk + compatibility checks            |
| Deployment/config repo      | Trunk + environment promotion           |

## 7. Environment promotion via artifacts, not branches

Build once from `main`, promote the artifact:

```text
commit → artifact/image → dev → test → staging → prod
```

Do not rebuild from different branches per environment.

## 8. Governance gates per repo

Standard gates:

```text
PR review, unit tests, contract tests, security scan,
dependency scan, linting, API compatibility check,
container scan, deployment smoke test
```

Additional gates for high-risk changes:

```text
architecture review, data migration review,
operational readiness review, rollback plan, change record approval
```

## Key principle

In a polyrepo microservice architecture, **branches are local to a repo**. Coordination happens through:

```text
contracts · versions · flags · deployment orchestration · observability · change tracking
```

Not through synchronized long-running branches across repos.

> Teams use trunk-based development with short-lived branches. Cross-repo changes are coordinated through change-set tracking, backward-compatible contracts, feature flags, and artifact promotion. Long-lived shared branches are prohibited except temporary release or hotfix branches for governed services.
