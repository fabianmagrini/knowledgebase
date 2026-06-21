---
title: Release Process for Regulated and High-Risk Services
tags: [ci-cd, git, security, microservices, governance]
topic: engineering/practices
status: notes
updated: 2026-06-15
related:
  - engineering/practices/polyrepo-branching-strategy.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/engineering-playbook.md
  - leadership/managed-disruption.md
  - engineering/practices/federated-pr-review.md
  - engineering/security/secure-sdlc.md
  - engineering/practices/release-confidence.md
  - concepts/continuous-delivery.md
  - concepts/ci-cd-continuous-deployment.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/practices/database-migration-strategies.md
---

# Release Process for Regulated and High-Risk Services

The strategy for regulated or high-risk services is **trunk + release branch + approval gates**. This introduces deliberate human governance between "deployable" and "deployed" while preserving trunk-based development for the team.

## The core tension

Pure trunk-based development treats CI passing as sufficient for deployment. Regulated services add a mandatory human gate — for audit, compliance, or risk sign-off. The release branch is the mechanism that creates a stable, reviewable snapshot without blocking main.

## What the release branch actually does

It is not a development branch — it is an **audit artifact**. Cut it when development is complete and CI is green. Main continues moving; the release branch does not.

```text
main  ──●──●──●──●──●──●──●──
              │
        release/v2.4.0
              │
         [gate process]
              │
           deploy to prod
```

## Approval gate taxonomy

Not all changes need the same gates. Classify changes upfront to avoid applying the full CAB process to every deployment.

| Change type | Definition | Gate |
|---|---|---|
| Standard | Pre-approved pattern, no novel risk | Automated CI only, no CAB |
| Normal | New behaviour, moderate risk | Full gate process |
| Emergency | Production incident, expedited path | Abbreviated gate, post-hoc review |

### Gate roles for normal changes

| Gate | Owner | Focus |
|---|---|---|
| Change record | Change manager | Change type, risk rating, rollback plan |
| Security sign-off | Security team | SAST/SCA results, new attack surface |
| Architecture review | Architect | Breaking changes, standards compliance |
| Ops readiness | SRE/platform | Runbooks, monitoring, rollback tested |
| CAB approval | Change Advisory Board | Overall risk, deployment window |

## Gate evidence package

Reviewers should assess an evidence package, not raw code. CI produces this automatically as part of the release branch pipeline:

```text
- test results (pass rate, coverage delta)
- security scan output (SAST, SCA, secrets)
- dependency audit
- API compatibility check result
- change record with risk and rollback plan
- diff summary (what changed, not the raw diff)
```

Gates that review code directly tend to become bottlenecks or rubber stamps. Gates that review structured evidence scale.

## Feature flags as a safety valve

Code can ship to production dark, behind a flag. This separates two distinct risks:

- **Deployment risk** — did the artifact deploy safely?
- **Release risk** — does the new behaviour cause harm?

The gate approves flag activation, not deployment. This dramatically reduces the blast radius of each decision and allows deployment and governance to move at different speeds.

## Anti-patterns

**Branch aging** — if the gate takes a week and main moves fast, the release branch drifts. Any late fix requires a cherry-pick onto the release branch, CI re-run, and potentially restarting gates.

**Gate as ceremony** — gates become rubber stamps when reviewers receive dense diffs without context. The fix is structured evidence packages and pre-classified change types.

**Velocity collapse** — full CAB cycles on every change cause teams to batch releases to amortise the cost. Larger batches increase risk, which makes reviewers more cautious — a compounding feedback loop. Prevent this with standard change classification and automated gate evidence.

## Operating policy

```text
1. Develop on main with short-lived feature branches
2. Cut release/vX.Y.Z from main when CI is green
3. Attach evidence package to the change record
4. Gate window: max 3 business days
5. Required approvals: change manager + security (+ architecture for high-risk)
6. Deploy within approved change window
7. Tag the release commit; discard the release branch
```

Release branches should be short-lived. If branch-to-deploy takes more than five business days consistently, the gate process is the bottleneck — not the code.
