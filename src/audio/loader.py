"""Audio file loading and resampling boundary."""

from pathlib import Path

import librosa
import numpy as np
from numpy.typing import NDArray

from audio.config import DEFAULT_AUDIO_CONFIG, AudioConfig

FloatArray = NDArray[np.float32]


def load_audio(
    path: str | Path,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> tuple[FloatArray, int]:
    """Load an audio file using the project's canonical analysis settings.

    The loader is the single boundary where source files become normalized DSP
    arrays. Everything downstream should use the returned sample rate instead
    of reaching back into file metadata.
    """

    audio_path = Path(path).expanduser()
    if not audio_path.exists():
        msg = f"Audio file not found: {audio_path}"
        raise FileNotFoundError(msg)

    samples, sample_rate = librosa.load(
        audio_path,
        sr=config.sample_rate,
        mono=config.mono,
        dtype=np.float32,
    )

    if samples.size == 0:
        msg = f"Audio file contains no samples: {audio_path}"
        raise ValueError(msg)
    if not np.all(np.isfinite(samples)):
        msg = f"Audio file contains non-finite samples: {audio_path}"
        raise ValueError(msg)

    return np.asarray(samples, dtype=np.float32), int(sample_rate)
