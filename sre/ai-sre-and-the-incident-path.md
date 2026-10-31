---
type: note
title: AI SRE and the Incident Path
description: "Agents in the live incident path rather than the post-incident review: a seven-stage investigation pipeline ending at hand-off, self-confirmation as the dominant failure, and the structurally independent verifier that answers it — the oracle-independence principle arriving in diagnosis."
tags: [observability, ai-engineering, agentic-workflows, culture, reading]
topic: sre
status: notes
level: intermediate
related:
  - sre/incident-swarming.md
  - sre/cognitive-diversity-in-incident-reviews.md
  - sre/heroic-saves-are-near-misses.md
  - sre/self-blame-in-incident-reviews.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/rollback-and-roll-forward.md
  - engineering/ai-native/dora-ai-capabilities.md
  - engineering/ai-native/dark-factories-examined.md
  - engineering/ai-native/long-running-agents.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - case-studies/oracle-ai-agent-memory.md
  - case-studies/anthropic-scion-source-control.md
  - case-studies/uber-mcp-gateway.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/architecture/agents-as-distributed-systems.md
source: "https://newsletter.pragmaticengineer.com/p/ai-sre"
updated: 2026-10-31
---

# AI SRE and the Incident Path

Gergely Orosz and Jessica Salmon (October 2026) on the tools now being called **AI SREs** —
agents placed in the live incident path rather than in the review afterwards.

> **Provenance, and a disclosed conflict.** Orosz states *"I'm an investor in incident.io"* and
> that he has not been paid to mention any company. The architectures below come from **vendor
> interviews** — Rootly, incident.io, ResolveAI describing their own products — and the paging
> data is Rootly's.
>
> **The article is paywalled from section 4, "Making agents accurate."** Its own title asks
> *"does it work?"* and **the answer is behind the paywall**: there are no resolution rates, no
> false-diagnosis rates and no before/after MTTR figures in what is readable. This note covers
> why the category exists and how the tools are built, not whether they deliver.

Every other note in `sre/` is about the review *after* an incident. This is the first on the
incident itself.

## Why the category exists: a formula joining two things these notes held separately

> **i = c x p: Incident rate = [Change rate] x [Probability]**

> This says that if we have few deployments (low change rate) and high confidence that each
> deploy works (low probability of failure), then that is a pretty stable system. But with AI
> agents, deploy frequency is up and the incident rate is likewise increasing at most companies.

These notes are heavy on the **change-rate** side and had never connected it to the consequence:

| Evidence already held | Figure |
|---|---|
| [Anthropic's Scion](../case-studies/anthropic-scion-source-control.md) | **2,500 → 30,000+** merges per day in four months |
| [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md) | *software delivery instability* **up** with AI adoption |
| [Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) (Faros, 22,000 devs) | incidents **+242%**, unreviewed merges **+31.3%** |

Rootly's addition is the on-call cost, which nothing here measured: *"pages are also up from a
year ago, and **outside-business-hours pages have nearly doubled**."* That is the second term of
the formula landing on people rather than on dashboards, and it is the practical argument for the
whole category.

[Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) is the same
argument without the equation — cheap production outrunning the system's ability to absorb it.
The formula is worth having because it makes the trade explicit: if `c` is going up and you
cannot lower it, the only lever is `p`.

## The investigation pipeline, and where it stops

Seven stages: **Trigger → Orientation → Fan out → Verify → Report → Steer → Hand off.**

The shape carries the claim. The agent consolidates alerts, dashboards, runbooks and logs
(*orientation*), pursues hypotheses in parallel (*fan out*), challenges its own conclusions
(*verify*), posts to Slack (*report*), takes direction from an engineer (*steer*) — and then
**hands off**. Mitigation is executed elsewhere.

**Investigation rather than remediation is the autonomy boundary**, and it is drawn at the
diagnosis rather than at the action. That is
[calibrated autonomy](../engineering/ai-native/agentic-autonomy-levels.md) applied to operations:
the agent is trusted to narrow the problem and not to change production. Code remediation
approaches differ by vendor — incident.io passes context to an existing coding agent, Rootly
describes autonomous merging after verification as the direction — so the boundary is where the
disagreement sits.

## Self-confirmation, and the fix that is this repo's principle in a new setting

The dominant failure mode, stated plainly:

> the agent was tasked to grade hypotheses it came up for likely causes of incidents. **The agent
> almost always confirmed its first suspicion and didn't examine its conclusion.**

ResolveAI's three roles, with the second doing the work:

| Role | What it does |
|---|---|
| **Investigator** | *"chases one hypothesis after another"* |
| **Verifier** | *"challenges the conclusions of investigators. It's **structurally independent** of investigators to avoid self-confirmation"* |
| **Communicator** | updates stakeholders |

**"Structurally independent" is the oracle-independence principle arriving in diagnosis.**
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
holds that *"tests written by the system that wrote the code prove very little"* and independence
must come from outside the generator.
[Harness Design for Long-Running Apps](../engineering/ai-native/harness-design-experiments.md)
splits planner/generator/evaluator because *a model evaluating its own work over-praises it*.
Here the same requirement appears because **a model grading its own hypothesis confirms it** —
third setting, same structure. Worth noting the cost that split carried there: a **22× cost
multiple** for the elaborate harness over the solo agent.

### Parallel instances of one model are not cognitive diversity

The observation the article does not make, and the reason the *fan out* stage deserves more
scrutiny than it gets.

[Cognitive Diversity in Incident Reviews](cognitive-diversity-in-incident-reviews.md) argues the
point precisely: **genuinely different mental models**, not identity diversity, are what improve
reasoning about a complex system — because *"a production system is too large and interconnected
for any single engineer to hold a complete picture."* N parallel instances of the same model is
the agentic form of **identity diversity without cognitive diversity**: more investigators, one
prior. That is exactly why the verifier has to be *structurally* independent rather than simply
another investigator, and it suggests fan-out buys throughput rather than perspective.

The contrast with [Swarming in Incident Response](incident-swarming.md) is the useful one. There,
human responders **self-select by relevant expertise** rather than being deliberately paged, and
the value is that they arrive with different vantage points — load-testing experience, support
contact, on-call intuition. Swarming brings different models *to* the problem; spawning brings
the same model *N times*. Both scale the investigation; only one of them widens it.

That note also records something sharper for this context: integrating AI models as system
dependencies *"widens the gap between individual understanding and actual behaviour"* by
introducing opaque probabilistic failure modes. So the systems AI SREs are asked to diagnose are
partly ones AI made harder to diagnose.

## Context rot, with observable symptoms

[Long-Running Agents](../engineering/ai-native/long-running-agents.md) names context rot as one
of its walls and describes it as quality degrading before the hard limit. A live incident supplies
signatures:

> for long, multi-service incidents, the agent ran into context saturation (the **"dumb zone"**)…
> It started to **request data it already had** and to **contradict its own conclusions**.

Two checkable symptoms rather than a general warning — and both are the kind of thing an operator
can spot in a Slack transcript, which makes them usable as a stop signal. Note the interaction
with self-confirmation: an agent that contradicts its own conclusions and an agent that never
questions them are opposite failures, and an incident long enough to reach the dumb zone passes
through both.

## Two mechanisms worth stealing

**Quiet-first design.** Rootly's agent is *"predominantly quiet"* and posts only when:

- a question in the channel goes unanswered
- a stakeholder joins without context
- someone declares *"mitigated"* without proof
- **a risky action is announced with no rollback plan**

Each trigger is an absence rather than an event, which is a good instinct for a channel where
attention is the scarce resource. The fourth is
[rollback and roll-forward](../engineering/practices/rollback-and-roll-forward.md) wired as an
agent trigger, and the third is the only automated check in these notes for a claim humans make
constantly under pressure.

**Activated and quarantined memory.** A curation lifecycle for incident memory, which nothing
here holds:

> **'Activated' memory notes**: a note earns its spot in a more important memory note after
> playing a useful role in an incident, or someone activates it manually; **'Quarantined' memory
> notes**: if a note is contradicted, it gets quarantined to not be used in the future.

Promotion on demonstrated usefulness, demotion on contradiction.
[Oracle AI Agent Memory](../case-studies/oracle-ai-agent-memory.md) has lifetime layers and TTL —
time-based expiry — where this is **evidence-based**, and the difference matters because a stale
runbook is not wrong until it is contradicted.

## The landscape

In-house systems, which is the signal worth recording — several large organisations built rather
than bought, driven by the breadth of access these tools need to telemetry, logs and source:

| Organisation | System |
|---|---|
| OpenAI | **Sevbot** |
| Monzo | **Project Chip** |
| Stripe | unnamed investigation agent — *"A simpler run… takes three minutes, on average. A more thorough deep investigation is 14 minutes long, on average."* |
| Google | **ProdAgent** (within Gemini CLI) |
| Uber | **Context Graph** as the knowledge layer |

Uber's Context Graph is already held in
[Uber's MCP Gateway](../case-studies/uber-mcp-gateway.md) as a platform component that *"maps
relationships between code, services and engineers to inform agent decisions"* — now reappearing
as the knowledge graph an incident agent reasons over. The same artefact serving development and
operations is the more interesting fact than either use alone.

Rootly is also a familiar voice here for a different reason:
[its decision to retire a small-PR rule](../case-studies/rootly-pr-size-risk-labels.md) is held
as code-review evidence. This is the first time it appears in its own product domain.

## What the piece does not cover

- **Whether any of it works.** The accuracy section is paywalled; there is not one effectiveness
  figure in the readable portion. For a category this new, that is the whole question.
- **Vendor-described architecture.** The pipelines and agent roles are companies describing their
  own products, with an investor disclosure on one of them.
- **The near-miss problem.** [Heroic Saves Are Near Misses](heroic-saves-are-near-misses.md)
  argues that *"a save should trigger the same investigation an outage would"*, since an
  unexamined save leaves the identical latent weakness in place. An agent that routinely
  shortens or absorbs incidents produces saves at volume, and nothing here addresses whether the
  near-miss information survives into a review or disappears into a transcript. **This is the
  sharpest unasked question in the piece**, and these notes already hold the argument for why it
  matters.
- **Alert quality as the upstream fix.** Categorising pages into *needs attention / can wait /
  noise* treats the alert stream as given. Reducing `p` or fixing the alerts are the other
  responses to the formula, and neither is examined.
- **No cost figures**, for either the tools or the token spend of a 14-minute deep investigation
  run at paging volume.

## Relationship to other notes

- [Swarming in Incident Response](incident-swarming.md) — human self-selection by expertise
  versus agent fan-out; the first widens perspective, the second multiplies one.
- [Cognitive Diversity in Incident Reviews](cognitive-diversity-in-incident-reviews.md) — why
  structural independence rather than more instances is the right answer to self-confirmation.
- [Heroic Saves Are Near Misses](heroic-saves-are-near-misses.md) — the question this piece does
  not ask about agents that save the day routinely.
- [Change Absorption Capacity](../engineering/practices/change-absorption-capacity.md) —
  `i = c × p` is that argument as an equation, with the on-call cost attached.
- [DORA on AI](../engineering/ai-native/dora-ai-capabilities.md) and
  [Dark Factories Examined](../engineering/ai-native/dark-factories-examined.md) — the
  independent measurements of the rising-incident side.
- [Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md)
  and [Harness Design](../engineering/ai-native/harness-design-experiments.md) — oracle
  independence and the generator/evaluator split, here applied to hypotheses instead of code.
- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — context rot, with two
  observable symptoms added.
- [Agents as Distributed Systems](../engineering/architecture/agents-as-distributed-systems.md) —
  cascading decision degradation is what self-confirmation produces over a long investigation.
- [Oracle AI Agent Memory](../case-studies/oracle-ai-agent-memory.md) — TTL-based memory
  lifetimes against evidence-based activation and quarantine.
