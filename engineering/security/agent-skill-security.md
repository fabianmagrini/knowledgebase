---
type: note
title: Securing AI Agent Skills
description: "Skills as a supply-chain problem: the intent/capability/substrate model, control points from pre-install scanning through provenance to runtime enforcement, and why signatures prove origin rather than harmlessness."
tags: [security, ai-engineering, governance, agentic-workflows, reading]
topic: engineering/security
status: notes
level: intermediate
related:
  - engineering/security/secure-sdlc.md
  - engineering/security/governing-ai-in-the-cloud.md
  - engineering/ai-native/skill-engineering-disciplines.md
  - case-studies/stripe-kai-agent-platform.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - tools/claude-code-steering-mechanisms.md
source: "https://generativeprogrammer.com/p/10-open-source-projects-for-securing"
updated: 2026-08-08
---

# Securing AI Agent Skills

Bilgin Ibryam (August 2026) surveys the security stack forming around agent skills. His
framing: **a skill is a supply-chain artefact** — installed from a registry, executed with the
agent's privileges, and rarely read — and no single tool covers its lifecycle, so defence has
to be layered.

The value here is the taxonomy and the caveats, not the tool list. The tools are recorded
below as an **August 2026 snapshot** and will date; the questions they answer will not.

## The problem is measured, not anticipated

| | |
|---|---|
| Public skills flagged with suspicious patterns | **26.1% of 31,132** (SkillScan, arXiv 2601.10338) |
| Precedent incident | Hugging Face intrusion, July 2026 |

Roughly one in four public skills tripping a pattern check is not a warning about a future
threat surface. It is the current state of one.

## Three questions, three layers

The most durable thing in the piece is a tiered mental model. Each layer answers a different
question, and none substitutes for another:

| Layer | Question | Enforced by |
|---|---|---|
| **Intent** | *Is this action allowed?* | Policy-gated middleware authorising each consequential operation |
| **Capability** | *Can this process reach that resource?* | Process-level sandboxing over filesystem, network and inference |
| **Substrate** | *Where does the isolated workload run?* | Cluster-native provisioning and lifecycle |

The Intent layer is the same control described from the architecture side in
[The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) —
per-action authorisation rather than per-session, and the runtime form of the calibrated
autonomy in [Agentic Autonomy Levels](../ai-native/agentic-autonomy-levels.md). Reading them
together: the gateway note argues *why* the control belongs at a seam; this one argues it is
insufficient alone, because an allowed action performed by a process that can reach more than
it should is still a breach.

## Control points across the lifecycle

Organised by *when* the control applies:

**Pre-deployment scanning** — detect intent before installation. Static scanning (YARA, AST,
taint tracking), optional LLM review, repository-wide sweeps for dangerous data flows, secrets
and MCP configuration, and **escalation pipelines** that promote ambiguous skills from static
analysis to sandboxed execution rather than treating every skill identically.

**Supply-chain governance** — dependency resolution with lockfiles and policy, plus signed
provenance catalogues carrying evaluation evidence.

**Runtime enforcement** — process sandboxes with filesystem/network/inference policy,
Kubernetes-native isolated workloads, and policy middleware authorising each action with an
audit trail.

### The tools named (August 2026)

NVIDIA SkillSpector, Cisco AI Defense Skill Scanner, SkillWard, Agent Audit, AgentShield
(scanning); Microsoft Agent Package Manager, NVIDIA Verified Agent Skills (supply chain);
NVIDIA OpenShell, Kubernetes Agent Sandbox, Microsoft Agent Governance Toolkit (runtime).

*Several are NVIDIA- or Microsoft-authored. The framing is ecosystem-wide and the
layered-defence conclusion cuts against any single vendor owning the stack, but the selection
is not disinterested.* Ibryam also notes that SkillWard, parts of Agent Audit and the
substrate layer are experimental or minimal on hardening.

## What each control cannot do

The caveats are the part worth memorising, because each describes a control that *looks*
stronger than it is:

- **Signatures prove origin and integrity — not harmlessness.** A correctly signed skill from
  a verified publisher can still be malicious, and can certainly be careless. Provenance
  answers *who*, never *what it does*. This is the most commonly conflated pair.
- **Static inspection identifies suspicious patterns, not runtime behaviour.** It raises
  suspicion; it cannot discharge it.
- **Dynamic analysis only sees the branches your scenarios reach.** A clean dynamic run is
  weak evidence — absence of a triggered payload is not absence of a payload.
- **Middleware sharing a process boundary with the agent is not isolation.** Policy enforced
  inside the blast radius it is meant to bound needs container isolation underneath it.

Together these are why the answer is layering rather than tool selection: every individual
control has a category of thing it structurally cannot see.

## Why this matters more as skill libraries grow

*The note's own reading.*
[Stripe's Kai Agent Platform](../../case-studies/stripe-kai-agent-platform.md) documents 1,000+
skills contributed by 100+ teams under **federated ownership** — teams maintain their own
skills rather than a platform team curating all of them.

Federation is the right answer for throughput and the hard case for security: it distributes
authorship faster than review can follow, and it is precisely the shape the pre-deployment and
provenance controls above exist to handle. An internal skill library is a package registry
with the same trust problem, minus the years of tooling that public registries have
accumulated.

The corollary for [Skill Engineering Disciplines](../ai-native/skill-engineering-disciplines.md):
a skill is not only an artefact to be written well, it is a dependency to be admitted
deliberately.

## Relationship to other notes

- [Secure SDLC](secure-sdlc.md) — supply-chain and pipeline security for code; this is the
  same discipline applied to skills, which are installed and executed with agent privileges
  but rarely read.
- [The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) —
  the Intent layer, argued from architecture rather than threat.
- [Stripe's Kai Agent Platform](../../case-studies/stripe-kai-agent-platform.md) — the scale
  and federation that make this a live concern rather than a theoretical one.
