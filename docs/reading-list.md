# Reading List

Working reading list for the music-driven visual system. Add synthesized notes in `docs/research/` for papers that directly inform implementation.

## Music Information Retrieval

- Meinard Muller, *Fundamentals of Music Processing* — especially chapters on Fourier analysis, onset detection, synchronization, and structure analysis.
- Brian McFee et al., 2015, "librosa: Audio and Music Signal Analysis in Python" — grounding for the Python MIR stack.
- Juan Pablo Bello et al., 2005, "A Tutorial on Onset Detection in Music Signals" — required before onset detector implementation.
- Simon Dixon, 2006, "Onset Detection Revisited" — useful comparison point after Bello.
- Sebastian Bock, Florian Krebs, and Gerhard Widmer, 2016, "Joint Beat and Downbeat Tracking with Recurrent Neural Networks" — context for modern beat/downbeat tracking models and historical comparison to `madmom`.
- CPJKU Beat This documentation and paper — candidate modern beat/downbeat tracker for Stage 2 evaluation.
- Essentia documentation — candidate MIR library if the project needs broader audio analysis beyond `librosa`.
- `librosa.segment` documentation — modern baseline primitives for recurrence matrices, time-lag representations, and agglomerative segmentation.
- Jonathan Foote, 2000, "Automatic Audio Segmentation Using a Measure of Audio Novelty" — required before the from-scratch structural segmentation pass.
- Oriol Nieto and Juan Pablo Bello, 2016, "Systematic Exploration of Computational Music Structure Research" — structure-analysis context and evaluation framing.

## Musical Tension And Structure

- Fred Lerdahl and Carol Krumhansl, 2007, "Modeling Tonal Tension" — conceptual basis for tension/release mapping.
- Morwaread M. Farbood, 2012, "A Parametric, Temporal Model of Musical Tension" — central long-horizon reference for emotional contour.
- Morwaread M. Farbood and Finn Upham, 2013, "Interpreting Expressive Performance Through Listener Judgments of Musical Tension" — useful for multi-timescale mappings.

## Cinematic Real-Time Visuals

- Greig Fraser interviews on *The Batman* cinematography — lensing, exposure, practical-light language.
- William Faucher Unreal lighting and post-process tutorials — practical Unreal fluency for cinematic scenes.
- GDC talks on procedural cinematic camera systems from studios such as Naughty Dog or Santa Monica Studio — camera language for real-time systems.

## Later, Parked

- Audio-conditioned diffusion / neural rendering papers — relevant after the offline Unreal pipeline has shipped a coherent full-track piece.
