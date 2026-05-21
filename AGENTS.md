# AGENTS.md

Instructions for AI coding agents working in this repo. Read this first, every session.

## What this project is

Real-time generative visual systems driven by music. Aesthetic target: cinematic synthwave — *The Batman* (2022), Kissland-era Weeknd, deep neon-noir. See `docs/CONTEXT.md` for full briefing before doing any work.

## Read order for a fresh session

1. This file (`AGENTS.md`) — conventions
2. `docs/CONTEXT.md` — project thesis, aesthetic, current focus
3. `docs/ARCHITECTURE.md` — repo layout and how pieces connect
4. `docs/decisions.md` — what's been decided and why (check before proposing alternatives)
5. The current branch name and open PR — that's where work is happening

## Git workflow — non-negotiable

This project uses real Git discipline. The point is to build habits that transfer to working in a startup.

- `main` is always working. Never commit directly to main.
- One feature branch per sub-problem. Naming: `feature/onset-detection`, `fix/spectral-flux-windowing`, `research/structural-segmentation`, `docs/update-context`. Use the `feature/`, `fix/`, `research/`, `docs/`, `refactor/` prefixes.
- Write the PR description **before** starting work on the branch. If you can't describe what the PR will do in three sentences, the scope isn't clear enough yet. Stop and clarify.
- One concern per PR. If you're touching DSP and Unreal integration in the same branch, split it.
- PR description must include: what changed, why, what was considered and rejected, how it was tested, any follow-ups created.
- Squash-merge to main. Keep history clean.
- Commit messages: imperative mood, present tense. `add onset detector` not `added onset detector`.

## Working conventions

- **Ask before scope creep.** If a task reveals a deeper problem, surface it as a separate issue or PR, don't silently expand the current one.
- **Plot everything in notebooks.** DSP work without visualization is guessing. Every audio feature gets plotted against the waveform at least once before it's trusted.
- **No magic numbers.** Sample rates, hop sizes, FFT windows live in a config module with comments on why those values.
- **Decisions go in `docs/decisions.md`** when they're non-obvious. Append-only, dated.
- **Research synthesis goes in local `docs/research/` notes** as one file per paper. These notes are intentionally ignored by Git by default so they can be referenced locally without being pushed. Don't dump raw PDFs into the repo — synthesize what matters.
- **Don't pick new tools without raising it.** The tool stack is deliberately minimal. If you think a new dependency is needed, propose it in a comment on the relevant PR or as a note in `decisions.md`, don't just `pip install` it.

## Code style

- Python: type hints on all function signatures, docstrings on anything non-trivial, `ruff` for linting, `black` for formatting. Functions do one thing.
- Notebooks are for exploration only. Once a pattern stabilizes, it moves into a module in `src/`. Notebooks import from `src/`, never the other way.
- Configuration via a single `config.py` or `pyproject.toml`, not scattered constants.
- Tests for any DSP function with a deterministic output. `pytest`. Aim for the core feature extraction pipeline to have test coverage.

## What I want from you, the agent

- **Push back when I'm wrong.** If I propose a change that contradicts something in `decisions.md` or that you think is technically off, say so. Don't just execute.
- **Surface tradeoffs explicitly.** "I'm going to do X" should usually be "I'm going to do X because Y, alternative was Z, rejected because W."
- **Flag when you're guessing.** If you don't know the right sample rate, hop size, model architecture, or aesthetic call, say "I'm guessing here — should we verify?" rather than committing a guess.
- **Don't vibe-code DSP.** This project's whole point is doing the work with real backing. If you're about to write a feature extractor without a reference paper or documented technique, stop and find one first.

## What not to do

- No commits directly to main.
- No `pip install`ing new libraries without flagging it.
- No expanding PR scope mid-branch.
- No deleting things from `decisions.md` — only append.
- No dumping unsynthesized research into the repo.
- No "I'll fix it later" TODOs without a corresponding issue or note.
