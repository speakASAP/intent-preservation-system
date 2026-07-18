# Context Package: TASK-005 Safe Draft Remediation

## Target task

TASK-005: `../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md`

## Upstream traceability

```text
VISION -> SYS-003 Audit Engine -> FEAT-001 Documentation Audit -> TASK-005
```

TASK-005 is governed by `../22_goal_impact/GOAL-IMPACT-TASK-005.md` and implemented through `../21_execution_plans/EP-TASK-005.md`.

## Included documents

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- `../04_systems/SYS-003-audit-engine.md`
- `../10_features/FEAT-001-documentation-audit.md`
- `../11_tasks/TASK-005-propose-and-generate-missing-document-drafts.md`
- `../21_execution_plans/EP-TASK-005.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-005.md`
- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`
- `../17_governance/AI_AGENT_RULES.md`
- `../18_templates/`
- `../../scripts/strict_doc_audit.py`

## Excluded documents

- Unrelated task implementation plans are excluded.
- Protected source-of-truth documents may be read for constraints but must not be modified.
- Raw production data, secrets, confidential identifiers, and real customer data are excluded from prompts, tests, examples, logs, reports, and generated drafts.

## Constraints

- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Do not invent business goals, approvals, missing source content, or traceability.
- Keep remediation template-based and approval-gated.
- Preserve existing document content when adding missing sections.
- Use explicit missing-information markers when approved source material is insufficient.
- Keep normal audit execution read-only.

## Parallel execution context

- Execution plan: `../21_execution_plans/EP-TASK-005.md`
- Plan status: validated.
- Parallelization status: `EP-TASK-005.md` includes Parallel Execution Strategy, Goal Blockers And Dependencies, Parallel Dispatch List and Parallel Agent Handoff Prompts.
- Ready-now workstreams: `WS-005-A` implements safe remediation recommendations.
- Dependency-gated workstreams: `WS-005-D` documents workflow changes if needed; `WS-005-V` validates after implementation and documentation handoffs.
- Integration owner and merge order: validation agent integrates after `WS-005-A`, then optional `WS-005-D`, then `WS-005-V`.

## Agent prompt

Implement TASK-005 using the included context. Add a safe remediation workflow to the strict documentation audit that can plan template-based missing-document or missing-section fixes, refuses write actions without explicit approval, preserves existing content when applying approved missing-section remediation, and keeps group-level missing-document findings proposal-only.

## Validation instructions

Run focused fixture tests for remediation planning and application, then run:

```bash
python3 scripts/strict_doc_audit.py --format markdown --fail-on-issues
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-005
```
