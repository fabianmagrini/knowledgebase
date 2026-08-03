---
type: note
title: The AI Gateway as a Governance Control Plane
description: "Concentrating the fastest-moving AI concerns — model choice, identity, action policy, guardrails, audit — behind one evolutionary seam, and why ordinary API gateways don't fit agentic traffic."
tags: [ai-engineering, architecture, security, governance, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/security/secure-sdlc.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/architecture/architectural-change-cases.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - case-studies/slack-ai-multi-cloud.md
source: "https://www.infoq.com/articles/evolutionary-architecture-pattern/"
updated: 2026-08-03
---

# The AI Gateway as a Governance Control Plane

A pattern proposal from Joe Price, Branimir Đurek, Pavlos Migkiros and Trevor Dearham (InfoQ,
July 2026, reviewed by Luca Mezzalira). Its premise is a mismatch in rates of change:

> AI ecosystems evolve orders of magnitude faster than enterprise platforms, and the gap is
> permanent enough to **design for** rather than wait out.

Models, protocols (MCP, A2A) and the threat surface all move continuously while backend
systems are deliberately stable. The proposal is to put an explicit **evolutionary seam**
between them — an AI gateway that absorbs the fast-moving concerns so the slow-moving systems
behind it do not have to.

This is the **governance** counterpart to
[Model Routing and AI Gateways](model-routing-and-ai-gateways.md), which covers the same
infrastructure as a *cost* layer. Same box in the diagram, different reason for it.

A pattern proposal and experience report drawing on documented public incidents, not
controlled research.

## Why ordinary API gateways don't fit

The sharpest section. A conventional API gateway assumes three things that agentic traffic
violates:

| Gateway assumption | What agents actually do |
|---|---|
| Services are **deterministic** | Identical inputs produce different outputs |
| Failures are **schema-level** | Failures are **semantic** — a valid, authenticated, well-formed request that refunds the wrong customer |
| The **client specifies intent** | The client specifies a *goal*; the agent decides which tools to invoke to reach it |

The second row is the one that breaks existing tooling. Schema validation, status codes and
retry logic all assume a failure is detectable at the boundary. When the request is
well-formed and the authorisation is genuine and the outcome is still wrong, nothing in a
traditional gateway notices.

## What the seam holds

Concentrate the components that change fastest into one control plane:

- **Model routing** — which provider and model serve a request
- **Identity** — who the agent is acting on behalf of (**delegated authority**)
- **Action policy** — which actions this agent may take, on what, right now
- **Guardrails** — input and output filtering
- **Audit** — what happened, and why

**Policy-as-config** is the mechanism: policies are declarative, version-controlled and
PR-reviewed, and deploy independently of the applications they govern. That independence is
the point — it lets policy move at the pace of the threat surface rather than the release
train, which is the same separation
[CI/CD as the Control Plane](ci-cd-ai-engineering.md) makes for deterministic gates.

**Zero trust for agents** (citing NIST SP 800-207): authorise **per action**, not per session.
This is [calibrated autonomy](agentic-autonomy-levels.md) enforced at runtime rather than
agreed in a document — that note's execution contract names tools, permissions and budget as
things to bound; this is where the bounding is actually applied.

**Semantic logging** structures records as **Request → Decision → Action** rather than as flat
events, so an audit can reconstruct *why* an agent did something and not merely that it did.
This is the evidence layer [Own the Outer Loop](own-the-outer-loop.md) calls answerability.

## The four-stage adoption path

| Stage | What it looks like |
|---|---|
| **1** | One team, one provider — in-application handling is adequate |
| **2** | Adoption spreads; approaches fragment across teams |
| **3** | A **forcing function** — an incident or a regulator — makes fragmentation untenable |
| **4** | Consolidated control plane |

Worth noting that stage 3 is usually an incident. The pattern's real-world adoption trigger is
retrospective, which is an argument for reaching stage 4 deliberately rather than being moved
there.

## The incidents cited

These are documented public cases, not hypotheticals:

- A **Replit agent** wiped a production database during a code freeze; 1,196+ companies affected
- An organisation reached **$500M monthly Claude spend** with no usage limits on employee licences
- **EchoLeak** — the first weaponised prompt-injection CVE
- Stanford HAI's **AI Incident Database**: 362 incidents in 2025, against 233 in 2024

The cost example is the one most likely to be dismissed as someone else's problem. It is the
same control gap as the security cases — nobody was enforcing a per-actor budget at the seam —
and it is the failure most organisations will meet first.

## Where it doesn't apply

The authors are unusually direct about the trade-offs:

- **Latency and throughput** — centralisation adds a hop; latency-sensitive workloads suffer
- **Centralisation risk** — the control plane becomes an organisational dependency and a policy bottleneck
- **Guardrails are probabilistic** — they mitigate rather than eliminate, with false positives in both directions (the Scunthorpe problem is cited)
- **Operational burden** — new tuning, triage and on-call surface
- **Not always justified** — a single team on a single LLM may reasonably prefer in-application guardrails, and development environments may not warrant the cost

## The framing oversells itself

The article is presented through evolutionary architecture — fitness functions, architectural
quanta, evolutionary pressure — but **no actual fitness functions are given**. The evolutionary
vocabulary is largely decorative over what is, underneath, a control-plane pattern with a
sound rationale for where the boundary goes.

That does not weaken the pattern, but it is worth reading the "evolutionary architecture"
framing as motivation rather than method. The genuinely evolutionary idea in it is narrower
and stands on its own: **place the seam where the rate of change differs most**, so the fast
side can move without dragging the slow side with it. That is the same reasoning as
[Architectural Change Cases](../architecture/architectural-change-cases.md) — designing for
the change you can anticipate.

## Relationship to other notes

- [Model Routing and AI Gateways](model-routing-and-ai-gateways.md) — the same layer justified
  on cost and provider independence; this note is the governance and security case for it.
  Together they explain why a gateway usually pays for itself twice.
- [Agentic Autonomy Levels](agentic-autonomy-levels.md) — per-action authorisation is the
  runtime enforcement of that note's execution contract.
- [Own the Outer Loop](own-the-outer-loop.md) — semantic logging is the audit evidence that
  makes answerability possible.
- [Secure SDLC](../security/secure-sdlc.md) — prompt injection as a delivery-pipeline concern;
  this covers it at the runtime boundary instead.
