# EP-TASK-001-bootstrap-service

completeness_level: complete

status: closed

## Upstream traceability
- `../11_tasks/TASK-001-bootstrap-service.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-001.md`
- `../12_validation/VAL-TASK-001-bootstrap-service.md`

## Scope
- Align local docs to the repository’s real standards and governance scope
- Create or update the acceptance profile and adoption artifacts
- Validate the repository against the central IPS profile rules

## Non-goals
- Deploy a runtime service
- Alter the shared IPS standard or master rollout plan
- Claim runtime dependencies the repo does not own

## Project invariants
- Honest ownership of runtime or hub responsibilities
- Clear task-to-goal-to-validation traceability
- No fabricated secret, contract, or capability evidence

## Sensitive-data handling
No secret values are introduced. The repository adoption docs describe project boundaries and governance only.

## Contract validation plan
The repo’s integration contract is reviewed for required vs not-applicable capability decisions and must remain consistent with the actual service or hub scope.

## Replay and determinism plan
The task is deterministic and re-runnable because it is based on the repo’s actual docs and the central validation rules.

## Files to inspect
- README.md
- BUSINESS.md
- SYSTEM.md
- AGENTS.md
- TASKS.md
- STATE.json
- relevant docs directory files if they already exist

## Files to create
- `ips-adoption.json`
- `docs/00_constitution/CONSTITUTION.md`
- `docs/01_vision/VISION.md`
- `docs/06_architecture/INTEGRATION_CONTRACT.md`
- `docs/11_tasks/TASK-001-bootstrap-service.md`
- `docs/12_validation/VAL-TASK-001-bootstrap-service.md`
- `docs/17_governance/PROJECT_INVARIANTS.md`
- `docs/21_execution_plans/EP-TASK-001-bootstrap-service.md`
- `docs/22_goal_impact/GOAL-IMPACT-TASK-001.md`
- `docs/orchestrator/VALIDATION_DEBT.md`

## Files to modify
- Repo-local root docs and state files that already exist

## Files that must not be modified
- `shared/config/ecosystem-repositories.json`
- The master rollout plan in the IPS repo

## Implementation steps
1. Confirm the repo’s actual standards or hub boundary.
2. Run the scaffolder for the missing IPS adoption artifacts.
3. Rewrite required sections to match the repository reality and no placeholders.
4. Set the local capability review and state file fields.
5. Validate the repository with the central IPS profile checker.

## Parallel execution
This is a single-repo onboarding task; no parallel service deployment work is included.

## Blockers
- Project owner approval evidence must remain explicit and current.
- If the repo is a standards-only or governance-only hub, the docs must be honest about that status.

## Test plan
- Run the IPS validator in planning phase
- Ensure the repo passes all required-section and integration-review checks

## Validation plan
- `python3 intent-preservation-system/scripts/validate_adoption_profile.py --root intent-preservation-system --phase planning`

## Gate commands
- `python3 intent-preservation-system/scripts/validate_adoption_profile.py --root intent-preservation-system --phase planning`

## Documentation updates
- Update the adopted repo docs and validation ledger to match actual project status.

## Rollback plan
If validation fails, revert the repo-adoption files to the last clean commit and re-run the scaffolder after correcting only the root issue.

## Handoff
The repository is left with a valid onboarding profile and explicit next action notes in the state file.

## Completion checklist
- [x] Repository scope is documented and truthful
- [x] Required adoption artifacts are present
- [x] Capability decisions are reviewable and concrete
- [x] Validator passed in planning phase
- [x] Traceability links exist across task, goal impact, execution plan, and validation docs
