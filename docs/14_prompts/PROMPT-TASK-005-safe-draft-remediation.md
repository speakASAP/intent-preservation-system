# Coding Prompt: TASK-005 Safe Draft Remediation

```yaml
id: PROMPT-TASK-005-safe-draft-remediation
source_task: ../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md
execution_plan: ../21_execution_plans/EP-TASK-005.md
context_package: ../13_context_packages/CP-TASK-005-safe-draft-remediation.md
status: used
```

## Role

You are an implementation agent working on a bounded documentation-audit task in the Intent Preservation System.

## Task

Implement TASK-005: safe local remediation for missing or incomplete documentation found by the strict documentation audit.

## Context

Use only the source material listed in `../13_context_packages/CP-TASK-005-safe-draft-remediation.md`, especially:

- `../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md`
- `../21_execution_plans/EP-TASK-005.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-005.md`
- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`
- `../18_templates/`
- `../../scripts/strict_doc_audit.py`

## Constraints

- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Do not invent goals, approvals, traceability, source content, or document meaning.
- Do not write remediation output during normal audit execution.
- Require explicit approval before any remediation command writes files.
- Keep missing-document group findings proposal-only unless a later approved workflow defines exact document creation.
- Preserve existing content when adding or replacing missing required sections.
- Insert explicit missing-information markers when approved source context is insufficient.

## Allowed Changes

- `../../scripts/strict_doc_audit.py`
- Focused fixture tests for strict audit remediation behavior.
- Validation documentation for TASK-005.
- Remediation workflow documentation if needed to explain approval-gated behavior.

## Forbidden Changes

- Protected baseline documents under `../00_constitution/` and `../01_vision/`.
- Unrelated execution plans, task scopes, or business-goal documents.
- Web interface code.
- Any prompt, test, example, log, report, or draft content containing secrets, raw production data, confidential identifiers, or real customer data.

## Implementation Instructions

1. Extend strict audit findings with remediation recommendations mapped to the appropriate template where possible.
2. Add a remediation-plan mode that lists proposed file creations or updates without writing files.
3. Add explicit approval gating for any apply/write mode.
4. Support approved missing-section remediation by adding missing required sections from templates while preserving existing document content.
5. Keep missing-document group findings as proposal-only actions.
6. Preserve explicit missing-information markers when source material cannot safely fill a gap.
7. Record validation evidence after the workflow and tests pass.

## Parallel Workstream Context

This prompt is a standalone single-agent prompt because `../21_execution_plans/EP-TASK-005.md` does not expose refactored parallel workstreams.

- Execution-plan status: validated.
- Parallel dispatch list: `WS-005-A` safe remediation recommendations, `WS-005-D` workflow documentation if needed, `WS-005-V` validation evidence.
- Goal blockers and dependencies: `WS-005-D` depends on final remediation behavior from `WS-005-A`; `WS-005-V` depends on implementation and documentation handoffs.
- Owned files: `../../scripts/strict_doc_audit.py`, focused remediation tests, TASK-005 validation documentation and remediation workflow documentation when needed.
- Forbidden files: `../00_constitution/CONSTITUTION.md`, `../01_vision/VISION.md`, unrelated execution plans, task scopes or business-goal documents.
- Expected handoff output: files changed, validation evidence, blockers, dependencies on other workstreams, integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- Audit can show a clear remediation plan for missing required sections.
- Normal audit and remediation planning perform no file writes.
- Write actions are refused without explicit approval.
- Approved missing-section remediation preserves existing document content.
- Placeholder section bodies can be replaced with template-derived missing-information content.
- Missing-document group findings remain proposal-only.
- Repository validation passes after implementation.

## Validation

Run the narrowest relevant fixture tests for remediation behavior, then run:

```bash
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-005
```

## Expected Output

The implementation agent must return:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining missing-information markers.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations from plan.
