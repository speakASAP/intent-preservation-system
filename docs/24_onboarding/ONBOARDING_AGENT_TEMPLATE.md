# Agent Onboarding Package

## Project purpose

[MISSING: summarize the project purpose from VISION.md]

## Immutable documents

Agents must not modify:

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Required workflow

```text
Vision -> Goal Impact -> System -> Feature -> Task -> Execution Plan -> Coding Prompt -> Code -> Validation
```

## Before starting work

The agent must verify:

- The task has upstream traceability.
- The task has goal impact mapping.
- An approved execution plan exists.
- Required context package exists or can be generated.
- Validation criteria are explicit.

## Forbidden actions

- Do not change immutable documents.
- Do not invent missing business goals.
- Do not write code directly from vague tasks.
- Do not skip validation.
- Do not modify files outside the execution plan unless reporting a deviation.

## Documentation gap handling

If required documentation is incomplete, follow:

- `23_documentation_contracts/DOCUMENTATION_COMPLETENESS_STANDARD.md`
- `23_documentation_contracts/AGENT_GAP_FILLING_RULES.md`

## Expected final output

At the end of work, the agent must provide:

- Changed files
- Validation evidence
- Documentation updates
- Deviations from execution plan
- Remaining gaps
