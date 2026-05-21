# Visualisation

Real-time generative visual systems driven by music, aimed at cinematic synthwave and deep neon-noir rather than generic audio-reactive graphics.

The project splits work into two deliberately separate layers:

- Python DSP and MIR analysis in `src/`
- Unreal Engine cinematic rendering in `unreal/`

The first bridge between them is offline: Python exports versioned timeline data under `data/outputs/`, and Unreal consumes that data for Sequencer-driven visuals.

## Current Status

Initial repository scaffold. See:

- `docs/CONTEXT.md` for the project thesis and aesthetic target
- `docs/ARCHITECTURE.md` for the intended module layout and data flow
- `docs/decisions.md` for append-only technical decisions
- `docs/ROADMAP.md` for staged deliverables and done gates

## Python Setup

Use Python 3.12 or newer.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

The local virtual environment is intentionally ignored by Git.

Legacy MIR packages such as `madmom` and `MSAF` are intentionally not part of
the base environment because their current PyPI releases do not import cleanly
on the modern Python stack. Beat/downbeat and structure-comparison tools will be
selected in the relevant later stages.

## Local Data

Audio files and rendered outputs are local-only and ignored by Git:

- `data/tracks/`
- `data/outputs/`
