# Project Invariants

## Purpose

Project invariants are non-negotiable truths that implementation work must preserve. They translate the vision, constitution, architecture decisions and domain rules into operational checks that can run before coding and before deployment.

## Invariant levels

- `constitutional`: derived from `00_constitution/CONSTITUTION.md`; AI agents must not weaken or override it.
- `vision`: derived from `01_vision/VISION.md`; changes require the controlled vision-evolution process.
- `architecture`: derived from ADRs and architecture documents.
- `product`: derived from approved feature, task, domain or business-case documents.
- `operational`: derived from validation, data-protection, contract or deployment requirements.

## Required declaration

Each project using IPS must maintain one project-invariants document, normally at `17_governance/PROJECT_INVARIANTS.md`. If a project genuinely has no additional invariants beyond the constitution and vision, the document must state that explicitly and explain who approved the exception.

Each invariant should include:

- identifier;
- level;
- source document;
- plain-language rule;
- forbidden outcome;
- validation method;
- gate applicability;
- owner.

## Gate usage

Pre-coding gates must verify that the invariant document exists or is explicitly marked not applicable. Deployment-readiness gates must verify that applicable invariants have validation evidence in the task execution plan, validation report or readiness report.

## IPS baseline invariants

| ID | Level | Rule | Validation method |
|---|---|---|---|
| IPS-INV-001 | constitutional | Implementation work must remain traceable to upstream intent. | Task and execution-plan traceability checks. |
| IPS-INV-002 | vision | The original vision and constitution are protected from AI-agent edits. | Git diff/status check for protected files. |
| IPS-INV-003 | operational | Code generation must follow an execution plan with explicit validation. | Pre-coding gate. |
| IPS-INV-004 | operational | Validation evidence must be captured before deployment or closure. | Deployment-readiness gate. |
| IPS-INV-005 | operational | Prompts, tests, examples, logs and reports must not contain secrets or raw production data. | Sensitive-data scan. |
