---
type: note
title: Secure SDLC (DevSecOps)
description: "Shifting security left with automated pipeline gates plus beyond-the-pipeline DevSecOps practices."
tags: [security, ci-cd, ai-engineering, governance]
topic: engineering/security
status: draft
related:
  - engineering/security/governing-ai-in-the-cloud.md
  - languages-and-frameworks/nodejs-cli-best-practices.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/code-review-policy.md
  - concepts/continuous-delivery.md
  - concepts/devops-capability-model.md
  - reading/fintech-engineering-handbook.md
updated: 2026-06-16
---

# Secure SDLC (DevSecOps)

Security is a property of the whole delivery lifecycle, not a gate at the end. **DevSecOps**
shifts security *left* and *everywhere*: into design, into the pipeline, and into runtime —
as automated guardrails rather than a manual review bottleneck. This matters more as AI
agents generate code at speed (see [CI/CD as the control plane](../ai-native/ci-cd-ai-engineering.md)):
AI can reproduce credential patterns, introduce injection flaws, or pull vulnerable
dependencies, so the automated checks must absorb what human review no longer can.

## Automated pipeline gates

| Gate | Catches |
|---|---|
| **Secret scanning** | Committed credentials / keys (AI may reproduce patterns from training data) |
| **SAST** (static analysis) | Injection, insecure defaults, unsafe code paths |
| **SCA** (dependency scanning) | Known-vulnerable or outdated packages |
| **License compliance** | Incompatible/again-risky dependency licenses |
| **Container scanning** | Vulnerable base images and layers |
| **SBOM + provenance/signing** | Supply-chain integrity — what's in the artifact and that it's authentic |

Place cheap, high-signal checks first; fail fast.

## Beyond the pipeline

- **Threat modeling** at design time — reason about trust boundaries before code exists.
- **Least privilege** for services, pipelines, and the agents themselves.
- **Human approval** for changes touching auth, payments, customer data, or security
  controls — never auto-merged (mirrors the high-risk tier in
  [code review policy](../practices/code-review-policy.md) and the gates in the
  [regulated service release process](../practices/regulated-service-release-process.md)).
- **Runtime**: monitoring, anomaly detection, and a tested incident-response path.

## Status

Starter note — seeds the `security/` section. Expand with dedicated notes on threat
modeling, supply-chain security (SLSA), and secrets management as they're captured.
