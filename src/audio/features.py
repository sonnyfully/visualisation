"""Frame-level spectral feature extraction."""

import librosa
import numpy as np
import pandas as pd
from numpy.typing import NDArray

from audio.config import DEFAULT_AUDIO_CONFIG, AudioConfig

FloatArray = NDArray[np.float32 | np.float64]


def frame_times(
    frame_count: int,
    sample_rate: int,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> NDArray[np.float64]:
    """Return frame-center timestamps for hop-aligned feature arrays."""

    frames = np.arange(frame_count)
    return librosa.frames_to_time(frames, sr=sample_rate, hop_length=config.hop_size)


def rms_envelope(
    samples: FloatArray,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> NDArray[np.float32]:
    """Compute frame-level root mean square energy."""

    rms = librosa.feature.rms(
        y=np.asarray(samples),
        frame_length=config.frame_size,
        hop_length=config.hop_size,
        center=True,
    )[0]
    return rms.astype(np.float32)


def spectral_centroid(
    samples: FloatArray,
    sample_rate: int,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> NDArray[np.float32]:
    """Compute the brightness center of mass for each analysis frame."""

    centroid = librosa.feature.spectral_centroid(
        y=np.asarray(samples),
        sr=sample_rate,
        n_fft=config.frame_size,
        hop_length=config.hop_size,
        center=True,
    )[0]
    return centroid.astype(np.float32)


def spectral_rolloff(
    samples: FloatArray,
    sample_rate: int,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> NDArray[np.float32]:
    """Compute the frequency below which most frame energy is concentrated."""

    rolloff = librosa.feature.spectral_rolloff(
        y=np.asarray(samples),
        sr=sample_rate,
        n_fft=config.frame_size,
        hop_length=config.hop_size,
        roll_percent=config.rolloff_percent,
        center=True,
    )[0]
    return rolloff.astype(np.float32)


def spectral_flux(
    samples: FloatArray,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> NDArray[np.float32]:
    """Compute half-wave rectified frame-to-frame spectral magnitude change."""

    stft = librosa.stft(
        y=np.asarray(samples),
        n_fft=config.frame_size,
        hop_length=config.hop_size,
        center=True,
    )
    magnitude = np.abs(stft)
    diff = np.diff(magnitude, axis=1, prepend=magnitude[:, :1])
    flux = np.maximum(diff, 0.0).sum(axis=0)

    max_value = float(np.max(flux))
    if max_value > 0:
        flux = flux / max_value

    return flux.astype(np.float32)


def basic_feature_frame(
    samples: FloatArray,
    sample_rate: int,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
) -> pd.DataFrame:
    """Compute Stage 1 frame-level features as a timestamped table."""

    rms = rms_envelope(samples, config)
    centroid = spectral_centroid(samples, sample_rate, config)
    flux = spectral_flux(samples, config)
    rolloff = spectral_rolloff(samples, sample_rate, config)
    frame_count = min(len(rms), len(centroid), len(flux), len(rolloff))

    return pd.DataFrame(
        {
            "time_seconds": frame_times(frame_count, sample_rate, config),
            "rms": rms[:frame_count],
            "spectral_centroid_hz": centroid[:frame_count],
            "spectral_flux": flux[:frame_count],
            "spectral_rolloff_hz": rolloff[:frame_count],
        }
    )
