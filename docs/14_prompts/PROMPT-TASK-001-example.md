# Coding Prompt: TASK-001

```yaml
id: PROMPT-TASK-001-example
source_task: ../11_tasks/TASK-001-create-required-document-audit-rules.md
execution_plan: ../21_execution_plans/EP-TASK-001-example.md
context_package: ../13_context_packages/CP-TASK-001-example.md
status: used
```

## Role

You are an implementation agent working on a bounded task in the Intent Preservation System.

## Task

Create required-document audit rules.

## Task Summary

Implement TASK-001 by adding local required-document audit rules that detect
missing baseline documents, missing required sections and empty required
sections in IPS repository artifacts.

## Required Context

- `../13_context_packages/CP-TASK-001-example.md`
- `../11_tasks/TASK-001-create-required-document-audit-rules.md`
- `../21_execution_plans/EP-TASK-001-example.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-001-example.md`
- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../15_audits/AUDIT_CHECKLIST.md`

## Context

Use the following documents:

- Vision
- Audit Engine system document
- Documentation Audit feature
- TASK-001

## Constraints

- Do not modify protected vision or constitution files.
- Do not add unrelated features.
- Keep the output simple and testable.

## Allowed Changes

- `../../scripts/strict_doc_audit.py`
- `../15_audits/AUDIT_CHECKLIST.md`
- Documentation updates listed by `../21_execution_plans/EP-TASK-001-example.md`.

## Forbidden Changes

- `../01_vision/VISION.md`
- `../00_constitution/CONSTITUTION.md`
- Unrelated audit categories, web UI code, RAG features or risk scoring.
- Any prompt, test, example, log or report containing secrets, raw production data, confidential identifiers or real customer data.

## Implementation Instructions

1. Define required sections for auditable IPS document types.
2. Parse Markdown headings in repository documents.
3. Detect missing required headings.
4. Detect required headings whose sections are empty or placeholder-only.
5. Produce machine-readable JSON output.
6. Produce human-readable Markdown output.

## Parallel Workstream Context

This prompt is a single-agent example prompt derived from `../21_execution_plans/EP-TASK-001-example.md`.

- Execution-plan status: reviewed.
- Parallel dispatch list: `WS-001-A` audit implementation, `WS-001-D` documentation alignment, `WS-001-V` validation evidence.
- Goal blockers and dependencies: `WS-001-D` depends on final audit rule names from `WS-001-A`; `WS-001-V` depends on implementation and documentation handoffs.
- Owned files: `../../scripts/strict_doc_audit.py`, `../15_audits/AUDIT_CHECKLIST.md`.
- Forbidden files: `../01_vision/VISION.md`, `../00_constitution/CONSTITUTION.md`.
- Expected handoff output: files changed, missing sections filled, remaining unresolved missing-information markers, validation evidence and deviations.

## Acceptance criteria

- Required document categories are defined.
- Missing required files are reported.
- Output includes severity levels.
- Validation instructions are provided.

## Validation

Run the audit against a sample project with missing files and confirm that gaps are reported.

## Expected Output

The implementation agent must return:

- Files changed.
- Tests run.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations.
- Remaining documentation gaps.
