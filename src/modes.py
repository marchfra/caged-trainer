from custom_types import IntervalStructure
from enums import Degree

MAJOR: IntervalStructure = {
    "Ionian": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.P4,
        Degree.P5,
        Degree.M6,
        Degree.M7,
    ],
    "Dorian": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Phrygian": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.m6,
        Degree.m7,
    ],
    "Lydian": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.A4,
        Degree.P5,
        Degree.M6,
        Degree.M7,
    ],
    "Mixolydian": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.P4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Aeolian": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.m6,
        Degree.m7,
    ],
    "Locrian": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.P4,
        Degree.A4,
        Degree.m6,
        Degree.m7,
    ],
}

HARMONIC_MINOR: IntervalStructure = {
    "Harmonic Minor": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.m6,
        Degree.M7,
    ],
    "Locrian maj6": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.P4,
        Degree.A4,
        Degree.M6,
        Degree.m7,
    ],
    "Ionian #5": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.P4,
        Degree.m6,
        Degree.M6,
        Degree.M7,
    ],
    "Dorian #11": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.A4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Phrygian Dominant": [
        Degree.R,
        Degree.m9,
        Degree.M3,
        Degree.P4,
        Degree.P5,
        Degree.m6,
        Degree.m7,
    ],
    "Lydian #9": [
        Degree.R,
        Degree.m3,
        Degree.M3,
        Degree.A4,
        Degree.P5,
        Degree.M6,
        Degree.M7,
    ],
    "Superlocrian diminished": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.M3,
        Degree.A4,
        Degree.m6,
        Degree.M6,
    ],
}

MELODIC_MINOR: IntervalStructure = {
    "Melodic Minor": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.M6,
        Degree.M7,
    ],
    "Dorian b9": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.P4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Lydian Augmented": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.A4,
        Degree.m6,
        Degree.M6,
        Degree.M7,
    ],
    "Lydian Dominant": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.A4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Mixolydian b6": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.P4,
        Degree.P5,
        Degree.m6,
        Degree.m7,
    ],
    "Locrian maj9": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.A4,
        Degree.m6,
        Degree.m7,
    ],
    "Superlocrian": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.M3,
        Degree.A4,
        Degree.m6,
        Degree.m7,
    ],
}

SYMMETRIC_SCALES: IntervalStructure = {
    "Diminished (Half-Whole)": [
        Degree.R,
        Degree.m9,
        Degree.m3,
        Degree.M3,
        Degree.A4,
        Degree.P5,
        Degree.M6,
        Degree.m7,
    ],
    "Diminished (Whole-Half)": [
        Degree.R,
        Degree.M9,
        Degree.m3,
        Degree.P4,
        Degree.A4,
        Degree.m6,
        Degree.M6,
        Degree.M7,
    ],
    "Whole Tone": [
        Degree.R,
        Degree.M9,
        Degree.M3,
        Degree.A4,
        Degree.m6,
        Degree.m7,
    ],
}

SCALES: dict[str, IntervalStructure] = {
    "Major scale": MAJOR,
    "Harmonic minor scale": HARMONIC_MINOR,
    "Melodic minor scale": MELODIC_MINOR,
    "Symmetric scales": SYMMETRIC_SCALES,
}


def find_compatible_scale(chord_degrees: list[Degree]) -> set[str]:
    """Find a compatible scale for the given chord degrees."""
    compatible_scales: IntervalStructure = {}
    for scale in SCALES.values():
        for mode, degrees in scale.items():
            if all(degree in degrees for degree in chord_degrees):
                compatible_scales[mode] = degrees
    return set(compatible_scales.keys())


def main() -> None:
    for scale in SCALES.values():
        longest_mode_name = max(scale.keys(), key=len)
        for mode, degrees in scale.items():
            print(
                f"{mode:{len(longest_mode_name)}} "
                f"{', '.join([degree.name for degree in degrees])}",
            )
        print()


if __name__ == "__main__":
    main()
