# ADR-0006
# Offline-First Architecture

> **This ADR establishes offline operation as the default execution model for all investigation workflows.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator analyzes data that has already been collected during an investigation.

Downloaded websites, exported metadata, archived images and local evidence should remain available regardless of network connectivity or changes to external services.

Depending directly on remote resources during analysis would introduce several problems.

Investigations would become less reproducible.

Results could change over time as websites evolve.

Network availability would become an implicit execution requirement.

External services could introduce latency, rate limits or unexpected failures unrelated to the analysis itself.

The framework required a deterministic execution model that remained stable over time.

---

## Decision

WebInvestigator adopts an offline-first architecture.

Analyzers operate exclusively on locally available investigation data.

The acquisition of evidence is considered a separate concern and takes place before analysis begins.

The framework assumes that all required investigation artifacts are already present within the investigation workspace.

Any future online capabilities must remain optional and must not replace the offline execution model.

---

## Consequences

### Positive

- Investigations remain reproducible.
- Results are independent of network availability.
- Analysis performance is more predictable.
- Archived investigations can be reanalyzed years later.
- Unit tests remain deterministic because they rely on local datasets.
- Privacy is improved since investigations are processed locally.

### Negative

- External data must be collected before analysis can begin.
- Investigations do not automatically benefit from newly available online information.
- Additional tooling may eventually be required for evidence acquisition.

### Trade-offs

The project deliberately separates evidence acquisition from evidence analysis.

This introduces an additional preparation step but provides significantly greater reproducibility, stability and long-term reliability.

---

## Alternatives Considered

### Live Online Analysis

Analyzers could retrieve data directly from remote services during execution.

This approach was rejected because results would depend on network conditions and the current state of external resources.

The same investigation could therefore produce different results over time.

### Hybrid Online-First Workflow

Online resources could become the default source of information, with local files used only as a fallback.

This approach was rejected because it reverses the architectural priorities of the framework.

Local evidence represents the source of truth.

External resources should only enrich an investigation when explicitly requested.

### Mandatory Cloud Processing

Analysis could be delegated to cloud-based services.

This approach was rejected because it reduces reproducibility, introduces external dependencies and conflicts with the framework's objective of remaining usable in isolated or privacy-sensitive environments.

---

## Related Handbook Chapters

- Chapter 02 — *The Origin of the Project*
- Chapter 03 — *Project Vision*
- Chapter 06 — *The Investigation Pipeline*
- Chapter 15 — *Configuration as Architecture*
- Chapter 18 — *Performance Without Premature Optimization*
- Chapter 29 — *Evolving Without Losing Identity*