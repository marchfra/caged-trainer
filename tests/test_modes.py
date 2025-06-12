from src.enums import Degree
from src.modes import SCALES, find_compatible_scale


def test_find_compatible_scale_major_triad() -> None:
    result = find_compatible_scale([Degree.R, Degree.M3, Degree.P5])
    assert "Ionian" in result
    assert "Lydian" in result
    assert "Mixolydian" in result
    assert "Lydian #9" in result
    assert "Lydian Dominant" in result
    assert "Dorian" not in result
    assert "Phrygian" not in result
    assert "Dorian #11" not in result
    assert "Lydian Augmented" not in result


def test_find_compatible_scale_minor_triad() -> None:
    result = find_compatible_scale([Degree.R, Degree.m3, Degree.P5])
    assert "Dorian" in result
    assert "Phrygian" in result
    assert "Aeolian" in result
    assert "Locrian" not in result
    assert "Ionian" not in result


def test_find_compatible_scale_no_match() -> None:
    class FakeDegree:
        name = "X"

    result = find_compatible_scale([FakeDegree()])
    assert result == set()


def test_modes_unique_names() -> None:
    mode_names = [mode for scale in SCALES for mode in scale]
    assert len(mode_names) == len(set(mode_names))
