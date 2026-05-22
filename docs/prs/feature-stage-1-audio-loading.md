# PR: Stage 1 Audio Loading And Basic Feature Plots

## What Changed

Implement the Stage 1 Python audio loop: load a local target track, compute basic frame-level features, and plot waveform, spectrogram, RMS, spectral centroid, spectral flux, and spectral rolloff in `notebooks/01-audio-loading.ipynb`.

Add deterministic tests around synthetic sine-wave loading and feature extraction, keeping sample rate and frame settings centralized in `src/audio/config.py`.

## Why

The project needs a trustworthy "audio in, plotted out" baseline before any onset, beat, structure, or Unreal mapping work can be trusted.

## Considered And Rejected

Hard-coding paths inside the notebook was rejected because local audio is gitignored and collaborator-specific. The notebook instead uses a single `TRACK_PATH` value and fails early with a clear message when the file is absent.

Adding new MIR dependencies was rejected because Stage 1 can be completed with the existing decided stack: `librosa`, NumPy, Pandas, and Matplotlib.

## How It Was Tested

- Run the pytest suite.
- Run ruff.
- Run black check.
- Execute `notebooks/01-audio-loading.ipynb` end-to-end after placing the local target track at the expected path.

## Follow-Ups

- Add the local target audio file under `data/tracks/`; it remains intentionally ignored by Git.
- Use the plotted spectral flux curve as the visual sanity check before starting Stage 2 onset detection.
