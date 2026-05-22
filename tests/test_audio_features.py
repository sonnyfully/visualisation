import numpy as np

from audio.config import DEFAULT_AUDIO_CONFIG
from audio.features import (
    basic_feature_frame,
    rms_envelope,
    spectral_centroid,
    spectral_flux,
    spectral_rolloff,
)


def _sine_wave(frequency: float, duration_seconds: float = 1.0) -> np.ndarray:
    sample_rate = DEFAULT_AUDIO_CONFIG.sample_rate
    times = np.arange(int(sample_rate * duration_seconds)) / sample_rate
    return (0.5 * np.sin(2 * np.pi * frequency * times)).astype(np.float32)


def test_basic_feature_frame_is_finite_and_timestamped() -> None:
    samples = _sine_wave(440.0)
    frame = basic_feature_frame(samples, DEFAULT_AUDIO_CONFIG.sample_rate)

    assert list(frame.columns) == [
        "time_seconds",
        "rms",
        "spectral_centroid_hz",
        "spectral_flux",
        "spectral_rolloff_hz",
    ]
    assert not frame.empty
    assert frame["time_seconds"].is_monotonic_increasing
    assert np.all(np.isfinite(frame.to_numpy()))


def test_sine_wave_centroid_tracks_tone_frequency() -> None:
    samples = _sine_wave(440.0)
    centroid = spectral_centroid(samples, DEFAULT_AUDIO_CONFIG.sample_rate)
    middle = centroid[len(centroid) // 4 : -len(centroid) // 4]

    assert 400.0 < float(np.median(middle)) < 480.0


def test_feature_extractors_share_frame_count() -> None:
    samples = _sine_wave(110.0, duration_seconds=0.5)

    rms = rms_envelope(samples)
    centroid = spectral_centroid(samples, DEFAULT_AUDIO_CONFIG.sample_rate)
    flux = spectral_flux(samples)
    rolloff = spectral_rolloff(samples, DEFAULT_AUDIO_CONFIG.sample_rate)

    assert len({len(rms), len(centroid), len(flux), len(rolloff)}) == 1
    assert float(np.max(flux)) <= 1.0
    assert float(np.median(rolloff)) > float(np.median(centroid))
