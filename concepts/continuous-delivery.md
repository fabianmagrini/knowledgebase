---
title: Continuous Delivery
tags: [ci-cd, testing, code-review]
topic: concepts
status: notes
level: intermediate
related:
  - concepts/devops-capability-model.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/release-confidence.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/test-coverage-policy.md
  - engineering/security/secure-sdlc.md
  - concepts/theory-of-constraints.md
source: "Jez Humble & David Farley — Continuous Delivery (2010); Forsgren, Humble & Kim — Accelerate (2018)"
updated: 2026-06-17
---

# Continuous Delivery

Continuous Delivery (CD) is the discipline of building software so that **every
change is releasable to production at any time**. The decision to release becomes
a business choice, not a technical event — the software is always in a deployable
state, and getting it live is a routine, low-drama action.

This is the parent concept that several practice notes here hang off:
[trunk-based development](../engineering/practices/trunk-based-development.md) is
how teams keep the trunk releasable, and
[release confidence](../engineering/practices/release-confidence.md) is the
property CD produces when done well.

## CI vs CD vs Continuous Deployment

These three are routinely conflated:

- **Continuous Integration (CI)** — developers merge small changes to a shared
  trunk frequently (at least daily), and every merge triggers an automated build
  and test run. The goal is to keep the codebase in a working, integrated state.
- **Continuous Delivery (CD)** — every change that passes the pipeline is a
  *candidate for release*. Deploying to production is a manual decision but a
  push-button operation. CI is a prerequisite.
- **Continuous Deployment** — the stricter superset: every change that passes the
  pipeline is deployed to production **automatically**, with no human gate.

CD is the property; Continuous Deployment is the policy of removing the last
manual approval. Many regulated contexts deliberately stop at Continuous Delivery
— see [Release Process for Regulated and High-Risk Services](../engineering/practices/regulated-service-release-process.md).

## The deployment pipeline

CD is realised through a **deployment pipeline** — an automated implementation of
the path from commit to release:

```
commit → build → automated tests → release candidate → deploy → release
         (fast feedback first)      (every stage gates the next)
```

Principles of the pipeline:

- **Build the binary once.** Promote the same artifact through every environment
  rather than rebuilding; what you tested is what you ship.
- **Fail fast.** Cheap, high-signal stages (compile, unit tests, lint) run first;
  slower stages (integration, end-to-end) run later.
- **Stop the line.** A failed stage halts promotion — a broken pipeline is the
  team's top priority to fix.
- **Make it visible.** Pipeline state is shared and obvious to everyone.

## Core principles (Humble & Farley)

1. **Build quality in** — defects are prevented at the source, not inspected out
   later. See [Test Coverage Policy](../engineering/practices/test-coverage-policy.md).
2. **Work in small batches** — small, frequent changes are easier to reason about,
   test, and roll back than large infrequent ones.
3. **Automate repetitive work** — humans do exploratory and creative work;
   machines do builds, tests, and deployments.
4. **Keep everything in version control** — code, configuration, infrastructure,
   and database schema.
5. **Done means released** — work is not "done" until it is delivering value in
   production.
6. **Everybody is responsible** — delivery is a shared whole-team concern, not a
   downstream hand-off.
7. **Continuous improvement** — the pipeline and process are themselves subject
   to inspection and refinement.

## Enabling practices

CD does not stand alone; it depends on a stack of supporting practices:

- **Trunk-based development** to keep integration continuous and avoid long-lived
  branches that defer (and amplify) integration pain.
- **Comprehensive automated testing** — unit, integration, and contract tests
  that let the pipeline gate releases without manual QA bottlenecks.
- **Configuration and infrastructure as code** so environments are reproducible.
- **Feature flags / branch by abstraction** to decouple *deploy* from *release*,
  letting unfinished work ship dark.
- **Observability** to detect problems fast and make rollback or roll-forward a
  confident decision.

## Why it matters

- **Lower release risk.** Small, frequent, automated releases fail less often and
  are cheaper to recover from than big-bang deployments.
- **Faster feedback.** Shorter lead time from idea to production means faster
  learning and course-correction.
- **Reduced toil and stress.** Releases stop being weekend events; the pipeline
  does the heavy lifting.

CD is one of the practices most strongly correlated with software delivery
performance in the DORA research (deployment frequency, lead time, change-failure
rate, and time to restore). In an AI-assisted workflow it becomes even more load-
bearing — see
[CI/CD as the Control Plane for AI-Assisted Engineering](../engineering/practices/ci-cd-ai-engineering.md),
where the automated pipeline is what makes high-volume machine-generated change
safe to absorb.

## CD in the Accelerate capability model

*Accelerate* (Forsgren, Humble & Kim) identifies 24 capabilities that drive
software delivery performance, grouped into five categories — see
[The DevOps Capability Model (Accelerate / DORA)](devops-capability-model.md) for
the full 24 and the four delivery metrics they move. Continuous Delivery is the
technical core of that model: not a single practice but a capability cluster, the
eight capabilities below being what it takes to make CD real:

- Use version control for **all** production artifacts (code, config, infra).
- Automate the deployment process.
- Implement continuous integration.
- Use trunk-based development methods —
  see [Trunk-Based Development](../engineering/practices/trunk-based-development.md).
- Implement test automation.
- Support test data management.
- Shift left on security — integrate it into design and test, not as a late gate.
  See [Secure SDLC (DevSecOps)](../engineering/security/secure-sdlc.md).
- Implement continuous delivery (the outcome the others enable).

The other four categories — architecture, product and process, lean management and
monitoring, and cultural — matter because CD does not succeed in isolation; they are
enumerated in [the capability-model note](devops-capability-model.md). CD is the
technical core, but delivery performance is a whole-system property.

## Further reading

- **Books** — *Continuous Delivery* (Humble & Farley); *Accelerate* (Forsgren,
  Humble & Kim); *Modern Software Engineering* (Farley); *Site Reliability
  Engineering* (Google).
- **Talks** — Dave Farley, *Optimising Continuous Delivery* (PIPELINE 2018);
  Jez Humble, *Building and Scaling High Performing Technology Organizations*;
  Ken Mugrage, *Modern Continuous Delivery* (GOTO 2019); Sander Hoogendoorn,
  *How Thinking Small is Changing Software Development* (GOTO 2019).
- **Topics to follow on** — DevOps and GitOps, the DevOps engineer's handbook,
  trunk-based development.
