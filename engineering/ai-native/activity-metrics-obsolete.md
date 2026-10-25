---
type: note
title: Activity Metrics Under AI
description: "Why LOC, commits and PR counts stopped measuring anything useful — the −19% to +40.5% productivity scatter, six diagnostic replacements including rework-per-AI-spend, a measured $150–$3,000/dev/month spend range for its denominator, and the finding that culture sets PR baselines so cross-company counts confound."
tags: [ai-engineering, observability, ci-cd, security, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/apex-framework.md
  - reading/ai-productivity-research.md
  - leadership/mission-to-metrics.md
  - concepts/devops-capability-model.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/security/agent-skill-security.md
  - engineering/security/secure-sdlc.md
  - engineering/architecture/comprehension-as-architecture.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/architecture/runtime-architecture-verification.md
  - case-studies/ramp-inspect-agent-platform.md
  - leadership/learning-organisation.md
  - leadership/magical-thinking.md
  - product/modelling-business-impact.md
  - engineering/architecture/llm-platform-engineering.md
  - engineering/ai-native/agentic-verification.md
  - case-studies/uber-mcp-gateway.md
  - case-studies/anthropic-scion-source-control.md
  - engineering/ai-native/dark-factories-examined.md
  - case-studies/openai-agent-first-harness.md
  - engineering/ai-native/dora-ai-capabilities.md
source: "https://bharatsharma.pro/articles/activity-based-engineering-metrics-are-obsolete; https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers"
updated: 2026-10-26
---

# Activity Metrics Under AI

Bharat Sharma (September 2026) argues that activity proxies — lines of code, commit counts, PR
counts — have stopped measuring anything useful, and that the reason is not that AI removed
engineering work but that it **moved the work downstream** into review, validation and security.

His sharpest line on the oldest proxy: **"LOC has always punished the refactor and rewarded the
bloat; now the bloat is automated."**

The piece is an evidence brief with concrete metric definitions, which is why it sits beside
rather than on top of [The APEX Framework](apex-framework.md) — that is a measurement *operating
model* (four pillars, one north star each, review cadences); this supplies the studies and the
measure definitions.

## The scatter, which is the real finding

| Figure | What it measured |
|---|---|
| **−19% slower** with AI tools | METR: 16 experienced open-source developers, 246 tasks, **mature repositories** |
| **+40.5%** more PRs | Observational analysis of heavy GitHub Copilot users |

The author is careful about the second — a *"self-selected group"*, marked as *"upper bound, not
a forecast"*. The conclusion is the part worth keeping: **no single productivity coefficient
exists.** The spread is not noise to be averaged away; it is the result, and the mediating
variables are task type, developer seniority and codebase familiarity.

**The METR condition deserves emphasis**: the negative number came from *experienced* developers
working in *mature* repositories — the hardest available setting, and the one most organisations
actually occupy. That is the same limit
[Brownfield Agentic Engineering](brownfield-agentic-engineering.md) raises about greenfield
evidence, arriving from the measurement side.

Against which: **76%** of surveyed organisations had rolled out at least one AI coding assistant
org-wide, up from 41% in 2024, while only **34%** could point to *"a measurable, audited change
in delivery metrics"* (Halkwinds, 2026). Three-quarters deployed; a third can tell whether it
worked.

## Where the work went

| Finding | Source |
|---|---|
| Copy/pasted duplicate code **exceeded moved (refactored) code for the first time** in the dataset — 211M lines, 2020–2024 | GitClear |
| Code churn among heavy AI users **up to 9×** that of non-users | Apiiro, Q1 2026 |
| **45%** of generated samples failed security tests, across 100+ LLMs on controlled tasks — OWASP Top 10 issues including XSS and log injection | Veracode |
| Privilege-escalation paths **up 322%** in Fortune 50 repositories, Dec 2024 – Jun 2025 | Apiiro |

**The security figures fill a measured gap.** `engineering/security/` holds three notes and had
no vulnerability-rate data for AI-generated code at all. Veracode's 45% is a rate on *generated
samples under controlled conditions* rather than on shipped code, so it bounds the raw output
quality rather than the post-pipeline result — which is precisely the argument for the
[secure SDLC](../security/secure-sdlc.md) gates existing. The Apiiro 322% is the shipped-code
side, and privilege escalation is the specific class worth noting: not a defect in a function
but a path through a system, which is the kind of thing
[Runtime Architecture Verification](../architecture/runtime-architecture-verification.md) argues
only shows up in behaviour.

**One claim to treat as unsourced.** He reports *"Claude Code-authored PRs averaging about six
times the size of human-authored ones"* across roughly 110,000 open-source PRs, characterised as
*"padding, not progress"*. **This is the only figure in the piece with no footnote or link** —
every other study above is cited. It is also the most quotable, and it would otherwise slot
neatly beside [Rootly's small-PR decision](../../case-studies/rootly-pr-size-risk-labels.md) and
acquire weight it has not earned. Recorded, not relied on.

## The six replacements

Each with a definition and a stated analysis level, which is what makes them usable:

| Category | Metric | Definition | Level |
|---|---|---|---|
| Delivery flow | **Review queue time** | Time to first *substantive* review | Team, weekly |
| Code quality | **14-day rework** | Lines changed or reverted within 14 days ÷ lines introduced | Repo, weekly |
| Infrastructure | **Validation failure rate** | PRs failing gates ÷ PRs entering validation | Pipeline, weekly |
| Production | **Post-deployment rework** | Deployments for defect remediation ÷ total deployments | Service, monthly |
| Cost | **Rework per AI spend** | Rework lines ÷ AI tooling cost | Org, monthly |

**Rework per AI spend is the novel one** — a cost-efficiency ratio with no equivalent in these
notes. The repo holds plenty of AI cost figures (per review, per run, per worker fleet) and
plenty of quality signals, but nothing dividing one by the other. It answers a question an
executive will ask and nothing else here can: *is the spend buying throughput or buying rework?*

His rules on using them matter as much as the list:

- **Track against a frozen pre-AI baseline** — otherwise there is nothing to compare against,
  which is what the 34% figure above is measuring.
- **Never report per individual.** Team-level minimum.
- **Pair with SPACE satisfaction metrics** and align to business outcomes.

That second rule is the one these notes already argue from another direction.
[Comprehension as an Architectural Characteristic](../architecture/comprehension-as-architecture.md)
holds that metrics about people change behaviour once enforced, so they should be *"investigation
triggers, not gates"*; [From Mission to Metrics](../../leadership/mission-to-metrics.md) treats
the same Goodhart problem with the target/guardrail/diagnostic split. His version is the policy
form: **the risk is the dashboard becoming a leaderboard**, and the mitigation is structural
rather than cultural.

## The denominator, measured — and a disagreement it surfaces

*Rework per AI spend* needs a spend figure, and a survey by
[Gergely Orosz](https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers)
(October 2026) supplies the first distribution of one in these notes.

> **How to read it.** The volume data below comes from **CodeRabbit** and **Gitar** (Sonar's AI
> code verification product) — vendors with an interest in PR volume looking high. Everything
> else is self-report from engineering leaders, which is the weak link
> [Dark Factories Examined](dark-factories-examined.md) identifies: METR measured developers
> **19% slower** while they believed they were **20% faster**. And the article is **paywalled
> from section 4**, so its actual ROI analysis — the question in its title — is not readable
> here. What follows is the spend survey, not an answer.

**Spend per developer per month spans roughly 20×, with no relation to company size:**

| Organisation | Per dev / month |
|---|---|
| Publicly traded, 1,500 engineers | **$150** (limit) |
| Publicly traded, 25,000+ employees | ~$1,000 (average) |
| Publicly traded SaaS, ~600 engineers | $1,200 (limit) |
| Series D hospitality, 200 engineers | $1,500 (default cap) |
| Quant trading, ~2,000 devs | $1,600 average — **up from $80** |
| AI SaaS, ~100 employees | $2,000 |
| Small .NET startup, **2 devs** | **$3,000** — the highest |
| Multinational, 10K+ employees | $4,000 hard-cap ceiling |

The extremes run *inverse* to headcount: the smallest company spends twenty times per head what
the 1,500-engineer one allows. Useful mainly as a sanity range — anyone computing rework per AI
spend now has an idea of what the denominator looks like elsewhere.

**The trajectory matters more than the level:**

> June and July saw peak monthly spend at nearly all companies, and costs have roughly halved
> for those on API plans. A mix of Opus 5.5 and moving to open models is the reason for the drop
> at most companies.

Nothing else here records AI cost *deflation* over time, and it has a direct consequence: every
cost figure in these notes captured before August 2026 is now wrong in the favourable direction,
and any ROI case built at the peak understates the return.

### The amplifier effect, contradicted

The **amplifier effect** below has strong practices magnifying AI's throughput gain. A staff
engineer at a publicly traded SaaS company (~600 engineers) reports close to the opposite:

> Overall, I personally see accelerated slop produced all around me. However, when the team
> cares about the quality in production code and wants to keep it like before AI, then actual
> development speed had not increased much.

DORA has good practice *amplifying* the gain; this has quality insistence *absorbing* it. The
likely reconciliation is that the two measure different outputs — DORA's throughput is delivered
change, this is features shipped **at constant quality** — but the disagreement is worth leaving
visible, because the second version is the one a team with high standards will recognise and the
first is the one that gets quoted at them.

### Culture sets the baseline, which confounds every PR count

Gitar's tiers across hundreds of customers: regular teams at **~5 PRs/dev/week**, "AI-native"
teams at **60+**. Orosz's explanation is not tooling:

> If the company is one where ~5 PRs per week is considered a high output, then new joiners get
> used to that pace. If it's a place where most people ship 20-30 PRs to production per week,
> then new joiners pick up that pace!

If baseline output is culturally set, **cross-company PR comparisons are partly measuring
culture rather than AI** — which is a caveat the authorship-count figures in these notes
([Ramp's 75%](../../case-studies/ramp-inspect-agent-platform.md),
[Rootly's 80%](../../case-studies/rootly-pr-size-risk-labels.md),
[OpenAI's ~3.5 PRs per engineer per day](../../case-studies/openai-agent-first-harness.md)) do
not carry. It is also a second argument for *Trusted Throughput* below: weighting by difficulty
at least normalises against a baseline the counting does not.

CodeRabbit's own figure — **a 128% rise in PRs** for the same cohort of 20,000 developers over a
year — is the volume claim, and it is a vendor measuring activity on its own platform.

One team lead reports *"PRs have exploded in size and have 3x as many lines of code per change
request as before"*. Faros's **+51% PR size** across 22,000 developers in
[Dark Factories Examined](dark-factories-examined.md) is the same direction at a third the
magnitude; treat the 3× as one team's observation and the +51% as the figure.

## Two framings worth keeping

**The senior/junior inversion.** AI *narrows* the output gap between junior and senior engineers
while *widening* the validation gap — so the ladder's assumption that output tracks judgement
breaks. This is the structural reason behind a practice
[Accountability for Unread Code](accountability-for-unread-code.md) recommends without
explaining: deliberately preserving hands-on skills among juniors. If output no longer
discriminates, the thing the ladder needs to measure is the thing AI did not level.

**"Trusted Throughput"** — credited to Mingsheng Hong, VP of AI at Ironclad: use AI to assign a
complexity t-shirt size to merged PRs, so throughput is *weighted by difficulty* rather than
counted. Paired with capped agentic loop steps and token hygiene. That is a direct answer to the
authorship-count ambiguity running through these notes
([Ramp's 75%](../../case-studies/ramp-inspect-agent-platform.md),
[Rootly's 80%](../../case-studies/rootly-pr-size-risk-labels.md)) — those count PRs; this tries
to weight them.

The **amplifier effect** (attributed to DORA 2025) — AI magnifies existing engineering culture,
so strong testing plus AI raises throughput while weak practices plus AI accelerates degradation
— is already the position of [The Learning Organisation](../../leadership/learning-organisation.md)
and [Magical Thinking](../../leadership/magical-thinking.md). The DORA attribution is the new
part. The **J-curve** (an initial productivity dip after rollout, then recovery) is asserted
rather than shown.

## The 90-day playbook

1. **Days 1–30** — freeze pre-AI telemetry as the baseline.
2. **Days 31–60** — implement guardrails: PR size caps, agentic loop limits.
3. **Days 61–90** — rewrite executive dashboards: remove LOC, commit and PR counts; add review
   queue time and rework.

Worth noting the tension in step 2: **PR size caps** are exactly what
[Rootly retired](../../case-studies/rootly-pr-size-risk-labels.md), on the argument that an agent
produces a whole feature atomically and splitting it afterwards is busywork. Both can hold — a
cap is a crude guardrail for a team without risk tiering, and risk labels are the better
instrument once you have them — but the playbook presents the cap without that caveat.

## Relationship to other notes

- [The APEX Framework](apex-framework.md) — the operating model to this note's evidence and
  definitions. APEX names the pillars and cadences; this specifies what to actually compute and
  supplies the studies for why.
- [Five Studies on AI and Software Engineering Productivity](../../reading/ai-productivity-research.md)
  — the repo's other evidence anchor, via Houck. These are different studies entirely, and the
  two together are the measurement layer under the cluster.
- [From Mission to Metrics](../../leadership/mission-to-metrics.md) — Goodhart's law and the
  target/guardrail/diagnostic split, treated more rigorously than the "use three at once"
  heuristic here.
- [The DevOps Capability Model (DORA)](../../concepts/devops-capability-model.md) — the four
  delivery metrics these diagnostics sit beside; the amplifier effect is attributed to DORA 2025.
- [Brownfield Agentic Engineering](brownfield-agentic-engineering.md) — METR's negative result
  came from mature repositories, which is this note's strongest connection to that one.
- [Securing AI Agent Skills](../security/agent-skill-security.md) and
  [Secure SDLC](../security/secure-sdlc.md) — the first vulnerability-rate figures for
  AI-generated code in these notes.
- [Change Absorption Capacity (CATS)](../practices/change-absorption-capacity.md) — rework and
  validation-failure rates are what exceeded absorption capacity looks like in telemetry.
