# Project Constitution

Status: Immutable except by human-approved amendment  
Owner: Project Sponsor / Product Owner  
AI write access: Forbidden  
Human write access: Controlled through review

## Purpose

This document defines the laws of the project. It exists to prevent loss of intent, uncontrolled scope drift, fragmented AI-generated work and undocumented architectural decisions.

## Constitutional principles

### 1. Intent preservation

The project must preserve the original intent from the earliest idea through architecture, implementation and validation.

No task may be considered valid unless its purpose can be traced to the project vision or to an explicitly approved amendment.

### 2. Immutable source of truth

The original vision and constitution are protected documents. AI agents may read them, summarize them and reference them, but may not modify them directly.

### 3. Human-controlled change

Humans may change the original intent only through a formal amendment process. Every amendment must explain:

- what changes;
- why it changes;
- what documents are affected;
- what previous assumptions become invalid;
- which milestones, features or tasks must be updated.

### 4. Traceability

Every artifact must contain trace links.

Minimum trace chain:

```text
Vision Goal -> System -> Subsystem -> Feature -> Task -> Validation Report
```

### 5. Documentation before implementation

Code must not be generated until the relevant system, subsystem, architecture decision, task and validation criteria are documented.

### 6. Small AI execution units

Every implementation task must be small enough to be completed by one AI agent in one bounded session.

A valid AI task must have:

- one clear goal;
- limited files or modules to touch;
- explicit constraints;
- input context package;
- acceptance criteria;
- validation steps.

### 7. Context minimization

AI agents must receive only the documents needed for the current task. Irrelevant context reduces accuracy and increases hallucination risk.

### 8. Validation at every level

Every level has a Definition of Done:

- task validation;
- feature validation;
- subsystem validation;
- system validation;
- vision validation.

### 9. Decision memory

Major architecture, technology, integration and product decisions must be captured as ADRs.

### 10. Auditability

The project must be auditable at any time. The audit must reveal:

- missing documentation;
- weak requirements;
- missing validation;
- broken traceability;
- unresolved decisions;
- concept drift from the original vision.

## Amendment process

To amend this constitution or the immutable vision:

1. Create an amendment proposal in `17_governance/amendments/`.
2. Identify affected documents.
3. Explain the reason and impact.
4. Get human approval.
5. Merge through protected branch review.
6. Run audit after merge.

## Non-negotiable rules for AI agents

AI agents must not:

- modify `00_constitution/` directly;
- modify `01_vision/` directly;
- invent project goals not present in vision or amendments;
- remove validation criteria;
- ignore ADRs;
- make architecture changes without creating or updating ADRs;
- expand scope without traceability.
