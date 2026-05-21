# CONTEXT.md

The briefing doc. If you're an agent or a collaborator joining this project, read this end-to-end before doing anything.

## Thesis

Build real-time generative visual systems driven by music, aimed at the sensory language of immersive venues in the *Printworks / Berghain* tier. The work is a piece of craft and R&D that compounds toward a long-term venue dream, not a startup. Output by September: a working pipeline, visible artifacts (generative music videos for specific tracks), and a developed visual + technical vocabulary that maps onto the target aesthetic.

The interesting open problem isn't making visuals respond to amplitude (that's solved and boring). It's capturing the **emotional contour of music** — making visuals that feel alive rather than reactive. Cinematic, not VJ. Pacing that matches musical structure, atmosphere that thickens with builds, camera language that breathes with the track. That's the research problem worth working on.

## Aesthetic target

Cinematic synthwave / dark electronic. Specifically:

- **The Batman (2022)** — Greig Fraser's anamorphic lensing, practical neon (sodium-vapor orange, emergency red), deep blacks with selective highlights, rain as constant texture, slow deliberate camera moves.
- **Kissland-era Weeknd** — VHS degradation, chromatic aberration, scan lines, lo-fi-but-luxurious texture, neon through haze.
- **The Weeknd: Trilogy / After Hours / Dawn FM visual language** — synth-driven, atmospheric, euphoric, controlled palette.
- **Adjacent references** — Blade Runner 2049, Nicolas Winding Refn (*Drive*, *Neon Demon*), early Hotline Miami artwork.

What this is **not**: rave visuals tradition (geometric, kaleidoscopic, glitchy fractals). Not Hydra. Not Shadertoy greatest hits. Not Tarik Barri. The technical lineage is closer to cinematic real-time rendering (game engines, virtual production) than to creative coding.

Aesthetic reference library lives in `docs/aesthetic/` — stills with teardown notes (lens, lighting, color grade, movement, post-processing).

## Stack — decided

- **Visual engine: Unreal Engine 5.4+.** Lumen for global illumination, Niagara for atmospheric particles, post-process volume for lens character, Movie Render Queue for final output. Higher ramp than TouchDesigner, but the aesthetic ceiling matches the target. See `decisions.md` for the tradeoff analysis.
- **Audio analysis: Python.** `librosa` + `madmom` + `MSAF` for MIR features (onset, beat, downbeat, spectral, structural segmentation). Jupyter for exploration, modules in `src/` for stable code.
- **Audio → visual bridge: offline first.** Python produces feature curves as CSV/JSON timeline data, Unreal Sequencer consumes them. Real-time via OSC is a later concern, not week one.
- **Output format: pre-rendered generative music videos.** One track at a time, fully composed, 3–5 minutes. No live performance constraint (no hardware for it currently).
- **Coding agent: Codex.** One agent. `AGENTS.md` is its entry point.
- **Notes / research: Obsidian, vault = this repo's `docs/` folder.** Single source of truth, version-controlled. NotebookLM for paper collection and querying; synthesized notes in `docs/research/`.
- **Version control: Git, real workflow.** See `AGENTS.md`.

## Current focus

[Update this section as work progresses. Replace bracketed placeholders.]

- **Phase:** [e.g. Week 1 — engine fluency + first DSP pipeline]
- **Active branch:** [e.g. `feature/onset-detection`]
- **Track being worked on:** [specific song title and artist]
- **Open question being answered:** [e.g. "which onset detection method tracks perceived beats most accurately on synth-heavy material?"]
- **Blockers:** [none / list]

## What's been ruled out

(So we don't re-litigate.)

- TouchDesigner as primary engine — chosen against because aesthetic ceiling didn't match Batman/Kissland reference target. See `decisions.md`.
- Real-time live-performance focus — no hardware, no current need. Offline-rendered is the format.
- Frame-by-frame neural rendering as week-one target — too expensive, six-month problem. Procedural-with-audio-conditioning first.
- Generic "audio-reactive" tutorials and Hydra/Shadertoy aesthetic — wrong visual tradition for this project.
- Multi-tool agent stack (Codex + Claude Code + Cursor + ...) — chose one agent (Codex) to avoid workflow-shopping.

## Research surface

The technical depth this project needs:

- **MIR (Music Information Retrieval):** onset/beat/downbeat detection, spectral features, harmonic/percussive separation, structural segmentation (boundary detection, section labeling), musical tension/release modeling. Starting references: Müller's *Fundamentals of Music Processing*, ISMIR proceedings, Lerdahl & Farbood on tension.
- **Real-time cinematography:** procedural camera language, virtual production techniques, Unreal Sequencer-driven cinematics. Starting references: Naughty Dog / Last of Us GDC talks on cinematic real-time camera, Faucher's Unreal lighting/post tutorials.
- **Audio-visual mapping:** the open problem. How do you map structural features (not just spectral ones) to visual parameters that produce *feeling* rather than reactivity? Likely involves multi-timescale mapping (sample-level → beat-level → phrase-level → section-level).
- **Generative visual models (later):** real-time neural rendering, latent diffusion at frame rate, conditioning on audio features. Not week-one work.

Synthesized notes per paper in `docs/research/`. NotebookLM holds the raw collection.

## Long horizon

This work feeds a 7–10 year arc toward building immersive venues. Tools, taste, and technical depth developed here are the foundation. Any commercial artifact (a producer tool, a startup) is downstream and falls out of the depth, not chosen up front. See `Current update how I feel` and `Projects` notes in the broader project context for the full framing.
