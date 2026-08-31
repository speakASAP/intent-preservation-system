# Superpowers Plan Frontmatter Template

Place this YAML frontmatter at the beginning of every `docs/superpowers/plans/*.md` file.

```yaml
---
status: draft
owner: repository-owner
last_updated: YYYY-MM-DD
---
```

Use `draft`, `ready`, `active`, `blocked`, `review`, `validated`, `done`,
`superseded`, `cancelled`, or `abandoned`. A plan is complete only when its
status is `done`; checkboxes track individual steps and are not a completion
signal. Use `review` when historical evidence is insufficient to truthfully
classify a legacy plan, and replace it after the repository owner verifies it.
