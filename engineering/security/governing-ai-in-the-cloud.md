---
title: Governing AI in the Cloud
tags: [security, ai-engineering, governance, reading]
topic: engineering/security
status: notes
level: intermediate
related:
  - engineering/security/secure-sdlc.md
  - engineering/practices/team-topologies-agentic-platform.md
  - engineering/architecture/design-systems-ai-control-plane.md
source: "https://www.infoq.com/articles/governing-ai-cloud-guide/"
updated: 2026-07-05
---

# Governing AI in the Cloud

Part of InfoQ's *Securing the AI Stack* series. The argument: most organisations have no
inventory of the AI integrations already running in their cloud, and traditional security
models — which assume visibility into deployed systems — break when AI runs across personal
accounts, proofs-of-concept, and embedded developer tools. Effective governance therefore
comes from **systematic discovery, classification at creation, infrastructure-level
enforcement, and policy-as-code** wired into developer workflows, not post-deployment review.

The article cites a survey claiming **71% of UK employees used unapproved AI tools** (51%
weekly) — a figure worth attributing to the source rather than treating as established.

## Shadow AI

**Shadow AI** is unauthorised AI tool usage and deployment — the AI-era analogue of shadow
IT. It widens the attack surface precisely because no one has counted it. This mirrors the
*industrialised shadow IT* risk that the
[Team Topologies for the Agentic Platform](../practices/team-topologies-agentic-platform.md)
note addresses from the organisational side; this note is the **technical-controls** side.

## A layered control architecture

The guide stacks controls so that no single blind spot is load-bearing.

### 1. Discovery — visibility precedes control

| Mechanism | Reveals |
|---|---|
| **CASB** (Defender for Cloud Apps, Netskope, Prisma Access) | Calls to external providers (`api.openai.com`, `api.anthropic.com`, `huggingface.co`, Azure OpenAI) |
| **Service-mesh telemetry** (Istio, Linkerd, App Mesh) | Self-hosted models inside Kubernetes clusters |
| **API-gateway logs** (API Gateway, Kong, Apigee) | Traffic patterns through network chokepoints |

Each addresses a different blind spot; aggregate all three into one SIEM/dashboard. Run CASB
in **alert-only mode for ~30 days** before enforcing.

### 2. Classification at write time

Tag data automatically **at object creation** (Macie, Purview, Google DLP; real-time via a
Lambda-on-S3-upload calling Amazon Comprehend for PII). Classifying at write closes the
exposure window in which untagged sensitive data could reach a model before an overnight scan
runs. A metadata shape:

```
DataClassification | ContainsPII | AIApproved | ScanDate | ComplianceScope
```

Scheduled scans (Macie) then catch **classification drift** — tagging that degrades over time.

### 3. Infrastructure-layer enforcement

Block unauthorised access at the **storage layer** with fail-secure IAM deny policies and VPC
endpoints — the author's claim is that infrastructure controls scale better than model-level
ones because they hold regardless of how many new AI endpoints appear. Five control points:

- Require classification tags on upload.
- Deny reads without a classification.
- Deny reads unless `AIApproved = true`.
- Allow only registered service roles through VPC endpoints.
- Absolute prohibition on `Restricted`-classified data reaching models.

**Fail-secure**: deny by default; only explicit approval grants access.

### 4. Policy-as-code

Static IAM cannot express contextual conditions, so evaluate them in a policy engine — **Open
Policy Agent** (Rego), **AWS Cedar**, or **HashiCorp Sentinel**. Rules chain conditions like:
principal is an AI service, classification ≠ Restricted, `AIApproved`, data within its
retention window, model registered and approved, production requirements met.

**Break-glass**: an emergency path (on-call approver + approval within 30 minutes) that grants
access *with a full audit trail* rather than a silent bypass.

### 5. Operational layer

- **Model registry** as a Kubernetes-native `AIModel` CRD capturing **data provenance**
  (which datasets and scan dates produced the model), approval chains, monitoring
  requirements (drift, explainability), and access constraints. **Kyverno** for simple
  validation, **OPA Gatekeeper** for complex admission logic.
- **Governance as production metrics** — expose violations alongside latency/errors:
  `ai_model_data_access_denied_total{model, reason}`, `ai_model_drift_score`,
  `ai_model_last_security_scan_timestamp`. Governance breaches become incidents.
- **Monitoring**: 30-day raw logs for investigation, 1-year aggregates for trends; sample
  high-volume endpoints (1/100), switch to full capture on anomalies.

### Risk-based approval pathways

Graduated escalation keyed to a calculated risk score, so approvals don't become a delivery
bottleneck:

| Risk score | Path |
|---|---|
| **Low (<3)** | Automatic approval, monitoring required |
| **Medium (3–7)** | Automated security scan; escalate on failure |
| **High (>7)** | Human governance-board review |

Retention windows follow the same **data-minimisation** logic — e.g. internal analytics
unrestricted, customer data ≤ 90 days, production models requiring a security scan within 7
days plus monitoring and explicit approval.

## Product mindset for governance

The recurring theme: **the secure path must be simpler than the insecure one**. Wrapper
libraries (a `SecureS3Client` that tags, encrypts, and routes to staging/training buckets),
staging workflows, and automatic tagging make compliance the path of least resistance rather
than an obstacle course — otherwise developers route around it and recreate shadow AI.

## Relationship to other notes

- **[Secure SDLC (DevSecOps)](secure-sdlc.md)** — the sibling security note, but focused on
  *securing the delivery pipeline* (shift-left SAST/SCA/SBOM gates). This note governs
  *running AI systems and their data access* at the cloud/runtime layer.
- **[Team Topologies for the Agentic Platform](../practices/team-topologies-agentic-platform.md)**
  — the organisational side of the same problem (who owns guardrails, application governance
  vs shadow IT); this is the technical-controls implementation (IAM, OPA, classification).
- **[Design Systems as the AI Control Plane](../architecture/design-systems-ai-control-plane.md)**
  — the "control plane / constraint layer for AI" idea realised at the UI layer; here the
  same constraint-layer principle operates at the data and infrastructure layer.
