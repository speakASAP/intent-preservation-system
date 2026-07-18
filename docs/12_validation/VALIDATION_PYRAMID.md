# Validation Pyramid

## Level 1: Task validation

Question: Did the agent complete the exact task?

Checks:

- acceptance criteria met;
- no forbidden changes;
- tests or review completed;
- validation report written.

## Level 2: Feature validation

Question: Does the feature work as intended?

Checks:

- all child tasks complete;
- feature acceptance criteria met;
- edge cases reviewed;
- documentation updated.

## Level 3: Subsystem validation

Question: Does the subsystem behave correctly as a unit?

Checks:

- interfaces work;
- dependencies are satisfied;
- integration risks addressed.

## Level 4: System validation

Question: Does the system deliver its responsibility?

Checks:

- all subsystems align;
- system-level success criteria met;
- architecture still valid.

## Level 5: Vision validation

Question: Does the current project still solve the original problem?

Checks:

- no major concept drift;
- business goals still represented;
- roadmap remains coherent;
- amendments are documented.
