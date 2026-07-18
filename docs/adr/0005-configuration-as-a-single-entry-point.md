# ADR-0005
# Configuration as a Single Entry Point

> **This ADR centralizes application configuration to provide a single, predictable source of architectural settings.**

**Status:** Accepted

**Date:** 2026-07-18

---

## Context

WebInvestigator relies on numerous configuration values, including investigation paths, output locations, feature toggles and execution parameters.

As the framework grows, allowing individual modules to define or retrieve their own configuration independently would lead to duplicated constants, inconsistent defaults and hidden dependencies.

Configuration scattered throughout the codebase also makes deployments more difficult and increases the risk of subtle inconsistencies between components.

A single architectural entry point for configuration was therefore required.

---

## Decision

All application-wide configuration is defined in a dedicated configuration module.

Components requiring configuration values obtain them from this centralized source rather than defining local constants or reading configuration independently.

Configuration values describe the environment in which the framework executes.

They do not contain business logic or influence architectural responsibilities.

Modules remain responsible for using configuration values, not defining them.

---

## Consequences

### Positive

- Configuration remains consistent throughout the framework.
- Default values are defined in a single location.
- Environment-specific settings can be managed without modifying business logic.
- Contributors know exactly where application settings are defined.
- Configuration changes do not require searching the entire codebase.

### Negative

- The configuration module becomes a shared dependency for many components.
- Poor organization of configuration values could eventually make the module difficult to navigate.

### Trade-offs

The project accepts a centralized configuration component in exchange for improved consistency and reduced duplication.

Centralization is considered preferable to allowing independent configuration mechanisms to emerge throughout the codebase.

---

## Alternatives Considered

### Local Module Configuration

Each module could define its own configuration values.

This approach was rejected because duplicated defaults and inconsistent naming conventions would inevitably appear as the framework expanded.

Configuration ownership would become unclear.

### Direct Environment Access

Modules could read environment variables or command-line arguments directly.

This approach was rejected because application behavior would become distributed across multiple components.

Testing would become more complicated and architectural boundaries would become less explicit.

### Multiple Configuration Files

Different subsystems could maintain separate configuration files.

This approach was rejected because it fragments configuration management and makes it more difficult to understand the overall execution environment.

---

## Related Handbook Chapters

- Chapter 05 — *Project Structure*
- Chapter 15 — *Configuration as Architecture*
- Chapter 20 — *Extensibility Without Complexity*
- Chapter 22 — *Refactoring as a First-Class Citizen*