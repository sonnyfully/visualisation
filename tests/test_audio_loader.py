import wave
from pathlib import Path

import numpy as np

from audio.config import DEFAULT_AUDIO_CONFIG
from audio.loader import load_audio


def _write_pcm16_wav(path: Path, samples: np.ndarray, sample_rate: int) -> None:
    pcm = np.clip(samples, -1.0, 1.0)
    pcm = (pcm * np.iinfo(np.int16).max).astype(np.int16)

    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(pcm.tobytes())


def test_load_audio_resamples_to_project_sample_rate(tmp_path: Path) -> None:
    source_sample_rate = 22_050
    duration_seconds = 0.25
    times = np.arange(int(source_sample_rate * duration_seconds)) / source_sample_rate
    sine = 0.25 * np.sin(2 * np.pi * 440.0 * times)
    audio_path = tmp_path / "sine.wav"
    _write_pcm16_wav(audio_path, sine, source_sample_rate)

    samples, sample_rate = load_audio(audio_path)

    expected_length = int(DEFAULT_AUDIO_CONFIG.sample_rate * duration_seconds)
    assert sample_rate == DEFAULT_AUDIO_CONFIG.sample_rate
    assert samples.dtype == np.float32
    assert abs(len(samples) - expected_length) <= 2
    assert np.all(np.isfinite(samples))


def test_load_audio_rejects_missing_file(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.wav"

    try:
        load_audio(missing_path)
    except FileNotFoundError as error:
        assert str(missing_path) in str(error)
    else:
        raise AssertionError("load_audio should reject missing files")
