---
type: note
title: Agentic AI Strategy Frameworks
description: "Practical frameworks for classifying, planning, and implementing AI participation in engineering — plus the selectivity axis the others lack: core vs supportive subdomains, which allocates by competitive value rather than by risk."
tags: [ai-engineering, agentic-workflows]
topic: engineering/ai-native
status: notes
updated: 2026-11-09
related:
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/practices/engineering-playbook.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - leadership/learning-organisation.md
  - engineering/ai-native/apex-framework.md
  - case-studies/microsoft-ai-core-competency.md
  - engineering/architecture/ddd-strategic-design.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/review-replacement.md
  - case-studies/tano-eleven-x-pr-throughput.md
  - leadership/plan-is-not-a-strategy.md
  - engineering/practices/change-absorption-capacity.md
  - sre/ai-sre-and-the-incident-path.md
source: "https://gist.github.com/fabianmagrini/58ece8f11d73cc33cf5c706ac5d37488; https://learnings.aleixmorgadas.dev/p/agentic-development-and-engineering"
---

# Agentic AI Strategy Frameworks

Practical frameworks for classifying, planning, and implementing AI participation in engineering. Useful for strategic alignment, backlog classification, and system design decisions.

## 1. AI Collaboration Matrix

A two-axis model for assessing where a team sits and planning trajectory.

**Axes:**
- Who produces the work? (Human ↔ AI)
- Who manages the process? (Human ↔ AI)

```
                  AI manages
                      │
  AI-led execution    │    Autonomous agents
  Human produces      │    AI produces + leads
                      │
──────────────────────┼──────────────────────
  Human-only          │    AI-assisted
  traditional SDLC    │    human-led
                      │
                  Human manages
```

Most organizations are in the bottom-right (AI-assisted, human-led). The strategic question is: which quadrants make sense for which types of work, and what does an intentional trajectory look like?

Unstructured AI adoption — plugging in tools without choosing a quadrant — leads to inconsistent outcomes, technical debt, and cultural resistance.

## 2. Levels of Coding Autonomy

Modeled on the SAE self-driving levels. Useful for classifying tasks, teams, and systems — not for categorizing AI tools as a whole.

| Level | Name | Description |
|---|---|---|
| 0 | Manual | No AI. Human writes every line. |
| 1 | AI-Assisted | Copilot-style suggestions. Human types, AI completes. Human is the pilot. |
| 2 | Partial Automation | Human delegates a specific task ("write a function to validate emails"), reviews output, integrates. |
| 3 | Conditional Autonomy | Agent plans and executes a workflow ("scaffold a microservice from these specs"). Human reviews the plan before execution and the output before merge. |
| 4 | High Autonomy | Agent identifies tasks itself ("found a vulnerability in dependency X, created a PR"). Human acts as final approver only. |
| 5 | Full Agency | Agent autonomously manages a domain (e.g., QA suite that writes, runs, and fixes its own tests). Human receives summary reports. |

Different work types in the same team can operate at different levels simultaneously. The level should match the risk and reversibility of the task — not be applied uniformly across all work.

## 3. Automation Matrix

A quadrant for classifying work before deciding whether to automate it agentically. Classify by **judgment required** and **volume/frequency**.

| | Low Volume | High Volume |
|---|---|---|
| **High Judgment** | Human Only | Human-in-the-Loop |
| **Low Judgment** | Consider later | Fully Agentic |

### Fully Agentic (Low Judgment, High Volume)
Routine, repetitive tasks with clear success criteria. Cost of error is low or easily reversible.

Examples:
- Writing unit tests and boilerplate
- Migrating legacy code (e.g., Java 8 → 17)
- Log analysis and anomaly detection
- Generating documentation from code
- Dependency update PRs

### Human-in-the-Loop (High Judgment, High Volume)
Frequent but nuanced tasks. AI does the heavy lifting (~80%); humans refine and approve (~20%).

Examples:
- Code review and refactoring suggestions
- Writing complex queries
- Generating UI components from design files
- Onboarding context ("chat with codebase")

### Human Only (High Judgment, Low Volume)
Strategic, high-stakes, infrequent decisions requiring deep context, ethical reasoning, or creative architecture.

Examples:
- System architecture and design decisions
- Defining business logic and requirements
- Security policy creation
- Debugging critical production outages

### Practical application

1. Audit your backlog — tag tasks as Agentic / Human-in-Loop / Human Only
2. Assign tooling accordingly:
   - Agentic: autonomous agents (Devin, GitHub Copilot Workspace, custom harnesses)
   - Human-in-Loop: IDE assistants (Cursor, Copilot)
   - Human Only: structured design sessions, architecture forums

## 4. Enterprise agentic design patterns

### Supervisor pattern

A primary AI agent breaks down a goal and delegates sub-tasks to specialised worker agents. A human sits above the Supervisor to approve the final consolidated result.

```
Human (final approver)
     ↓
Supervisor Agent (coordinates)
     ├── Coder Agent
     ├── Reviewer Agent
     └── Tester Agent
```

Best for: complex, multi-step tasks where specialisation improves quality and a single agent would lose context.

### Human-as-Tool pattern

The agent works autonomously but has a tool it can call: `ask_human()`. When the agent's confidence drops below a threshold, it pauses and requests human input via a notification channel.

```
Agent working autonomously
     ↓
Confidence < threshold?
     ↓ Yes
ask_human() → human clarifies
     ↓
Agent resumes
```

Best for: long-running agentic tasks where human interruption should be exception-based, not constant — but total autonomy is too risky.

### Quality Gate pattern

Work is done agentically but cannot proceed to the next stage (e.g., merge, deploy) without passing a deterministic gate (automated tests) and a human manual approval.

```
Agent generates code
     ↓
Automated gate (tests, lint, security scan, policy checks)
     ↓ Pass
Human review and approval
     ↓ Approve
Merge / deploy
```

Best for: any agent work going into production. This is the standard pattern; the others are used in combination with it. See [[ci-cd-ai-engineering]] and [[agentic-sdlc]] for how the evaluation harness implements this.

## 5. Core vs supportive subdomains — selectivity by competitive value

The four frameworks above answer *how much* autonomy and *how* to structure it. None answers
**where it is worth applying at all**, and
[Aleix Morgadas](https://learnings.aleixmorgadas.dev/p/agentic-development-and-engineering)
(October 2026) supplies an axis for that from Domain-Driven Design:

| Subdomain | Agent fit |
|---|---|
| **Supportive / generic** — necessary but not differentiating | **Strong.** Fast delivery of expected features is pure gain; the solution being conventional is the point |
| **Core** — the competitive moat | **Risk zone.** AI excels at generating *known* solutions, so it tends to produce derivative work precisely where differentiation is the goal |

**This is orthogonal to every allocation model these notes already hold, which is why it is worth
having.** The zones in [Brownfield Agentic Engineering](brownfield-agentic-engineering.md), the
risk tiering in [Agentic Code Review](agentic-code-review.md), and the
migrations/public-interfaces/finance denylist in
[Replacing Code Review With Upstream Verification](review-replacement.md) all allocate by
**risk** — what a change can damage. This allocates by **value** — what the work is for. A core
subdomain can be perfectly safe to generate and still be the wrong place to generate, because
what you want there is the thing *not* already in the training data.

[DDD Strategic Design](../architecture/ddd-strategic-design.md) already holds the
core/supporting/generic axis as a guide to where engineering effort belongs; this extends the
same classification to where *agent* effort belongs, which that note does not cover.

It also generalises an observation these notes recorded as a UI problem.
[Tano](../../case-studies/tano-eleven-x-pr-throughput.md) reports design commoditisation — *"AI
designs are very similar to a lot of other designs out there"* — and this is the general form:
**generated output converges toward the mean of its training data, so differentiation becomes a
deliberate cost wherever it matters.** DDD supplies the vocabulary for naming where that is.

> **Provenance.** Self-described as *"a first exploration, a draft with thoughts"*, with **no
> metrics, cases or measurement anywhere in it**. Carried for the axis, not as evidence.

Two smaller things from the same piece.

**"Strategy Theater", with an attribution the repo was missing** — *"when we use buzzwords and
apparently esoteric concepts to create the illusion of high-level thinking. **Richard Rumelt
calls this Fluff.**"* [A Plan Is Not a Strategy](../../leadership/plan-is-not-a-strategy.md)
holds Roger Martin's version of the same critique; Rumelt's *fluff* is the canonical term for it
and appeared nowhere here. The relevance to this note is direct: a page of frameworks is exactly
the artefact that can be adopted as theatre.

**The build-cost inversion, with its consequence named.** Cheaper building makes *build* more
attractive than *buy*, and the saving does not stay where it was made: *"whoever builds it isn't
responsible for running it. **We are moving a lot of work to our SRE teams.**"* That is
[Change Absorption Capacity](../practices/change-absorption-capacity.md) pointed at a team rather
than a codebase, and it lands on
[AI SRE and the Incident Path](../../sre/ai-sre-and-the-incident-path.md), where `i = c × p` has
pages rising and out-of-hours pages nearly doubled. **Buy-versus-build now carries an unpriced
SRE term**, and his practical advice follows from it: assess SRE capacity *before* committing to
build.

## Using the frameworks together

| Decision | Framework to use |
|---|---|
| "Where is our team today?" | AI Collaboration Matrix |
| "Which level of autonomy is right for this task?" | Levels of Coding Autonomy |
| "Should we automate this with an agent?" | Automation Matrix |
| "How should we structure the agent system?" | Design patterns |
| **"Is this the right *place* to apply agents at all?"** | **Core vs supportive subdomains** |
| "How mature is our overall SDLC?" | Agentic SDLC Maturity Model (see [[agentic-sdlc-maturity-model]]) |
