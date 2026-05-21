"""Shared audio-analysis configuration.

These are initial project defaults, not evidence that a detector works well.
Each DSP PR should validate its own assumptions visually in notebooks.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AudioConfig:
    """Project-wide audio analysis settings."""

    # 44.1 kHz preserves standard music-release resolution for offline analysis.
    sample_rate: int = 44_100
    # 2048/512 is a common MIR starting point for spectral features in librosa.
    frame_size: int = 2_048
    hop_size: int = 512
    mono: bool = True


DEFAULT_AUDIO_CONFIG = AudioConfig()

