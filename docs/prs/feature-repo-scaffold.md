# PR: Scaffold Repository Structure

## What Changed

Create the initial repository layout from `docs/ARCHITECTURE.md`: docs vault, Python source packages, notebook area, tests, local data folders, and Unreal project placeholder.

Finish Stage 0 by adding the roadmap, reading list, Python 3.12 editable-install setup, Jupyter/dev tooling, a scaffold smoke test, and documented decisions for Unreal over TouchDesigner and modern Python over legacy MIR packages.

## Why

The repo needs a stable shape before DSP, bridge schema, notebook exploration, or Unreal integration work can proceed cleanly.

## Considered And Rejected

Starting with implementation modules first was rejected because no DSP method has been validated yet. Keeping `CONTEXT.md` and `ARCHITECTURE.md` at the repo root was rejected because `AGENTS.md` and the architecture both define `docs/` as the project knowledge base and Obsidian vault.

Keeping `madmom` and `MSAF` in the base environment was rejected after install/import checks showed their PyPI releases do not work cleanly on the modern Python 3.12 scientific stack. Downbeat tracking and structure comparison remain Stage 2/3 concerns, where maintained options such as Beat This, Essentia, and `librosa.segment` can be evaluated explicitly.

## How It Was Tested

- Created a local `.venv` with Python 3.12.12.
- Ran `python -m pip install -e ".[dev]"`.
- Ran `python -m pytest`.
- Ran `python -m ruff check .`.
- Ran `python -m black --check .`.
- Verified imports for `librosa`, `librosa.segment`, `matplotlib`, `numpy`, `pandas`, `pydantic`, `pytest`, and `ruff`.
- Verified `madmom` and `msaf` are not installed in the clean venv.

## Follow-Ups

- Create the first audio loading notebook and plot waveform output before trusting loader behavior.
- Add real tests when the first deterministic DSP function lands.
- In Stage 2, choose a maintained downbeat tracker rather than relying on `madmom`.
- In Stage 3, choose a maintained structure-comparison baseline rather than relying on `MSAF`.
