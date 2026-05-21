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

## 2026-05-21 — Use Unreal Over TouchDesigner

Decision: use Unreal Engine 5.4+ as the primary visual engine instead of TouchDesigner.

Why: the aesthetic target is cinematic synthwave / neon-noir: deep blacks, practical neon, lens character, haze, slow camera language, and final renders that can sit near *The Batman* and Kissland-era references. Unreal's rendering stack, Sequencer, Niagara, Lumen, and Movie Render Queue have the aesthetic ceiling this project needs.

Alternatives considered: TouchDesigner was considered for faster visual iteration and a more native live-performance lineage. Rejected because that lineage points toward reactive VJ systems, while this project is aiming for offline, cinematic music videos first. The extra Unreal ramp cost is accepted.

## 2026-05-21 — Bootstrap Legacy MIR Packages Explicitly

Decision: document a Python environment bootstrap that installs `Cython`, `numpy`, `wheel`, and `setuptools<81` before installing `madmom` with build isolation disabled.

Why: `madmom` is an older MIR package. Its source distribution needs `Cython` during build and imports `pkg_resources` at runtime, which is no longer available from newer `setuptools` releases. Without this bootstrap, a fresh Python 3.12 virtual environment can install most of the stack but fail at the `madmom` build or import step.

Alternatives considered: dropping `madmom` for now was rejected because beat/downbeat tracking is part of the decided Stage 2 stack. Silently relying on a locally cached wheel was rejected because Stage 0 needs the setup to be reproducible on another machine.

Status: superseded by the next entry after direct import checks showed `madmom` still fails on Python 3.12 even after the bootstrap.

## 2026-05-21 — Keep The Base Environment On Modern Python

Decision: remove `madmom` and `MSAF` from the Stage 0 Python environment and require Python 3.12+.

Why: the PyPI `madmom` release does not work cleanly with the modern scientific Python stack. It needs legacy build handling, imports APIs removed from `collections`, and uses NumPy aliases removed after NumPy 1.20. `MSAF` also installs but fails to import against current SciPy. Keeping either in Stage 0 would force the project toward old Python for dependencies only needed later as comparison tools.

Alternatives considered: pinning the project to Python 3.11 or patching legacy dependencies locally. Rejected because Stage 0 should establish a clean, reproducible modern environment. Downbeat tracking and structure comparison remain important, but they should be selected in their own stages from maintained options such as Beat This, Essentia, or `librosa.segment` after explicit comparison.
