# TASK-005: Propose and generate missing document drafts

```yaml
id: TASK-005
status: validated
owner: documentation-audit-agent
created: 2026-06-05
last_updated: 2026-06-12
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-003-audit-engine.md
  - ../10_features/FEAT-001-documentation-audit.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-005.md
execution_plan:
  - ../21_execution_plans/EP-TASK-005.md
validation_report:
  - ../12_validation/VAL-TASK-005-safe-draft-remediation.md
```

## Objective

Implement a safe local workflow that proposes template-based draft creation or updates for missing and incomplete documentation found by the audit.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Audit system: `../04_systems/SYS-003-audit-engine.md`
- Parent feature: `../10_features/FEAT-001-documentation-audit.md`
- Documentation completeness standard: `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- Agent gap filling rules: `../23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`

## Goal Impact

This task turns audit findings into controlled remediation while keeping humans in the approval loop and preventing AI agents from silently changing protected project intent.

## Scope

- Read strict audit findings.
- Map missing documents and missing sections to templates in `../18_templates/`.
- Present a draft-generation plan before writing files.
- Ask the user for approval before creating or updating documents.
- Create missing documents from templates when approved.
- Update incomplete documents only by adding missing sections or explicit missing-information markers when content cannot be derived from approved upstream documents.

## Non-Goals

- Do not modify `../00_constitution/` or `../01_vision/` without explicit human amendment approval.
- Do not invent business goals that are not present in upstream documents.
- Do not clone remote repositories.
- Do not build a web interface.

## Acceptance Criteria

- The command can run locally against this repository structure.
- The command shows a clear list of proposed file creations and updates.
- No document is written unless the user approves the proposal.
- Generated content preserves source paths and marks uncertain content according to the documentation completeness standard.
- Existing document content is preserved when missing sections are added.

## Required Context

- `../../scripts/strict_doc_audit.py`
- `../18_templates/`
- `../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `../23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`
- `../17_governance/AI_AGENT_RULES.md`

## Validation Task

Run the workflow against a temporary copy of this repository with one required section removed. Confirm that the workflow proposes an update, asks for approval, preserves existing content, and inserts the missing section from the appropriate template or an explicit missing-information marker.

## Execution Plan Requirement

This task requires an approved execution plan before implementation because it writes or updates repository documentation.
