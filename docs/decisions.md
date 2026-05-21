# Decisions

Append-only decision log. Add dated entries for non-obvious technical, aesthetic, workflow, and schema choices.

## 2026-05-21 — Use Git Branches From The Start

Decision: initialize the repo with `main` as the stable branch and use feature branches for scoped work.

Why: the project explicitly values startup-grade Git hygiene, and even the initial scaffold should model the workflow expected later.

Alternatives considered: working directly on `main` for the empty-repo bootstrap. Rejected because it immediately breaks the repo convention and makes the first change a special case.

