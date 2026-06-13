---
title: The Agentic SDLC
tags: [ai-engineering, architecture, ci-cd]
topic: engineering/practices
status: notes
updated: 2026-06-13
related:
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/agentic-sdlc-maturity-model.md
  - engineering/practices/agentic-ai-strategy-frameworks.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/architecture/c4-model.md
  - engineering/architecture/composable-architecture.md
source: "https://gist.github.com/fabianmagrini/4862954cd301634ab4bfd595c00ea52c"
---

# The Agentic SDLC

The traditional SDLC rested on a single implicit assumption: humans write most of the code. Waterfall, agile, and DevOps all preserved this shape:

```
Requirements → Design → Implement → Test → Deploy → Operate
```

That assumption no longer holds. The SDLC is not dying — it is being rewired.

## The cybernetic SDLC

The emerging agentic lifecycle is a closed-loop reasoning system:

```
Intent → Spec → Context → Generate → Evaluate → Repair → Govern → Observe → Iterate
```

Each stage maps to a transformed discipline:

| Old | New |
|---|---|
| Requirements | Structured specifications (executable context) |
| Code review | AI-assisted diff reasoning |
| Testing | Automated evaluation harnesses |
| Governance | Policy-as-code + agent gates |
| Deployment | Continuous verification |

This is less waterfall vs agile — more **human-in-the-loop cybernetic systems**.

## Seven theses

1. AI compresses implementation cost dramatically
2. Architecture and system design become the leverage points
3. Context quality determines output quality
4. Evaluation harnesses are mandatory
5. Governance must become automated
6. The role of engineers shifts upward — abstraction and orchestration
7. Organizations that redesign their operating model outperform those that "just add AI"

## Code is cheap. Coherence is not.

When AI writes code, volume increases, variability increases, and review surface area explodes. The real bottlenecks become:

```
Architectural coherence
Interface stability
Test coverage integrity
Policy enforcement
Organizational alignment
```

AI amplifies both productivity and chaos. The difference between high-performing and struggling teams is their ability to manage entropy.

## Spec-driven workflow

The consensus from practitioners (Addy Osmani, Simon Willison, Nick Tune):

1. Write the spec first
2. Constrain the model heavily
3. Decompose tasks into small increments
4. Generate and evaluate aggressively
5. Refine iteratively

This is effectively **TDD + systems thinking + prompt engineering**. The most effective engineers are not the fastest typists — they are the best constraint designers.

> Senior engineers don't write more code. They design better context.

## Spec-as-Code

In AI-native organizations, specifications become first-class production artifacts:

- Version-controlled alongside source code
- Linted for completeness and consistency
- Change-controlled (diff-based spec review before generation)
- Traceable to generated artifacts

Artifacts that require versioning extend beyond source code:

```
Structured specs (Markdown + schema)
API contracts
Prompt templates
Guardrail definitions
Architectural constraints
Test expectations
Evaluation datasets
```

Prompt changes, evaluation threshold updates, and model upgrades are change management events — not informal tweaks.

## Context Development Lifecycle

Patrick Debois's insight: in the age of agents, **managing context is as important as managing source code**. If the agent doesn't have the right context, the code it produces is "hallucinated debt."

Context must be:

- Curated and pruned (not just accumulated)
- Versioned and traceable
- Scoped to the task (context isolation)
- Protected from sensitive data leakage

## Architecture matters more, not less

AI thrives in clean, modular systems with explicit contracts and clear boundaries. It amplifies dysfunction in tightly coupled systems, codebases with implicit domain knowledge, and "big ball of mud" architectures.

> Agents are powerful accelerators — but they accelerate in the direction your architecture already points.

Requirements for agent-ready architecture:

```
Idempotent workflows
Durable execution
Clear module boundaries
Deterministic test harnesses
Strong observability
Policy enforcement layers
```

## AI observability and drift detection

AI outputs must be observable like microservices. New operational domain: **AI SRE**.

Metrics to track:

```
Generation success rate
Repair loop count (attempts before passing)
Test pass ratio on first generation
Hallucination frequency
Context token usage and cost
Model regression indicators
```

Drift types to monitor:

| Drift type | Description |
|---|---|
| Model drift | Model behaviour changes across versions |
| Prompt drift | Prompt template decay or inconsistency |
| Evaluation drift | Test suite no longer reflects risk |
| Domain drift | System behaviour diverges from spec |

### New incident taxonomy

Agentic systems introduce new incident types that require distinct detection and response:

```
Hallucination incident     — agent generates non-existent APIs or logic
Drift incident             — system behaviour diverges silently from spec
Prompt regression          — prompt change degrades output quality
Evaluation failure         — harness passes code that is actually broken
Context leakage            — sensitive data exposed through agent context
```

## The organizational divide

Organizations are splitting into two camps:

**Tool adopters**
- Use AI for code completion
- Improve local productivity
- Keep legacy process intact

**AI-native operators**
- Redesign workflows around agents
- Build internal harness platforms
- Shift governance upstream into spec and policy
- Invest in evaluation engineering
- Formalize context management

The second group is building compounding advantage — not because they write more code, but because they manage entropy better.

## The harness is the product

The most important convergence across practitioners (Stripe Minions, OpenAI Harness Engineering):

> Frameworks help. Prompts matter. But neither is sufficient.

Without structured evaluation loops, AI-generated systems drift. A proper agent harness includes:

```
Deterministic test suites
Automated repair loops (generate → evaluate → repair → re-evaluate)
Policy gates
Observability hooks
Rollback mechanisms
Change traceability
```

This is CI/CD extended into probabilistic systems. Where DevOps automated deployment pipelines, the agentic SDLC automates reasoning verification.

## The psychological trap

AI increases the feeling of speed. But velocity illusions are common. Rapid generation can:

- Mask architectural debt
- Inflate perceived progress
- Encourage superficial iteration
- Increase cognitive overload

Dalia Havens' framing: "Feeling Fast, Delivering Slow." The illusion of speed becomes a managerial risk. Code volume is a bad productivity metric in an AI-augmented team.
