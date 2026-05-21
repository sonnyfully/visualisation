# NONCODE-ROADMAP.md

Time-based companion to `ROADMAP.md`. This file lives in Obsidian and tracks what you should have read, watched, or become comfortable with by the time each repo stage is in progress or shipped.

Weeks, not calendar dates — calendar dates rot the second you slip a day, weeks flex with reality. Convert to calendar dates locally if you want, but keep the canonical version in weeks.

Each week has: **reading**, **fluency** (Unreal, Python, DSP), **aesthetic study**, and a **roadmap position** — what stage of `ROADMAP.md` you should be in or shipping by the end of the week.

If you're behind on a week, don't skip ahead — the later weeks assume the earlier reading. If you're ahead, get further into the long-horizon papers in section 4 of the reading list, or deeper into Unreal cinematography craft. Don't start Stage N+2 of the repo before Stage N+1.

---

## Week 1 — Foundations laid

**Reading**
- `docs/CONTEXT.md`, `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/reading-list.md`, `docs/ROADMAP.md` — re-read end-to-end. They're the project's constitution.
- Müller FMP **Chapter 1** (music representations) and **Chapter 2** (Fourier transform) via the free FMP notebooks. Don't read the book — run the notebooks.
- librosa paper (McFee 2015) — short, do it in one sitting.

**Fluency**
- Python env reproducible on your machine. `pip install -e .` works. Jupyter launches.
- Unreal 5.4+ installed. "Your First Hour in Unreal" official tutorial done.
- Git workflow used for the scaffolding PRs. No commits to main.

**Aesthetic study**
- Pick the target track. Listen to it 10 times with no other input. Write 1 paragraph in `docs/aesthetic/target-track.md` describing what you hear — sections, energy arcs, what you *want* the visuals to do.

**Roadmap position:** Stage 0 shipped. Stage 1 started.

---

## Week 2 — Audio in, plots out

**Reading**
- FMP **Chapter 3** (music synchronization) — skim, you mainly need the spectral feature material.
- Müller FMP **Section 6.1** (onset detection — the chapter intro material). Don't go deep yet, just the framing.
- Bello et al. 2005 — start reading, target finishing by end of week 3.

**Fluency**
- librosa: load audio, compute STFT, plot spectrogram, RMS, spectral centroid. No notes app — do it in a Jupyter notebook and check the plots match intuition.
- Unreal: complete one tutorial that gets you comfortable with the viewport, the level editor, and a basic post-process volume. William Faucher's intro lighting video is a strong candidate.

**Aesthetic study**
- Add 3 reference stills to `docs/aesthetic/`. Each with a teardown note (lens character, lighting setup, color grade, post-processing). Batman 2022 and Kissland-era Weeknd are the priority sources.

**Roadmap position:** Stage 1 shipped. Stage 2 started.

---

## Week 3 — Event-level features

**Reading**
- Bello et al. 2005 — finish. Write the synthesis note in `docs/research/bello-2005-onset-tutorial.md` *before* committing onset-detection code.
- Dixon 2006 *Onset Detection Revisited* — short, do it after Bello.
- Böck/Krebs/Widmer 2016 *Joint Beat and Downbeat Tracking with RNNs* — read once, note the architecture and the dataset, then move on. The point is to understand what madmom does, not to reimplement it.

**Fluency**
- Onset detection in a notebook using two methods (spectral flux from scratch, complex domain from librosa or your own). Plotted, eyeballed against waveform, sanity-checked.
- Downbeat tracker candidate selected and running against the target track. Compare it to the `librosa` beat baseline and note where it succeeds and where it fails.
- Unreal: comfortable creating a new level, placing a camera, adjusting the post-process volume settings.

**Aesthetic study**
- Watch The Batman (2022) opening sequence (the first ~10 min) with the sound off. Note the visual pacing — when does the camera move, when does it hold, when does the color shift. This is the "structural pacing" your visuals need.

**Roadmap position:** Stage 2 in progress. Possibly shipping by end of week.

---

## Week 4 — Structural segmentation begins

**Reading**
- Foote 2000 *Automatic Audio Segmentation* — the seminal paper. Short. You will implement this from scratch, so read it like you're implementing it.
- Müller FMP **Chapter 4** (structure analysis). The notebooks for this chapter are excellent — run them on a track of your choice.

**Fluency**
- Compute a chroma-based self-similarity matrix for your target track in a notebook. Plot it as an image. Visually identify where the section boundaries are by eye on the SSM alone.
- Unreal: confident with the post-process volume settings — bloom, chromatic aberration, film grain, lens distortion. Tuned to taste, not just default.

**Aesthetic study**
- Add the *first stage of `docs/aesthetic/teardowns/`* — pick the strongest reference still and write a 300-word teardown. Lens, lighting setup (including practicals), color grade in three-point form (shadows / midtones / highlights), grain/texture, implied movement, post-processing chain.

**Roadmap position:** Stage 2 shipped. Stage 3 started.

---

## Week 5 — From-scratch novelty implementation

**Reading**
- Foote & Cooper 2003 — the SSM-decomposition follow-up. Skim, mainly for the "segment-level SSM" idea which feeds your multi-timescale schema.
- Re-read Müller FMP **Section 4.4** (novelty-based segmentation) — this is the section the from-scratch implementation maps to.

**Fluency**
- Implement the Foote checkerboard-kernel novelty curve from scratch. From your own SSM. From your own chroma. Don't use MSAF yet.
- The novelty curve plotted against the audio. The peaks should align with section boundaries you can hear.

**Aesthetic study**
- Watch the *Kiss Land* short film (or the Trilogy-era music videos if you can't find Kiss Land). Note specifically the *transitions* — how scenes change, what visual rhythm sits underneath the music's rhythm.

**Roadmap position:** Stage 3 in progress. From-scratch Foote PR opened.

---

## Week 6 — Structure comparison

**Reading**
- Nieto & Bello 2016 *Systematic Exploration of Computational Music Structure Research*. Now you have your own implementation to compare against, the paper's value goes up.
- McFee & Ellis 2014 *Spectral Clustering* — useful context for structure segmentation, even if the original MSAF implementation is not in the base environment.

**Fluency**
- Structure-comparison baseline selected and running. Prefer `librosa.segment` primitives unless a maintained package earns its place. Compare boundaries to your from-scratch implementation. Document the differences in `docs/decisions.md`.
- Unreal: comfortable with Niagara basics — a particle system you've built yourself, with a couple of parameters exposed.

**Aesthetic study**
- Second teardown in `docs/aesthetic/teardowns/`. This time pick a *moving* reference — a 5-second clip from a music video or film. Annotate frame-by-frame.

**Roadmap position:** Stage 3 shipping.

---

## Week 7 — The data contract

**Reading**
- Lerdahl & Krumhansl 2007 *Modeling Tonal Tension* — skim. The conceptual frame matters more than the tonal-theory details. Note that the *temporal aspect* is the part that maps to your project.
- pydantic docs on model versioning (not a paper — actually useful for schema design).

**Fluency**
- Schema design in `src/bridge/schema.py`. Pydantic models for the multi-timescale structure. Test the schema by exporting and re-importing a timeline.
- Unreal: have imported a CSV into Sequencer at least once via a tutorial, even if the data is dummy. The mechanical knowledge of "how does Sequencer eat data" is the unblocker.

**Aesthetic study**
- Begin the William Faucher cinematic-lighting series in earnest. Goal: ability to set up a single-light, single-subject Unreal scene that has *character* — not the default "everything is grey" look.

**Roadmap position:** Stage 4 in progress. Schema PR opened.

---

## Week 8 — Schema locked, taste calibration starts

**Reading**
- Farbood 2012 *A Parametric, Temporal Model of Musical Tension*. This is the central paper for the project's emotional-contour thesis. Read it slowly. Synthesize notes.
- Re-read your own `docs/CONTEXT.md` and `docs/aesthetic/` notes. Are they still right? If not, update them.

**Fluency**
- `TimelineV1` schema locked. Validated export for the target track running cleanly. The JSON is readable enough to spot-check by eye.
- Unreal: can build a scene with one camera, one moving light, particles, and post-processing. The scene doesn't have to be "good" yet — it has to be *yours*, built without a tutorial.

**Aesthetic study**
- Five reference stills now in `docs/aesthetic/`, three with full teardowns. The reference library is starting to be useful as a working tool, not just a moodboard.

**Roadmap position:** Stage 4 shipped. Stage 5 started.

---

## Week 9 — The still that hits

**Reading**
- Greig Fraser interviews on The Batman cinematography. Search the *American Cinematographer* April 2022 issue. Read at least two interviews — print or web.
- One William Faucher YouTube tutorial specifically on color grading in Unreal.

**Fluency**
- Unreal: building toward the first still. The post-process volume is tuned. The lighting setup has practical-light character. You've rendered at least 10 still iterations and discarded 8 of them.

**Aesthetic study**
- The active practice: at the end of each work session, open the current Unreal render next to the chosen reference still and ask "what's the biggest gap." Fix that, render again, repeat.

**Roadmap position:** Stage 5 in progress. First still being iterated.

---

## Week 10 — Still shipped, connection begins

**Reading**
- Farbood & Upham 2013 *Interpreting expressive performance through listener judgments of musical tension*. This is the multi-timescale paper that anchors Stage 7. Read it with Stage 7 in mind.
- Skim one GDC Vault talk on procedural cinematic camera in real-time (Naughty Dog or Santa Monica Studio).

**Fluency**
- The Stage 5 still is committed to `docs/aesthetic/teardowns/`. Side-by-side with reference. Honest assessment: tier-matched, or still a tier off?
- Unreal: Sequencer comfortable. CSV import working with dummy data, ready for real timeline data.

**Aesthetic study**
- This week, stop adding to the reference library. The bottleneck is now *applying* the references in Unreal, not collecting more. Apply the existing library more carefully.

**Roadmap position:** Stage 5 shipped. Stage 6 started.

---

## Week 11 — First connection

**Reading**
- Light week on reading. The work this week is integration, and that needs head-space. Re-read your own `docs/research/` notes for any paper you'll touch this week.
- TenseMusic paper (PLOS One 2024) — skim, identify whether running their code on your track gives you a useful tension curve to compare against your own work later.

**Fluency**
- 15–30 second clip rendered with one parameter driven by one feature. Subtle is fine. The proof point is *the loop closes*.
- Unreal: comfortable with Movie Render Queue settings — codecs, color space, frame range, anti-aliasing.

**Aesthetic study**
- Watch your own clip 5 times. Then watch the target reference clip 5 times. Write a 1-paragraph honest comparison.

**Roadmap position:** Stage 6 shipping.

---

## Week 12 — Multi-timescale begins

**Reading**
- Re-read Farbood & Upham 2013 with the multi-timescale schema in front of you. The connection between paper and schema should now click. If it doesn't, you've found a gap — log it.
- One paper from `docs/reading-list.md` section 5 (cinematography research). This is the week you start treating visual craft as a research surface, not just taste.

**Fluency**
- Three different feature-to-parameter bindings in Unreal, each at a different timescale. The work this week is iteration speed — how fast can you change a binding, render, and look.

**Aesthetic study**
- Schedule a watch session: one full pass of *Kiss Land* film visuals + one full pass of The Batman opening + one full pass of a Blade Runner 2049 sequence. Take notes on pacing specifically. Stage 7 is pacing.

**Roadmap position:** Stage 7 in progress.

---

## Weeks 13–14 — Multi-timescale completes

**Reading**
- Catch-up week. Any reading-list entries you've skipped and now wish you hadn't. Don't add new papers — close gaps.
- Light skim of MM-Diffusion or VeM (reading list section 4). Park-it pass. You're not implementing them — you're orienting.

**Fluency**
- Stage 7 deliverable: a friend who hasn't heard the track can identify section changes from the visuals alone. Test this with an actual person.
- Unreal: Niagara fluency is now real. Camera work is now real. Post-processing is now real. The Unreal side has caught up to the Python side.

**Aesthetic study**
- Postmortem on what the existing aesthetic library got right and wrong. Update `docs/aesthetic/` accordingly.

**Roadmap position:** Stage 7 shipping. Stage 8 started.

---

## Weeks 15–17 — The full piece

**Reading**
- Very light. You're in production, not research. Read for inspiration not for unblocking.
- Re-read your own postmortems from Stages 3 and 7. Apply lessons.

**Fluency**
- Stage 8 deliverable: the full track, fully composed visuals, rendered to MP4. Shareable.
- Unreal: render times, MRQ settings, frame budgeting — these are the bottlenecks now, not creative ones.

**Aesthetic study**
- Final teardown: your own video, treated as you'd treat a reference still. Lens, lighting, color, pacing, post — what worked, what didn't. This is the entry-point document for whatever Stage 9 becomes.

**Roadmap position:** Stage 8 shipping by end of week 17.

---

## Week 18 onwards — Direction decision

The roadmap deliberately ends here. Stage 9+ in `ROADMAP.md` lists possible directions but doesn't commit. The point of this 18-week arc is to *get to the position where direction can be chosen from depth, not from idea-shopping*.

When Stage 8 ships, write a `docs/postmortem-stage-8.md` that's the basis for picking what Stage 9 is. Re-read `Current update how I feel` and `Projects` from the broader project context — what was true when you started should be updated.

Don't rush this decision. The work is the depth, not the next stage.

---

## How to use this file

- **Open it Monday morning.** Read the current week's section. That's the work for the week.
- **Update it Friday evening.** What slipped, what moved forward, what was easier or harder than expected. Brief.
- **Don't mark things complete with checkboxes.** This isn't a todo list. The signal is whether the *roadmap position* at the end of the week matches reality. If it doesn't, the next week's plan changes.
- **Flag drift early.** If by week 5 you're still on Stage 2, the whole timeline shifts — but it doesn't break. Just reset the week-numbering, don't try to compress.
- **The reading is not optional.** The project's thesis is depth, not vibe-coding. Skipping the reading is skipping the project.
