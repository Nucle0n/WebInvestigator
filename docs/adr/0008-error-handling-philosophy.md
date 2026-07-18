# ADR-0008
# Error Handling Philosophy

> **This ADR establishes resilient error handling as the default behavior for all analysis workflows.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

During an investigation, analyzers may encounter corrupted files, unsupported formats, missing metadata or unexpected parsing errors.

Terminating the entire investigation because one analyzer or one artifact fails would unnecessarily reduce the value of the remaining results.

Conversely, silently ignoring failures would make investigations unreliable and difficult to diagnose.

The framework therefore required a consistent philosophy for handling failures while preserving as much useful information as possible.

---

## Decision

WebInvestigator adopts a resilient error handling strategy.

Whenever possible, failures affecting an individual artifact are isolated to that artifact.

Analyzers should continue processing the remaining investigation data after reporting the failure.

Only errors that prevent the framework itself from continuing execution may terminate the investigation.

Errors are treated as investigation results that should be reported rather than hidden.

---

## Consequences

### Positive

- A single corrupted file does not invalidate an entire investigation.
- Investigations produce the maximum amount of usable information.
- Failures become visible and diagnosable.
- Large investigations become more robust against imperfect datasets.
- Analyzer implementations remain responsible for handling expected operational failures.

### Negative

- Analyzers require additional error handling logic.
- Partial failures must be clearly distinguished from successful analyses.

### Trade-offs

The framework favors partial results over complete failure.

This increases implementation complexity but significantly improves robustness and usability during real-world investigations.

---

## Alternatives Considered

### Fail Fast

The framework could immediately terminate when an analyzer encounters an unexpected error.

This approach was rejected because a single problematic artifact would prevent the analysis of all remaining evidence.

### Silent Failure

Analyzers could ignore errors and simply skip problematic artifacts.

This approach was rejected because missing information would become difficult to detect and investigations would lose transparency.

### Global Exception Handling

A single global exception handler could absorb all failures.

This approach was rejected because it removes responsibility from analyzers and makes it more difficult to identify the origin of failures.

---

## Related Handbook Chapters

- Chapter 10 — *Failure as a First-Class Citizen*
- Chapter 18 — *Performance Without Premature Optimization*
- Chapter 24 — *Designing for Evolution*
- Chapter 26 — *Architectural Integrity*