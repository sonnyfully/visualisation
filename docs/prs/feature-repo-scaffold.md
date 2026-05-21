# PR: Scaffold Repository Structure

## What Changed

Create the initial repository layout from `docs/ARCHITECTURE.md`: docs vault, Python source packages, notebook area, tests, local data folders, and Unreal project placeholder.

## Why

The repo needs a stable shape before DSP, bridge schema, notebook exploration, or Unreal integration work can proceed cleanly.

## Considered And Rejected

Starting with implementation modules first was rejected because no DSP method has been validated yet. Keeping `CONTEXT.md` and `ARCHITECTURE.md` at the repo root was rejected because `AGENTS.md` and the architecture both define `docs/` as the project knowledge base and Obsidian vault.

## How It Was Tested

Verify the Git branch, file tree, and Python project metadata are present. No runtime DSP tests are expected for this scaffold-only PR.

## Follow-Ups

- Create the first audio loading notebook and plot waveform output before trusting loader behavior.
- Add real tests when the first deterministic DSP function lands.

