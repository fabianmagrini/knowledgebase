---
type: case-study
title: Netflix's Ontology-Driven Observability
description: "Netflix treating end-to-end observability as a data-modelling problem: an RDF/OWL knowledge graph unifying a dozen operational tools, identity gated by the software catalogue, incident discussion captured as triples, and the ontology — not messages — as the interface between root-cause agents."
tags: [observability, system-design, ai-engineering, agentic-workflows, reading]
topic: case-studies
status: notes
level: advanced
related:
  - case-studies/netflix-service-topology.md
  - sre/ai-sre-and-the-incident-path.md
  - engineering/architecture/data-readiness-for-agents.md
  - reading/reactive-reducer-orchestration.md
  - reading/durable-execution-for-agents.md
  - case-studies/uber-mcp-gateway.md
  - standards/open-knowledge-format.md
source: "https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf"
updated: 2026-11-28
---

# Netflix's Ontology-Driven Observability

Prasanna Vijayanathan and Renzo Sanchez-Silva (Netflix Tech Blog, 16 October 2026) on building a
knowledge graph across Netflix's operational tooling so that incident investigations — human and
agentic — start from connected context rather than from what one engineer remembers. The thesis
in a line:

> The hard part of end-to-end observability is probably better understood as a **data modelling
> problem**.

> **Provenance.** Company-authored, and candid about being early: *"the ranked hypotheses are
> sometimes wrong"*, the Metrics and Alerts ontologies are still in progress, and the integration
> with Netflix's Upper domain-modelling language is a proof of concept. **No before/after
> measurement is reported** — no MTTR, no hypothesis accuracy. The scale figures (65M concurrent
> streams, 2B+ requests a day, 38M+ log events/sec) are scene-setting for the problem, not results
> of the system, and the flywheel outputs quoted ("api-gateway deploys cause 40% of SEV-2s") are
> **illustrative examples of what the loop could produce**, not findings.

## The problem: coherent systems, isolated from each other

> Each of our systems is internally coherent and externally isolated.

Atlas (metrics), Radar, incident.io, PagerDuty, Spinnaker (deploys) and Slack each hold accurate
data, but the same thing is an *application* in one, a *service* in another and a *cluster* in a
third. The worked example is a home-screen regression adding ~1.5s to render, which takes roughly
four hours to resolve — and most of that is **reconstructing relationships the systems already
knew**. Each MELT pillar (metrics, events, logs, traces) answers about a quarter of the question;
joining them is left to a human doing name resolution in their head.

That is a different diagnosis from the one [AI SRE and the Incident
Path](../sre/ai-sre-and-the-incident-path.md) works with. There, *orientation* — consolidating
alerts, dashboards, runbooks and logs — is a stage the agent performs on every incident. Netflix's
position is that orientation is expensive because the **data model is missing**, and that it
should be built once as a standing artefact rather than re-derived per incident.

## Architecture

| Layer | What it is |
|---|---|
| **Data model** | Subject–predicate–object triples on W3C standards: RDF (data), OWL (ontology), SHACL (validation), SPARQL (query) |
| **Ontology** | Twelve namespaces, one per operational domain |
| **Storage** | **QuipuDB**, an in-house distributed quad store on **redb** (a Rust embedded KV store); each harvest also emits Turtle for archiving and diffing |
| **Identity gate** | No entity becomes an `ops:Application` unless it validates against the software catalogue (~49,000 entries) — *unvalidated strings never become applications* |
| **Enrichers** | Dozens of them, each reading the graph, adding typed triples, writing back — **sequentially** (load, add, save) to avoid races; external calls best-effort, so a slow dependency degrades the graph rather than blocking it |
| **Correlation engine** | 13 signal types (log errors, metric anomalies, slow/failed traces, alerts, incidents, deploys, config changes, experiments, autoscaling, commits, end-to-end bottlenecks, error patterns) scored by temporal proximity and severity in a **10-minute window**; chains under **0.6 confidence** discarded; known causal pairs (deploy → log error) carry higher priors; every chain stored with the records that produced it |

Three invariants hold the graph together: every entity has an `rdf:type`, URIs follow one naming
scheme, and the catalogue gates every application. Dependency edges are **capped in both
directions** so a heavily-used service does not dominate — the graph-modelling form of the
100× hot-node problem in [Netflix's Service Topology](netflix-service-topology.md), which is the
system that discovers those edges in the first place.

## What the case adds

### Identity before anything else

The first design principle the authors list is *model identity before anything else*, and it is
the one the rest depends on. A knowledge graph over unresolved names is a graph of strings. The
catalogue gate is a **hard precondition on entity creation**, which is the same move as the
data-contract gate in [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md),
applied to the nouns rather than to the datasets.

### "Constrain stochastic tools with a type system"

The principle the authors say they *"would defend hardest"*. LLMs, fuzzy matching and
probabilistic causal inference all stay in the pipeline, but their outputs are forced into typed
fields with fixed vocabularies (a `category` restricted to a list), through **five layers that
progressively reduce unstructured information** (they call what remains *entropy*). The goal is
that the final graph answers a given SPARQL query the same way every time.

That is the third arrival of one position in these notes:

- [Reactive Reducer Orchestration](../reading/reactive-reducer-orchestration.md) — remove the model
  from control flow entirely; agents write typed values, a deterministic loop decides.
- [Long-Horizon Agents and Durable Execution](../reading/durable-execution-for-agents.md) — the
  model chooses, but only among tools an `allowed()` predicate in code permits.
- Here — the model *produces data*, but only data that fits a schema.

The difference is where the constraint sits: on control flow, on action selection, or on the
shape of what the model writes. Netflix is the only one of the three with production scale behind
it.

### The ontology as the interface between agents

**AutoRCA**, Netflix's internal root-cause system, coordinates specialist agents around one
question. Each reads and writes triples about the same entities (`ops:Application` and so on)
**without knowing the other agents exist**. New agents learn the vocabulary once.

That is a coordination model the repo did not hold. The others in these notes are messages
(orchestrator–workers), protocols ([Agent Interop Protocols](../standards/agent-interop-protocols.md)),
or a typed context store with a deterministic scheduler (Reactive Reducer). This is closest to the
last, but with an **open-world shared schema** in place of a closed state type — a blackboard
architecture whose blackboard is a validated ontology. It also explains why the identity gate
matters so much: in a coordination-through-data design, an entity-resolution error is a
miscommunication between agents.

### Human reasoning as data

Incident Slack channels are converted into triples capturing **hypotheses, mitigations, and who
knew what**.

> Telemetry records what the system did, discussion records what people understood and
> interpreted.

This is the part closest to the post-incident cluster in `sre/`, which treats what responders
understood as the primary object of a review. Capturing it as structured data makes past
reasoning queryable at the next incident — *"similar past incidents"* is one of the things the
graph supplies — and is what the authors mean by *"the ontology gradually stops being a schema
and starts being a memory."* The obvious open question, not addressed, is fidelity: a triple
extracted from a Slack thread by a stochastic parser records what the parser understood people to
have understood.

### The knowledge flywheel

Four phases per harvest cycle — **Observe, Enrich, Infer, Adapt** — with recurring correlation
patterns hardening over time into detection rules. Illustrative only, per the provenance note.

## A tension worth holding

[Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) records its
authors' concession that **knowledge graphs are supplementary, not foundational** — relationship
depth at the cost of separate infrastructure. Netflix's architecture is the opposite bet: the
graph *is* the foundation and the tools are its sources. The two are not necessarily in conflict —
data readiness is about agents consuming business datasets, where joins already exist; Netflix's
problem is that **no join exists across tools**, because the identities do not match. A graph is
foundational where identity resolution is the missing piece, supplementary where it is not.

## The claimed saving, stated precisely

The authors do **not** claim the four-hour investigation becomes minutes. Humans still assess the
evidence and write the fix; the saving is the **context-assembly work — roughly an hour or two of
the four** in the worked example. Ranked hypotheses carry their supporting evidence precisely
because they are sometimes wrong. That keeps the human as approver (one of the listed principles)
and is consistent with the hand-off boundary in [AI SRE](../sre/ai-sre-and-the-incident-path.md):
investigation is automated, remediation is not — though Netflix lists targeted rollbacks, traffic
shifts and eventually self-healing as planned.

## Design principles (from the article)

1. Model identity before anything else.
2. Treat the ontology as code — versioned, reviewed, tested.
3. Separate concepts from instances.
4. Build on open standards.
5. Constrain stochastic tools with a type system.
6. Make enrichment best-effort and ordered.
7. Model human reasoning alongside machine telemetry.
8. Keep humans as approvers.

## Relationship to other notes

- [Netflix's Service Topology at Scale](netflix-service-topology.md) — the system that discovers
  dependency edges; this one gives those edges typed identities and joins them to everything else.
- [AI SRE and the Incident Path](../sre/ai-sre-and-the-incident-path.md) — the agent-side view of
  the same problem; this is the data layer that makes its *orientation* stage cheap.
- [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) — the
  "knowledge graphs are supplementary" position this case argues against, within limits.
- [Reactive Reducer Orchestration](../reading/reactive-reducer-orchestration.md) and
  [Long-Horizon Agents and Durable Execution](../reading/durable-execution-for-agents.md) — the
  other two placements of the determinism constraint.
- [Uber's MCP Gateway](uber-mcp-gateway.md) — Uber's Context Graph/Cortana maps code, services and
  engineers for agent decisions; the nearest analogue in these notes, held there only as a line.
- [Open Knowledge Format](../standards/open-knowledge-format.md) — the RDF-like linking this
  repository itself uses; Netflix's is the formal version, with SHACL doing what this repo's linter
  does.
