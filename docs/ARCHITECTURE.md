# ARCHITECTURE.md

How the repo is laid out and how the pieces fit together. Read this after `CONTEXT.md`.

## High-level data flow

```
   Audio file (.wav / .flac)
            │
            ▼
   ┌─────────────────────┐
   │  Python DSP layer   │   librosa, NumPy, Pandas
   │  (src/audio/)       │   onset, beat, spectral, structural
   └─────────────────────┘
            │
            ▼
   Feature timeline (JSON / CSV)
   sample-level → beat-level → phrase-level → section-level
            │
            ▼
   ┌─────────────────────┐
   │  Bridge layer       │   exporters, schema validation
   │  (src/bridge/)      │
   └─────────────────────┘
            │
            ▼
   ┌─────────────────────┐
   │  Unreal Engine 5    │   Sequencer consumes timeline data
   │  (unreal/)          │   Niagara, Lumen, post-process
   └─────────────────────┘   Movie Render Queue → final video
            │
            ▼
   Rendered music video (.mp4 / EXR sequence)
```

The split is deliberate: Python is the right tool for DSP and MIR (mature ecosystem, fast iteration in notebooks, plotting). Unreal is the right tool for cinematic real-time visuals. They communicate via a clean data contract — a timeline file with a defined schema — not via tight coupling.

## Repo layout

```
audio-visual-project/
├── AGENTS.md                  # Conventions for AI coding agents (Codex entry point)
├── README.md                  # Top-level project summary, status
├── pyproject.toml             # Python deps, ruff/black/pytest config
├── .gitignore
│
├── docs/
│   ├── CONTEXT.md             # Project briefing — read this first
│   ├── ARCHITECTURE.md        # This file
│   ├── decisions.md           # Append-only decision log
│   ├── research/              # Local ignored notes; one markdown file per paper / reference
│   │   └── <paper-slug>.md    # Link, summary, what to steal (not pushed by default)
│   └── aesthetic/             # Visual reference library
│       ├── batman-2022/       # Stills + teardown notes
│       ├── kissland/
│       └── ...
│
├── src/
│   ├── audio/                 # DSP and MIR
│   │   ├── __init__.py
│   │   ├── loader.py          # Audio file I/O, resampling
│   │   ├── features.py        # Spectral features, RMS, centroid, flux
│   │   ├── onsets.py          # Onset detection
│   │   ├── beats.py           # Beat + downbeat tracking
│   │   ├── structure.py       # Structural segmentation
│   │   ├── harmonic.py        # HPSS, chroma, key estimation
│   │   └── config.py          # Sample rates, hop sizes, FFT windows
│   │
│   ├── bridge/                # Audio → Unreal data export
│   │   ├── __init__.py
│   │   ├── schema.py          # Timeline data schema (pydantic models)
│   │   ├── exporters.py       # Write JSON/CSV for Unreal Sequencer
│   │   └── validators.py      # Sanity checks on output
│   │
│   └── viz/                   # Plotting helpers (notebook-side)
│       └── plots.py
│
├── notebooks/                 # Exploration only. Stable code → src/
│   ├── 01-audio-loading.ipynb
│   ├── 02-onset-detection.ipynb
│   ├── 03-beat-tracking.ipynb
│   ├── 04-structural-segmentation.ipynb
│   └── ...
│
├── tests/                     # pytest. DSP functions with deterministic outputs.
│   ├── test_features.py
│   ├── test_onsets.py
│   └── ...
│
├── data/                      # Audio files, not tracked in Git (see .gitignore)
│   ├── tracks/                # Source audio
│   └── outputs/               # Feature timelines per track
│
└── unreal/                    # Unreal project. May live in a separate repo later.
    ├── README.md              # How to open, what's in it
    ├── Content/               # Unreal assets (mostly Git LFS or untracked)
    └── ...
```

## Module responsibilities

### `src/audio/`

The DSP and MIR layer. Everything here is pure Python, returns numpy arrays or dataframes, and has no knowledge of Unreal. Each module owns one concern. Functions are deterministic given the same input — same audio, same config → same output.

- `loader.py` — load audio, resample to project sample rate, return mono/stereo numpy arrays. Single source of truth for sample rate.
- `features.py` — frame-level spectral features (centroid, rolloff, flux, RMS, MFCC).
- `onsets.py` — onset detection, multiple methods (spectral flux, complex domain, etc.) for comparison.
- `beats.py` — beat tracking and downbeat estimation. Start with a `librosa` beat baseline; select a maintained downbeat tracker in Stage 2.
- `structure.py` — structural segmentation. Start with from-scratch Foote-style novelty and `librosa.segment` primitives; select any external comparison library in Stage 3.
- `harmonic.py` — harmonic/percussive separation, chroma, key estimation.
- `config.py` — `SAMPLE_RATE`, `HOP_SIZE`, `FRAME_SIZE`, etc. All magic numbers live here with comments on why.

### `src/bridge/`

Translates DSP output into a stable data contract Unreal can consume. The schema is the API — Unreal-side code depends on the schema, not on Python internals.

- `schema.py` — pydantic models for the timeline format. Sample-level, beat-level, phrase-level, section-level data with timestamps.
- `exporters.py` — write JSON (for development) and CSV (for Sequencer import) files.
- `validators.py` — assert no NaNs, monotonic timestamps, expected ranges. Run on every export.

### `src/viz/`

Plotting helpers used in notebooks. Not for production output — just for sanity-checking DSP work. Matplotlib-based.

### `notebooks/`

Numbered, one notebook per exploration topic. Notebooks are scratch. The pattern: explore in notebook → once it works, extract into `src/` module → notebook imports from `src/` and demonstrates usage. Notebooks should be re-runnable end-to-end against a sample audio file.

### `unreal/`

The Unreal project. Lives inside this repo for now; may split into its own repo if it grows large enough to need its own LFS setup. Reads timeline files from `data/outputs/<track-name>/`. The Unreal side is documented separately in `unreal/README.md`.

## Data contract — the timeline schema

The bridge between Python and Unreal. Versioned. Breaking changes to this schema require a `decisions.md` entry and a PR titled `schema:` so it's obvious.

Rough shape (the real definition lives in `src/bridge/schema.py`):

```
TimelineV1
├── meta
│   ├── track_id, duration_seconds, sample_rate, bpm_estimate
│   └── schema_version
├── samples      # frame-level, hop-aligned
│   ├── timestamps[]
│   ├── rms[], centroid[], flux[], ...
│   └── chroma[12][]
├── beats        # event-level
│   ├── beat_times[], downbeat_times[]
│   └── confidence[]
├── phrases      # 4–8 bar groupings (derived)
│   └── boundaries[], energies[]
└── sections     # structural boundaries and labels
    ├── boundaries[], labels[]
    └── novelty_curve[]
```

The multi-timescale structure is intentional — it's the architecture answer to "how do visuals respond to musical structure, not just to amplitude." Different visual systems consume different timescales. Particle motion might respond to sample-level features. Camera moves respond to phrase boundaries. Lighting state changes respond to section boundaries.

## What lives outside this repo

- **NotebookLM** — raw paper collection and Q&A. Synthesized private notes can live locally in `docs/research/` as markdown.
- **Obsidian vault** — *is* `docs/`. Don't maintain a separate vault. Research notes are ignored by Git by default.
- **Audio files** — in `data/tracks/` locally, not committed to Git (copyright + size).
- **Rendered video output** — local only or external storage, not in Git.

## How a typical work session flows

1. Open repo. Codex reads `AGENTS.md` automatically. Confirm it's seen `CONTEXT.md` and `decisions.md`.
2. Check current branch and open PR. Resume from there, or start a new branch with a written-out PR description.
3. If DSP work: open relevant notebook, explore, plot, validate. Once stable, extract to `src/audio/` module with tests.
4. If Unreal work: open Unreal project, work against the latest timeline file from `data/outputs/`. Iterate in viewport, final render via Movie Render Queue.
5. PR with full description (what / why / alternatives considered / tested how / follow-ups). Squash-merge.
6. Append to `decisions.md` if anything non-obvious was decided.
