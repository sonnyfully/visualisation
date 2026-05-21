# ROADMAP.md

Progress-based, not time-based. Each stage produces a concrete, visible artifact. Don't move on until the current stage's artifact exists and works. Skipping ahead is how this project becomes a half-built mess.

Each stage lists: the goal, what the deliverable looks like, the PRs that compose it, and a "done when" gate.

---

## Stage 0 — Project scaffolding

**Goal:** repo exists, conventions are in place, an agent (Codex) can be pointed at it and know what to do.

**Deliverable:** A repo on GitHub with `AGENTS.md`, `docs/CONTEXT.md`, `docs/ARCHITECTURE.md`, `docs/decisions.md`, `docs/reading-list.md`, `README.md`, `.gitignore`, `pyproject.toml`. Python env reproducible. `main` protected. First decision entry written: "Unreal over TouchDesigner — chose for aesthetic ceiling, accept ramp cost."

**PRs:**
- `docs/initial-scaffold` — all the markdown files
- `chore/python-env` — pyproject.toml with Python 3.12+, librosa, numpy, pandas, matplotlib, pytest, ruff, black, pydantic, Jupyter
- `chore/git-hygiene` — .gitignore (audio files, Unreal binaries, `__pycache__`, `.venv`), branch protection on main, PR template

**Done when:** you can clone the repo on a different machine, run `pip install -e .`, and the test suite (empty but runnable) passes. Codex pointed at the repo correctly summarizes the project from AGENTS.md alone.

---

## Stage 1 — Audio in, plotted out

**Goal:** the Python side can load an audio file, run basic analysis, and produce trustworthy plots. This is the "hello world" that proves the loop works before any DSP claims are made.

**Deliverable:** Pick the target track. Load it. Plot waveform, spectrogram, RMS envelope. All in a notebook that re-runs end-to-end against the track. The notebook is documentation, not just exploration.

**PRs:**
- `feature/audio-loader` — `src/audio/loader.py` with `load_audio(path) -> (samples, sr)`. Single source of truth for sample rate in `src/audio/config.py`. Tests on a synthetic sine wave.
- `feature/basic-features` — `src/audio/features.py` with RMS, spectral centroid, spectral flux, spectral rolloff. Plotted against waveform in `notebooks/01-audio-loading.ipynb`.
- `feature/track-pick` — `decisions.md` entry naming the target track and *why*. Audio file in `data/tracks/` (gitignored).

**Done when:** the notebook re-runs end-to-end on the target track. Every feature plotted has a sentence in the notebook explaining what it shows musically (not just mathematically). You can point at the spectral flux curve and say "those peaks are the kick hits."

---

## Stage 2 — Event-level features: onsets, beats, downbeats

**Goal:** the Python side can detect what's *happening* in the track at event resolution. This is where the project starts having actual MIR depth rather than just spectral plots.

**Deliverable:** Onset times, beat times, downbeat times, with confidence values, all aligned to and verifiable against the waveform. Multiple onset methods compared.

**PRs:**
- `research/foote-onset-tutorial` — synthesized notes in `docs/research/bello-2005-onset-tutorial.md` *before* writing code. This is the pattern check.
- `feature/onset-detection` — `src/audio/onsets.py` with at least two methods (spectral flux and complex domain, both from Bello). Plotted overlay on waveform in `notebooks/02-onset-detection.ipynb`.
- `research/downbeat-tracker-selection` — compare modern downbeat-tracking options such as Beat This and Essentia against the project constraints. Include why `madmom` was rejected for the base environment.
- `feature/beat-tracking` — `src/audio/beats.py` with a `librosa` beat baseline and the selected downbeat tracker. Outputs beat times, downbeat times if available, BPM estimate, and confidence where the chosen method supports it.

**Done when:** for the target track, you can list every onset and every beat and the list matches what you'd tap. The downbeat estimate is correct (verify by counting "1, 2, 3, 4" against the playback). If the downbeat is wrong, that's a real finding — log it in `decisions.md` and decide whether to fix or work around.

---

## Stage 3 — Structural segmentation: the section-level

**Goal:** the Python side knows the *structure* of the track — intro, verse, build, drop, breakdown — not just the moment-by-moment features. This is the section where the project's thesis actually starts paying off.

**Deliverable:** A novelty curve, section boundaries, and (ideally) section labels for the target track. Implemented from scratch following Foote 2000, with `librosa.segment` primitives or another maintained package used for comparison.

**PRs:**
- `research/foote-2000-novelty` — synthesized notes. Implementation plan included.
- `feature/self-similarity-matrix` — `src/audio/structure.py` with SSM computation from chroma features. Plotted as image in `notebooks/04-structure.ipynb`.
- `feature/foote-novelty` — checkerboard-kernel correlation along the SSM diagonal, producing a novelty curve. From-scratch implementation. Compared visually to the audio.
- `research/structure-tool-selection` — decide whether a maintained package is useful for comparison, or whether `librosa.segment` primitives are enough.
- `feature/structure-comparison` — compare the from-scratch implementation to the selected maintained baseline. Do not add legacy dependencies that break Python 3.12+.

**Done when:** the section boundaries align with how *you* hear the track. Where they don't align, you can articulate why (e.g. "the algorithm split the breakdown because the timbre changed but I hear it as one section"). That articulation is the actual research output of this stage.

---

## Stage 4 — The data contract: timeline schema and bridge layer

**Goal:** Python output is in a stable, validated format that something else can consume. This is the first stage where the project stops being a notebook collection and becomes a *system*.

**Deliverable:** A versioned `TimelineV1` schema, exporters to JSON and CSV, validators that catch garbage, and a complete timeline file for the target track.

**PRs:**
- `feature/timeline-schema` — `src/bridge/schema.py` with pydantic models matching the multi-timescale design in `ARCHITECTURE.md` (samples / beats / phrases / sections).
- `feature/timeline-export` — `src/bridge/exporters.py` writing JSON (dev-friendly) and CSV (Unreal-Sequencer-friendly). Output to `data/outputs/<track-slug>/`.
- `feature/timeline-validators` — `src/bridge/validators.py` asserting no NaNs, monotonic timestamps, expected ranges. Runs on every export.
- `schema:v1-finalize` — version-bump PR. Schema is now stable; further changes require a `schema:v2` PR.

**Done when:** running one command produces a complete, validated timeline file for the target track. The JSON is human-readable enough that you can sanity-check it by eye. The schema is locked — any further changes are versioned.

---

## Stage 5 — Unreal: the still frame that hits

**Goal:** prove the visual side of the project can hit the aesthetic target, *without* audio reactivity yet. Taste calibration before connection.

**Deliverable:** An Unreal scene that renders a single still frame approximating the look of a Batman 2022 or Kissland reference still. Side-by-side comparison committed to `docs/aesthetic/`.

**PRs:**
- `docs/aesthetic-references` — 5 reference stills with teardown notes (lens, lighting, color grade, movement implied, post). This *precedes* opening Unreal.
- `unreal/scene-scaffold` — Unreal project initialized in `unreal/`. Lumen, basic post-process volume, one camera, one light, one geometry block. `unreal/README.md` explains how to open.
- `unreal/post-process-pass` — bloom, chromatic aberration, film grain, lens distortion, deep color grade toward orange/teal/black. Tuned to the reference stills.
- `unreal/first-still` — Movie Render Queue export of one still. Side-by-side with the chosen reference in `docs/aesthetic/teardowns/`.

**Done when:** the rendered still and the reference still can sit next to each other without obvious tier mismatch. If they can't, the audio reactivity layer won't save it — stay in this stage until the look is there.

---

## Stage 6 — First connection: feature curves into Sequencer

**Goal:** Python timeline data drives one visual parameter in Unreal. The simplest possible end-to-end loop.

**Deliverable:** A short (15–30 second) section of the target track rendered with one visual parameter (e.g. fog density, or a light's intensity, or camera Z position) driven by one feature curve (e.g. RMS, or section-boundary novelty).

**PRs:**
- `unreal/sequencer-csv-import` — Unreal-side code or Blueprint that reads a CSV from `data/outputs/<track>/` and binds a column to a Sequencer track.
- `unreal/first-driven-parameter` — bind one curve to one parameter. Pick deliberately: RMS → fog density is a sensible first pairing.
- `unreal/first-clip` — 15–30 second render of the track section with the parameter driven. Committed (or linked, given file size) and shown in `docs/aesthetic/clips/`.

**Done when:** the rendered clip is *better* than a constant-parameter render of the same scene. Subtly is fine — drama is not the goal here. The goal is "proof that the pipeline works end-to-end." If the driven version isn't better, debug the mapping, not the engine.

---

## Stage 7 — Multi-timescale mapping: where the thesis lives

**Goal:** different visual systems respond to different timescales. This is where "emotional contour, not amplitude" stops being a slogan and becomes code.

**Deliverable:** A full pass on the target track where particle behavior responds to sample-level features, camera moves respond to phrase boundaries, and lighting state changes respond to section boundaries. All from the same `TimelineV1` file.

**PRs:**
- `unreal/particle-system-rms` — Niagara particles whose emission rate or motion responds to sample-level features (RMS, flux).
- `unreal/camera-phrase-mapping` — camera movement that arrives with phrase boundaries. Slow when energy is low, lateral movement when energy ramps.
- `unreal/section-state-changes` — discrete lighting/atmosphere changes at section boundaries. A new state per section. Hard cuts and soft transitions both available.
- `research/farbood-tension-timescales` — synthesized notes on Farbood & Upham 2013. The "different timescales for different features" insight in this paper is the conceptual backbone of this stage; the note must precede the work.

**Done when:** playing the track with the visuals, a friend who hasn't heard it before can correctly identify when sections change without seeing a timeline. That's the perceptual test. If they can't, the mapping isn't there yet — iterate, don't move on.

---

## Stage 8 — The full piece: target-track render

**Goal:** one complete generative music video for the target track. Start to finish. 3–5 minutes. The September deliverable from `CONTEXT.md`.

**Deliverable:** A rendered MP4 of the full track with composed visuals. Watchable as a piece. Sharable.

**PRs:**
- `unreal/full-track-sequencer` — Sequencer extended to the full track. Section-by-section composition.
- `unreal/scene-variations` — at least three distinct visual "states" or environments that the section-level system can move between. Not three separate scenes — one scene with three configured states.
- `unreal/final-render` — Movie Render Queue full render. MP4 in releases / linked from `docs/clips/`.
- `docs/postmortem-stage-8` — written postmortem: what worked, what didn't, what the next track should change. This is the entry-point for Stage 9.

**Done when:** the video is shareable without caveat. If you'd preface sharing it with "okay so it's not really finished but," it's not done. The goal isn't perfect — it's *coherent*.

---

## Stage 9+ — Where the work goes next

Not stages yet. Possible directions, listed for orientation, not commitment:

- **Second track, different aesthetic register** — proves the system isn't single-track-overfitted.
- **Tension-curve mapping** — implement TenseMusic-style continuous tension and bind it to a meta-parameter (atmosphere intensity, lens haze). The "emotional contour" thesis at its most direct.
- **Real-time / OSC path** — when (and only when) live performance is on the table.
- **Neural rendering / latent diffusion conditioned on audio features** — the long-horizon research direction. Park until Stage 8 has actually shipped.
- **Producer-tool spin-off (Track 2)** — if the audio-side infrastructure suggests a tool worth selling, this is where it becomes a real branch of work.

Decide between these when Stage 8 is done. Don't pre-commit.

---

## Working principles for the roadmap

- **No stage skipping.** Each stage's "done when" gate is the contract. If you're tempted to skip a stage, that's the project's most important signal that something is unclear — surface it in `decisions.md`.
- **PRs match stages, not days.** A stage might take a week or four. The unit is the deliverable, not the time.
- **Postmortems on hard stages.** After Stages 3, 7, and 8 specifically — write a `docs/postmortem-stage-N.md`. What was harder than expected, what was easier, what the assumptions in `CONTEXT.md` should be updated to reflect.
- **The roadmap is a living document.** Update this file when a stage's scope sharpens. Append a `## Changelog` section at the bottom if changes start happening often.
