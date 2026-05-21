# Decisions

Append-only decision log. Add dated entries for non-obvious technical, aesthetic, workflow, and schema choices.

## 2026-05-21 — Use Git Branches From The Start

Decision: initialize the repo with `main` as the stable branch and use feature branches for scoped work.

Why: the project explicitly values startup-grade Git hygiene, and even the initial scaffold should model the workflow expected later.

Alternatives considered: working directly on `main` for the empty-repo bootstrap. Rejected because it immediately breaks the repo convention and makes the first change a special case.

## 2026-05-21 — Keep Research Notes Local By Default

Decision: ignore local Obsidian research notes under `docs/research/` while keeping the rest of the docs vault version-controlled.

Why: research notes should remain available to Obsidian and local coding agents without being pushed to GitHub by default.

Alternatives considered: versioning every synthesized research note. Rejected because local research notes may be exploratory, private, or too noisy for the shared repository history.
