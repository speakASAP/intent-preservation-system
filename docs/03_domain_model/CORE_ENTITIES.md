# Core Entities

## Entity relationship overview

```text
VisionGoal
  -> System
    -> Subsystem
      -> Feature
        -> Task
          -> ContextPackage
          -> CodingPrompt
          -> ValidationReport

ADR -> System
ADR -> Subsystem
ADR -> Feature
Milestone -> Feature
Milestone -> ValidationReport
```

## VisionGoal

Fields:

- id;
- title;
- description;
- priority;
- success metric;
- source document.

## System

Fields:

- id;
- name;
- responsibility;
- upstream goals;
- downstream subsystems;
- interfaces;
- validation strategy.

## Subsystem

Fields:

- id;
- parent system;
- responsibility;
- inputs;
- outputs;
- dependencies;
- constraints.

## Feature

Fields:

- id;
- parent subsystem;
- user or system value;
- acceptance criteria;
- dependencies;
- validation method.

## Task

Fields:

- id;
- feature link;
- exact goal;
- allowed scope;
- forbidden changes;
- required files;
- acceptance criteria;
- validation steps.

## ContextPackage

Fields:

- id;
- target task;
- included documents;
- excluded documents;
- summary;
- constraints;
- prompt output.
