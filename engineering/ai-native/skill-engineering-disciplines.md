---
type: note
title: Skill Engineering Disciplines
description: "Bilgin Ibryam argues agent skills decay as models, APIs, and infrastructure change, and applies five classic software-engineering disciplines — linting, evals, scanning, dependencies, and observability — to keep shareable skills from rotting."
tags: [ai-engineering, agentic-workflows, testing, security, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/cress-context-engineering.md
  - tools/claude-code-steering-mechanisms.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/security/secure-sdlc.md
source: "https://generativeprogrammer.com/p/5-software-disciplines-that-keep"
updated: 2026-07-19
---

# Skill Engineering Disciplines

Bilgin Ibryam (*The Generative Programmer*) argues that **skills** — reusable units
of agent context — **decay** over time as the models, APIs, and infrastructure they
assume drift out from under them. His remedy is to stop treating skills as ad-hoc
markdown and instead apply the **same lifecycle rigour used for code**: a skill is
*context-like code*, so give it linting, tests, security scanning, dependency
management, and observability. The framing extends the
[eval-driven](eval-driven-ai-development.md) argument from "test your skills" to the
full **context development lifecycle**: Generate → Evaluate → Optimise → Distribute
→ Consume Safely → Observe → repeat.

The load-bearing claim is that a shared skill occupies an **attack and maintenance
surface equivalent to a third-party code dependency** — so it deserves the same
supply-chain controls.

## The five disciplines

| Discipline | Analogue | What it does |
|---|---|---|
| **1. Skill linting** | Static analysis / code review | Offline checks *before* execution: deterministic schema/reference validation → best-practice scoring → model-assisted substance review |
| **2. Skill evals** | Automated testing | Behavioural evidence on representative tasks, as a **test pyramid** (isolated skill → project-with-repo-context → system). Scenario quality and **target-model diversity** matter more than a single coverage number |
| **3. Skill scanning** | Security / SCA | Assess three risk classes — **malicious**, **negligent**, **vulnerable** (information-flow) — via signatures, data-flow analysis, sandbox execution, dependency checks |
| **4. Skill dependencies** | Package management | Make implicit relationships explicit: manifests, lockfiles, versioning, transitive resolution — turning ad-hoc sharing into governed repositories |
| **5. Skill observability** | Runtime monitoring | Close the loop: convert production failures into new eval scenarios, and cluster behaviour traces to find missing or redundant skills |

### On linting (1)
A graduated pipeline: cheap deterministic checks (required fields, valid references)
run on every change; more expensive **model-based substance review** is scheduled by
risk and cost rather than run universally.

### On scanning (3)
Ibryam frames skills as a **supply-chain surface** with novel risks — instruction
injection, chain manipulation — and cites a tool landscape (NVIDIA SkillSpector,
Cisco Skill Scanner, SkillWard, Snyk Agent Scan). Listed as the emerging landscape
he surveys, not endorsements. This is where skill engineering meets the
[secure SDLC](../security/secure-sdlc.md): the same shift-left, scan-everywhere
discipline applied to a new artifact.

### On dependencies (4)
Governance and traceability add adoption friction but are what let skills scale
across an organisation. Microsoft's Agent Package Manager is cited as an example of
manifest/lockfile-style governance for skills.

### On observability (5)
Production telemetry turns skill maintenance from **reactive** (patch when it breaks)
to **optimising** (trace clustering surfaces hypotheses about which skills are
missing, redundant, or misfiring). Failures become the next test scenarios — the
runtime feedback edge of the [backpressure](agent-backpressure-loops.md) idea applied
to skills rather than code.

## Why it matters

The argument positions agent skills where microservices already sit: a shared,
versioned, tested, observable artifact ecosystem. Offline checks alone cannot capture
real-world behaviour, and shared repositories of skills demand the same lifecycle
controls as production systems. Treating context as a **first-class engineered
artifact** — not disposable prose — is the throughline.

## Relationship to other notes

- [Eval-Driven Development for AI Capabilities](eval-driven-ai-development.md) — owns
  discipline #2 in depth (assertions, the hill-climbing loop, negative tests); this
  note places evals as one of five lifecycle disciplines around it.
- [Harness Engineering](harness-engineering.md) — defines the **skill** as a reusable
  markdown-defined harness component; this note is about keeping that component
  healthy over time.
- [CRESS Principles for Context Engineering](cress-context-engineering.md) — skills
  *are* context, so the *Current* and *Refutable* properties are exactly what linting
  and evals defend against decay.
- [Claude Code Steering Mechanisms](../../tools/claude-code-steering-mechanisms.md) —
  the same author's catalogue of *where* an instruction (including a skill) can live;
  this note is *how* to keep those skills from rotting.
- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — skills are a
  layer of that stack; these disciplines are its maintenance regime.
- [Secure SDLC (DevSecOps)](../security/secure-sdlc.md) — the scanning discipline is
  DevSecOps applied to the skill supply chain.
