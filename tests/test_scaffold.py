from audio.config import DEFAULT_AUDIO_CONFIG
from bridge.schema import SCHEMA_VERSION


def test_scaffold_imports() -> None:
    """Stage 0 smoke test for editable installs."""
    assert DEFAULT_AUDIO_CONFIG.sample_rate == 44_100
    assert SCHEMA_VERSION == "timeline.v1"
