# Required Project Document Set

This is the canonical document manifest for a newly onboarded Alfares runtime
service. The complete set must exist before implementation begins.

## Root project contracts

| Artifact | Purpose | Ownership and mutability | Template |
| --- | --- | --- | --- |
| `README.md` | Human entry point and links to authority | Maintained with the service; summarizes, never replaces contracts | `README_TEMPLATE.md` |
| `BUSINESS.md` | Problem, users, value, goals, non-goals and success metrics | Human-approved protected business baseline | `BUSINESS_TEMPLATE.md` |
| `SYSTEM.md` | Responsibilities, boundaries, interfaces, dependencies and validation | Technical contract; update with reviewed architecture changes | `SYSTEM_TEMPLATE.md` |
| `AGENTS.md` | Canonical repository instructions and required reading | Maintained repository policy; substantive instructions live here | `AGENTS_TEMPLATE.md` |
| `CLAUDE.md` | Claude Code compatibility entry point | Thin pointer to `AGENTS.md`; must not duplicate policy | `CLAUDE_TEMPLATE.md` |
| `AGENT_OPERATIONS.md` | Cross-agent roles, parallel work, validation debt and handoff | Maintained operational contract linked from `AGENTS.md` | `AGENT_OPERATIONS_TEMPLATE.md` |
| `TASKS.md` | Concise human-readable active/backlog/completed work | Updated at task and handoff boundaries | `TASKS_ROOT_TEMPLATE.md` |
| `STATE.json` | Machine-readable current task, lifecycle, deployment and blockers | Updated at handoff and deployment boundaries; must remain valid JSON | `STATE_TEMPLATE.json` |
| `ips-adoption.json` | Machine-readable IPS artifact and integration manifest | Validated before implementation and deployment | `IPS_ADOPTION_PROFILE_TEMPLATE.json` |

All template paths above are relative to `docs/18_templates/`.

## Protected intent and governance

| Artifact | Purpose | Template |
| --- | --- | --- |
| `docs/00_constitution/CONSTITUTION.md` | Non-negotiable project laws and amendment process | `CONSTITUTION_TEMPLATE.md` |
| `docs/01_vision/VISION.md` | Durable intended outcome, users, non-goals and success criteria | `VISION_TEMPLATE.md` |
| `docs/17_governance/PROJECT_INVARIANTS.md` | Executable constraints derived from protected intent | `PROJECT_INVARIANTS_TEMPLATE.md` |

Constitution, vision and approved business intent are protected. An agent may
structure a draft only from owner-provided or approved source material. Human
approval is required before implementation, and later changes require a
reviewed amendment.

## Bootstrap delivery chain

| Artifact | Purpose | Template |
| --- | --- | --- |
| `docs/06_architecture/INTEGRATION_CONTRACT.md` | Decisions for all ecosystem capabilities and required contracts | `INTEGRATION_CONTRACT_TEMPLATE.md` |
| `docs/11_tasks/TASK-001-bootstrap-service.md` | Bounded onboarding and implementation task | `BOOTSTRAP_TASK_TEMPLATE.md` |
| `docs/22_goal_impact/GOAL-IMPACT-TASK-001.md` | Why the bootstrap task advances approved goals | `BOOTSTRAP_GOAL_IMPACT_TEMPLATE.md` |
| `docs/21_execution_plans/EP-TASK-001-bootstrap-service.md` | Allowed files, steps, parallel lanes, validation and rollback | `BOOTSTRAP_EXECUTION_PLAN_TEMPLATE.md` |
| `docs/12_validation/VAL-TASK-001-bootstrap-service.md` | Acceptance and integration evidence | `BOOTSTRAP_VALIDATION_TEMPLATE.md` |
| `docs/orchestrator/VALIDATION_DEBT.md` | Known failures that are outside the active task | `ADOPTION_VALIDATION_DEBT_TEMPLATE.md` |

## Choosing a plan format

Use `docs/superpowers/plans/` for a single-feature, same-day-scoped change.
Every plan must begin with the metadata defined in
[`SUPERPOWERS_PLAN_FRONTMATTER_TEMPLATE.md`](../18_templates/SUPERPOWERS_PLAN_FRONTMATTER_TEMPLATE.md).

Use `docs/21_execution_plans/EP-*.md` with its `docs/11_tasks`,
`docs/22_goal_impact`, and `docs/12_validation` siblings for work that changes
a public contract, spans more than one service, or requires more than one work
session. Preserve existing plans in place during migration; do not infer a
completed status from checked boxes alone.

## Generated and optional agent files

`.github/copilot-instructions.md` is required for ecosystem repositories but is
a generated compatibility pointer, not an authoritative project document.
Create it after adding the repository to
`shared/config/ecosystem-repositories.json`:

```bash
python3 ../shared/scripts/generate-copilot-instructions.py --repo <repository>
```

Repository-local `.claude/settings.json` is optional. Add it only for concrete
Claude Code permissions or tool configuration that cannot live in `AGENTS.md`.

## Optional documents triggered by scope

Create additional documents when the system requires them:

- ADRs for architecture, technology, data ownership or integration decisions;
- subsystem documents for independently owned runtime components;
- feature documents when the bootstrap task contains multiple user-visible
  capabilities;
- data classification, migration and rollback plans for persistent data;
- API, event and schema contracts for every required integration;
- operations/runbook documents for non-obvious recovery or maintenance.

Optional means scope-triggered, not disposable. If the project has the
corresponding concern, the document is required.

## Creation and completion

Create the non-destructive skeleton:

```bash
python3 ../intent-preservation-system/scripts/scaffold_project_adoption.py \
  --root . \
  --project <repository> \
  --repository https://github.com/speakASAP/<repository>
```

The scaffolder never overwrites existing files and intentionally leaves
project decisions as `[MISSING: ...]` or profile placeholders. It does not
authorize, invent or approve intent.

Before implementation:

1. Resolve protected business, constitution and vision content from approved
   owner input and record approval evidence.
2. Complete `SYSTEM.md`, project invariants and all 16 integration decisions.
3. Complete the bootstrap task, goal impact and execution plan.
4. Keep unresolved owner decisions as explicit blockers.
5. Run the adoption validator.

```bash
python3 ../intent-preservation-system/scripts/validate_adoption_profile.py --root . --phase planning
```

A directory containing filenames but only generic filler is not complete.
Apply
[`DOCUMENTATION_COMPLETENESS_STANDARD.md`](../23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md)
to every major document.
