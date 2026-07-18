# WebInvestigator Architecture Handbook

The WebInvestigator Architecture Handbook documents the architectural philosophy behind the framework.

Unlike the Architectural Decision Records (ADRs), which document individual architectural decisions, the handbook presents the concepts, principles and reasoning that shape the architecture as a whole.

The handbook is intended to be read sequentially. Each chapter builds upon concepts introduced in previous chapters, gradually explaining not only how the architecture works, but why it was designed that way.

---

# Table of Contents

## Part I — Foundations

- [01. Preface](01-Preface.md)
- [02. Origin of the Project](02-Origin_of_the_Project.md)
- [03. Project Vision](03-Project_Vision.md)
- [04. Overall Architecture](04-Overall_Architecture.md)
- [05. Project Structure](05-Project_Structure.md)

---

## Part II — Core Architecture

- [06. The Investigation Pipeline](06-The_Investigation_Pipeline.md)
- [07. The Domain Model](07-The_Domain_Model.md)
- [08. The Analyzer Architecture](08-The_Analyzer_Architecture.md)
- [09. AnalysisResult](09-AnalysisResult.md)
- [10. Output Isolation](10-Output_Isolation.md)

---

## Part III — Design Principles

- [11. Loose Coupling and Dependency Management](11-Loose_Coupling_and_Dependency_Management.md)
- [12. Separation of Responsibilities](12-Separation_of_Responsibilities.md)
- [13. Abstraction Before Experience](13-Abstraction_Before_Experience.md)
- [14. Error Handling and Failure Philosophy](14-Error_Handling_and_Failure_Philosophy.md)
- [15. Configuration as Architecture](15-Configuration_as_Architecture.md)

---

## Part IV — Engineering Practices

- [16. Testing as Architectural Protection](16-Testing_as_Architectural_Protection.md)
- [17. Logging and Observability](17-Logging_and_Observability.md)
- [18. Performance Without Premature Optimization](18-Performance_Without_Premature_Optimization.md)
- [19. Designing for Parallelism](19-Designing_for_Parallelism.md)
- [20. Extensibility Without Complexity](20-Extensibility_Without_Complexity.md)

---

## Part V — Architecture Evolution

- [21. API Stability and Evolution](21-API_Stability_and_Evolution.md)
- [22. Refactoring as a First-Class Citizen](22-Refactoring_as_a_First-Class_Citizen.md)
- [23. Software Entropy](23-Software_Entropy.md)
- [24. Technical Debt vs Architectural Debt](24-Technical_Debt_vs_Architectural_Debt.md)
- [25. Architectural Smells](25-Architectural_Smells.md)
- [26. Mistakes We Intentionally Avoided](26-Mistakes_We_Intentionally_Avoided.md)

---

## Part VI — Architectural Governance

- [27. Architectural Decision Records](27-Architectural_Decision_Records.md)
- [28. When to Say No](28-When_to_Say_No.md)
- [29. Evolving Without Losing Identity](29-Evolving_Without_Losing_Identity.md)

---

## Part VII — Beyond the Architecture

- [30. AI as a Tool, Not an Architect](30-AI_as_a_Tool_Not_an_Architect.md)
- [31. Architecture Beyond Its Authors](31-Architecture_Beyond_Its_Authors.md)
- [32. The Next Architect](32-The_Next_Architect.md)

---

# Reading the Handbook

The handbook is designed to be read from beginning to end.

Each chapter introduces concepts that are expanded upon in later chapters. While individual chapters can be consulted independently, reading the handbook sequentially provides the complete architectural rationale behind WebInvestigator.

The handbook is intended to evolve slowly.

Architectural decisions are first captured as Architectural Decision Records (ADRs). Once those decisions become established and shape the long-term philosophy of the framework, they may be incorporated into future revisions of the handbook.

The handbook is not intended to document every change, but to preserve the architectural principles that remain true as the project evolves.