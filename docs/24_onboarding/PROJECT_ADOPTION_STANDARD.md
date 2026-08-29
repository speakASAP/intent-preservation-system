# IPS Project Adoption Standard

This standard defines how an Alfares repository adopts the Intent Preservation
System without copying the complete IPS framework into every project.

## Ownership model

The central
[`intent-preservation-system`](https://github.com/speakASAP/intent-preservation-system)
repository owns reusable standards, schemas, templates and validators.

Each adopting repository owns its project-specific intent and evidence:

- constitution and vision;
- business and system contracts;
- architecture decisions and integration contract;
- project invariants;
- goals, features, tasks and execution plans;
- validation reports and validation debt;
- active task and state files.

Do not copy central standards into service repositories. Copying creates
independent versions that drift. Link to the central version and pin the
adoption profile to a reviewed IPS Git revision.

## Required profile

Every newly created Alfares service must contain `ips-adoption.json`, based on
[`IPS_ADOPTION_PROFILE_TEMPLATE.json`](../18_templates/IPS_ADOPTION_PROFILE_TEMPLATE.json).

The profile declares:

- project identity and profile;
- the central IPS repository and reviewed revision;
- paths to local intent, governance, task, plan and validation artifacts;
- a decision for every ecosystem integration capability;
- the bootstrap task's traceability chain.

## Required local artifacts

For a new runtime service:

```text
BUSINESS.md
SYSTEM.md
AGENTS.md
AGENT_OPERATIONS.md
TASKS.md
STATE.json
docs/00_constitution/CONSTITUTION.md
docs/01_vision/VISION.md
docs/06_architecture/INTEGRATION_CONTRACT.md
docs/11_tasks/TASK-001-bootstrap-service.md
docs/12_validation/VAL-TASK-001-bootstrap-service.md
docs/17_governance/PROJECT_INVARIANTS.md
docs/21_execution_plans/EP-TASK-001-bootstrap-service.md
docs/22_goal_impact/GOAL-IMPACT-TASK-001.md
docs/orchestrator/VALIDATION_DEBT.md
```

Use the central templates as source material, but the resulting documents must
describe the project rather than the IPS framework.

## Integration review

Every capability listed in the profile template must be reviewed. A decision is
either:

- `required`: the project needs the capability and documents its contract,
  configuration, failure mode and validation; or
- `not-applicable`: the capability is unnecessary and the profile explains why.

This is a completeness gate, not a mandate to connect every service. The goal
is deliberate interconnection without accidental coupling.

Any new ecosystem capability added to the canonical new-service contract must
be added to the profile validator in the same change.

## Validation

Run from the adopting repository:

```bash
python3 ../intent-preservation-system/scripts/validate_adoption_profile.py --root .
```

The validator is dependency-free and checks profile structure, required local
artifacts, the bootstrap traceability chain and the complete integration review.

Operational IPS gates scan the adopting repository by default. If a repository
contains a derived or generated documentation tree that is validated at its
authoritative source, list its repository-relative path in `.ipsignore`, one
path prefix per line. Blank lines and `#` comments are allowed. Do not exclude
project-owned intent, task, plan, integration or validation artifacts merely to
make a gate pass.

The Alfares new-service deploy template sets `IPS_ADOPTION_REQUIRED=1`. The
shared deploy runner executes this validator during preflight. Existing
services are not retroactively blocked until they intentionally enable the
flag.

## Protected intent

Agents cannot:

- create or change human intent to make a gate pass;
- modify a protected constitution or vision without a human-approved amendment;
- mark an integration `not-applicable` without a project-specific reason;
- remove task-to-goal or validation traceability;
- authorize their own deployment by editing policy during the current task.

Deployment authorization must be pre-existing, human-approved project or
ecosystem policy. Agents may execute within that policy but may not create the
authorization they rely on.

## Adoption completion

Adoption is complete only when:

1. the profile validator passes;
2. required integrations are implemented and validated;
3. the bootstrap validation report links evidence;
4. repository agent instructions link this standard;
5. the service is registered in the ecosystem repository catalog and map;
6. docs-RAG indexes the repository directly from Git.
