---
title: AI in the SDLC — Terminology
tags: [ai-engineering, agentic-workflows, documentation]
topic: engineering/ai-native
status: notes
level: beginner
related:
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/ai-dlc-methodology.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - reading/new-sdlc-vibe-coding.md
updated: 2026-07-03
---

# AI in the SDLC — Terminology

There is no single industry term for "AI in the software development lifecycle."
The competing terms are not synonyms — they mark different **depths** of
integration, from AI that *assists* a human to AI that *autonomously runs* parts
of the lifecycle. This note disambiguates the vocabulary. For the staged
*progression* between these states, see the
[Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md); this note is just
the glossary.

## The four terms

**AI-Augmented SDLC** — the standard enterprise term (McKinsey, Deloitte, and
most consultancies). The traditional phases (plan, design, build, test, deploy)
stay intact; AI tools (Copilot, Claude, Cursor) are embedded in each phase as
high-powered assistants to boost productivity and automate repetitive work.
*Synonyms:* AI-Assisted SDLC, AI-Driven SDLC. **Use it** for today's mainstream
practice: speeding up existing workflows without restructuring them.

**AI SDLC** — the loose shorthand umbrella, used when leaders talk about their
modern toolchain or governance ("we're overhauling our AI SDLC for security").
**Caveat:** in data-science contexts the same phrase sometimes means the *ML
model* lifecycle — a naming collision worth flagging when it's ambiguous.

**Agentic SDLC** — the 2026 leading-edge term (popularised by Cisco,
Thoughtworks, GitHub) for mature orgs. Autonomous agents handle multi-step tasks
end to end: pick up a ticket, find the service, write the code, open the PR, run
tests, triage bugs. Humans stop doing the manual typing and become reviewers,
orchestrators, and governance gateways. **Use it** for pipelines where AI
*completes tasks autonomously*.

**AI-Native SDLC** — the architectural framing, defined by contrast with
"augmented." Augmented = bolting AI onto old Agile/Waterfall; native = rebuilding
the lifecycle from the ground up assuming AI is a core team member. The focus
shifts from producing code artifacts to defining intent, constraints, and
outcomes, leaning heavily on spec-driven development and continuous human–agent
collaboration. **Use it** when the *process itself* is redesigned around AI, not
just accelerated.

## Picking the right word

- Accelerating existing workflows with AI assistants → **AI-Augmented SDLC**.
- Autonomous agents executing tasks with humans verifying → **Agentic SDLC**.
- The lifecycle re-architected around AI from first principles → **AI-Native
  SDLC**.
- Loose umbrella / toolchain talk → **AI SDLC** (watch the ML-lifecycle
  collision).

## The underlying axis

The terms line up on one axis — *who executes the work, and where the bottleneck
moves* — which is exactly what the
[maturity model](agentic-sdlc-maturity-model.md) stages in detail. In short: as
execution shifts from humans to agents, the developer's role moves from *syntax
writer* → *copilot driver* → *systems thinker / auditor*, and the bottleneck
moves from typing speed → review capacity → human verification, architectural
governance, and defining intent. The
[Agentic SDLC](agentic-sdlc.md) and
[AI-DLC](ai-dlc-methodology.md) notes describe concrete methodologies at the
autonomous end; [AI-Native Engineering — Overview](ai-native-engineering-overview.md)
maps the whole cluster.
