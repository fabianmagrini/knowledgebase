---
title: Trunk-Based Development
tags: [git, ci-cd]
topic: engineering/practices
status: notes
updated: 2026-06-15
related:
  - engineering/practices/polyrepo-branching-strategy.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/engineering-playbook.md
  - leadership/managed-disruption.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/release-confidence.md
  - tools/git.md
  - concepts/continuous-delivery.md
---

# Trunk-Based Development

All developers integrate to a single branch (`main` or `trunk`) continuously. Branches are short-lived — hours to at most a few days. The trunk is always in a releasable state.

This is the branching model that makes continuous delivery possible. Small batches, fast feedback, no merge queues.

## Prerequisites

Trunk-based development fails without these foundations:

| Prerequisite | Why it matters |
|---|---|
| Fast, reliable CI (< 10 min) | Developers need signal before moving on |
| Feature flag infrastructure | Incomplete work merges safely behind a flag |
| Sufficient test coverage | Trust that green CI means a releasable trunk |
| Small PR discipline | Large PRs block integration and invite conflict |

Introducing trunk-based practices without these in place causes instability, not speed.

## Branching by team scale

### Solo or pair
Commit directly to trunk. No branches needed. Push triggers CI.

### Small team (2–5 engineers)
Short-lived feature branches, open for hours to one day. PRs are small and reviewed quickly.

### Large team (5+ engineers)
Feature branches capped at 1–3 days. CI gates enforce merge eligibility. Affected-area test tooling keeps feedback fast as the codebase grows.

The rule of thumb: if a branch is still open on day four, something is wrong — either the task is too large, or it needs a feature flag.

## Enabling techniques

### Feature flags
Merge incomplete or experimental work to trunk with the feature disabled. The flag decouples code deployment from feature release.

```text
main contains the code
flag off in prod → deploy safely
flag on for internal users → validate
flag on for all users → release
remove flag → clean up
```

### Branch-by-abstraction
For large refactors that cannot fit in one PR, introduce an abstraction layer first, then migrate behind it incrementally — all on trunk.

```text
Introduce interface (PaymentClient)
Add new implementation behind it (NewPaymentClient)
Migrate call sites incrementally
Remove old implementation
Remove the abstraction if no longer needed
```

No long-running branch. Multiple engineers can work in parallel. Main stays green throughout.

### Keystone interface
Build all the supporting pieces first. Add the final connecting piece (the keystone) as the last, small commit that activates the feature. The work is in trunk but inert until the keystone lands.

## Comparison with other branching models

| Model | Branch lifetime | Integration frequency | Best for |
|---|---|---|---|
| Trunk-based | Hours–3 days | Continuously | Teams practising CD, fast iteration |
| GitHub Flow | Days–weeks | Per PR | Simpler projects, less frequent releases |
| Gitflow | Weeks–months | Per release cycle | Scheduled releases, multiple active versions |

Gitflow optimises for parallel release management at the cost of integration frequency. Trunk-based optimises for delivery speed at the cost of requiring mature CI and flag infrastructure. GitHub Flow sits between them.

## Common objections

**"We can't merge incomplete features."**
Feature flags solve this. Code ships dark; the feature ships when ready.

**"Our releases are scheduled, not continuous."**
Trunk-based is compatible with scheduled releases. Cut a release branch from trunk when ready. Trunk keeps moving; the release branch is an audit artifact. See [[regulated-service-release-process]].

**"Our codebase is too large for this."**
Large codebases benefit most from trunk-based because merge conflicts compound with branch age. The solution is affected-test tooling (Nx, Turborepo, Bazel) so CI only runs what changed, keeping feedback fast.

**"Code review takes time — branches have to wait."**
Small PRs (< 400 lines) review in minutes, not days. If review is the bottleneck, the PR is too large or the team is too thin.

## Relationship to continuous delivery

Trunk-based development is the **branching model**. Continuous delivery is the **deployment model**. They reinforce each other:

- Trunk-based ensures the artifact you deploy was recently integrated
- CD ensures the pipeline from commit to production is automated and fast
- Together they minimise the distance between writing code and observing it in production

You can practise trunk-based without full CD (manual deploy from a green trunk). You cannot sustainably practise CD without trunk-based — long-lived branches make deployment cadence unpredictable.
