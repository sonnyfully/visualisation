"""Plotting helpers for validating audio features against waveforms."""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from numpy.typing import NDArray

from audio.config import DEFAULT_AUDIO_CONFIG, AudioConfig


def plot_waveform(
    samples: NDArray[np.float32 | np.float64],
    sample_rate: int,
    ax: Axes | None = None,
) -> Axes:
    """Plot a waveform against seconds."""

    if ax is None:
        _, ax = plt.subplots(figsize=(12, 3))

    librosa.display.waveshow(samples, sr=sample_rate, ax=ax, color="#b8c1ff")
    ax.set(title="Waveform", xlabel="Time (s)", ylabel="Amplitude")
    return ax


def plot_spectrogram(
    samples: NDArray[np.float32 | np.float64],
    sample_rate: int,
    config: AudioConfig = DEFAULT_AUDIO_CONFIG,
    ax: Axes | None = None,
) -> Axes:
    """Plot a decibel-scaled short-time Fourier transform spectrogram."""

    if ax is None:
        _, ax = plt.subplots(figsize=(12, 4))

    stft = librosa.stft(
        y=np.asarray(samples),
        n_fft=config.frame_size,
        hop_length=config.hop_size,
        center=True,
    )
    db = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    image = librosa.display.specshow(
        db,
        sr=sample_rate,
        hop_length=config.hop_size,
        x_axis="time",
        y_axis="hz",
        ax=ax,
        cmap="magma",
    )
    ax.figure.colorbar(image, ax=ax, format="%+2.0f dB")
    ax.set(title="Spectrogram")
    return ax


def plot_feature_against_waveform(
    samples: NDArray[np.float32 | np.float64],
    sample_rate: int,
    features: pd.DataFrame,
    feature_name: str,
    ax: Axes | None = None,
) -> Axes:
    """Overlay a normalized feature curve on the waveform."""

    if ax is None:
        _, ax = plt.subplots(figsize=(12, 3))

    times = np.arange(len(samples)) / sample_rate
    waveform = np.asarray(samples, dtype=float)
    peak = float(np.max(np.abs(waveform)))
    if peak > 0:
        waveform = waveform / peak

    feature = features[feature_name].to_numpy(dtype=float)
    feature_peak = float(np.nanmax(np.abs(feature)))
    if feature_peak > 0:
        feature = feature / feature_peak

    ax.plot(times, waveform, color="#2b335f", linewidth=0.6, alpha=0.7)
    ax.plot(
        features["time_seconds"],
        feature,
        color="#ff4f87",
        linewidth=1.5,
        label=feature_name,
    )
    ax.set(
        title=f"{feature_name} against waveform",
        xlabel="Time (s)",
        ylabel="Normalized value",
    )
    ax.legend(loc="upper right")
    return ax
