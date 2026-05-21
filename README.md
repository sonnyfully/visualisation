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

## Local Data

Audio files and rendered outputs are local-only and ignored by Git:

- `data/tracks/`
- `data/outputs/`

