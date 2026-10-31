---
type: index
title: SRE
description: "Site reliability and operations: the live incident path (including agents placed in it) and the post-incident review practices that learn from it."
tags: [meta]
status: complete
updated: 2026-10-31
---

# SRE

Site reliability and operations: incident response, on-call, reliability practice.

## Notes

### The incident path

- [AI SRE and the Incident Path](ai-sre-and-the-incident-path.md) — agents placed in the live incident rather than the review afterwards: `i = c × p` as the reason the category exists (with outside-business-hours pages nearly doubled), a seven-stage investigation pipeline that stops at **hand-off** rather than remediation, **self-confirmation** as the dominant failure and a *structurally independent* verifier as the answer — the repo's oracle-independence principle arriving in diagnosis. Plus context rot with two observable symptoms, quiet-first alerting, and evidence-based memory activation/quarantine *(paywalled before the accuracy section, so there is no evidence here that any of it works)*

### Post-incident review

- [Swarming in Incident Response](incident-swarming.md) — why spontaneous responder convergence is a feature to facilitate, not a bug to suppress, and the conditions that enable it
- [Self-Blame in Post-Incident Reviews](self-blame-in-incident-reviews.md) — why self-blame ends a review's investigation as effectively as external blame, and how facilitators redirect it toward systemic causes
- [Cognitive Diversity in Incident Reviews](cognitive-diversity-in-incident-reviews.md) — why genuinely different mental models, not identity diversity, improve reasoning about complex systems, and how to compose reviews for it
- [Heroic Saves Are Near Misses](heroic-saves-are-near-misses.md) — why a save that only worked because of luck, timing, or one specific person carries the same information as an outage, and why recognition systems quietly select for heroics over preparedness
