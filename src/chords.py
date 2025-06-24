from custom_types import IntervalStructure
from enums import Degree

CHORD_DEGREE_MAP: IntervalStructure = {
    # Triadi
    "maj [triad]": [Degree.R, Degree.M3, Degree.P5],
    "min [triad]": [Degree.R, Degree.m3, Degree.P5],
    "dim [triad]": [Degree.R, Degree.m3, Degree.A4],
    "aug [triad]": [Degree.R, Degree.M3, Degree.m6],
    "sus2 [triad]": [Degree.R, Degree.M9, Degree.P5],
    "sus4 [triad]": [Degree.R, Degree.P4, Degree.P5],
    # Triadi add
    "add9 [triad]": [Degree.R, Degree.M3, Degree.P5, Degree.M9],
    "add11 [triad]": [Degree.R, Degree.M3, Degree.P5, Degree.P4],
    "min(add9) [triad]": [Degree.R, Degree.m3, Degree.P5, Degree.M9],
    "min(add11) [triad]": [Degree.R, Degree.m3, Degree.P5, Degree.P4],
    "min(add13) [triad]": [Degree.R, Degree.m3, Degree.P5, Degree.M6],
    "dim(add9) [triad]": [Degree.R, Degree.m3, Degree.A4, Degree.M9],
    "dim(add11) [triad]": [Degree.R, Degree.m3, Degree.A4, Degree.P4],
    "dim(add13) [triad]": [Degree.R, Degree.m3, Degree.A4, Degree.M6],
    "aug(add9) [triad]": [Degree.R, Degree.M3, Degree.m6, Degree.M9],
    "aug(add11) [triad]": [Degree.R, Degree.M3, Degree.m6, Degree.P4],
    "aug(add13) [triad]": [Degree.R, Degree.M3, Degree.m6, Degree.M6],
    # Settima
    "7": [Degree.R, Degree.M3, Degree.P5, Degree.m7],
    "min7": [Degree.R, Degree.m3, Degree.P5, Degree.m7],
    "min7b5": [Degree.R, Degree.m3, Degree.A4, Degree.m7],
    "maj7": [Degree.R, Degree.M3, Degree.P5, Degree.M7],
    "dim7": [Degree.R, Degree.m3, Degree.A4, Degree.M6],  # M6 = dim7 enharmonic
    "minMaj7": [Degree.R, Degree.m3, Degree.P5, Degree.M7],
    "maj7#5": [Degree.R, Degree.M3, Degree.m6, Degree.M7],
    "maj7b5": [Degree.R, Degree.M3, Degree.A4, Degree.M7],
    "maj7sus2": [Degree.R, Degree.M9, Degree.P5, Degree.M7],
    "maj7sus4": [Degree.R, Degree.P4, Degree.P5, Degree.M7],
    # Estensioni
    "maj9": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.M9],
    "9": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.M9],
    "min9": [Degree.R, Degree.m3, Degree.P5, Degree.m7, Degree.M9],
    "11": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.M9, Degree.P4],
    "13": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.M9, Degree.P4, Degree.M6],
    "maj13": [
        Degree.R,
        Degree.M3,
        Degree.P5,
        Degree.M7,
        Degree.M9,
        Degree.P4,
        Degree.M6,
    ],
    "6": [Degree.R, Degree.M3, Degree.P5, Degree.M6],
    "min6": [Degree.R, Degree.m3, Degree.P5, Degree.M6],
    "6/9": [Degree.R, Degree.M3, Degree.P5, Degree.M6, Degree.M9],
    # Accordi alterati
    "7(b9)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m9],
    "7(#9)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m3],
    "7(b5)": [Degree.R, Degree.M3, Degree.A4, Degree.m7],
    "7(#5)": [Degree.R, Degree.M3, Degree.m6, Degree.m7],
    "7(b9, b5)": [Degree.R, Degree.M3, Degree.A4, Degree.m7, Degree.m9],
    "7(b9, #5)": [Degree.R, Degree.M3, Degree.m6, Degree.m7, Degree.m9],
    "7(#9, b5)": [Degree.R, Degree.M3, Degree.A4, Degree.m7, Degree.m3],
    "7(#9, #5)": [Degree.R, Degree.M3, Degree.m6, Degree.m7, Degree.m3],
    "13(b9)": [
        Degree.R,
        Degree.M3,
        Degree.P5,
        Degree.m7,
        Degree.m9,
        Degree.P4,
        Degree.M6,
    ],
    "13(#9)": [
        Degree.R,
        Degree.M3,
        Degree.P5,
        Degree.m7,
        Degree.m3,
        Degree.P4,
        Degree.M6,
    ],
    "7(#11)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.A4],
    "7(b13)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m6],
    # Accordi di settima ed estensioni variate
    "maj7(#11)": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.A4],
    "maj7add13": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.M6],
    "minMaj9": [Degree.R, Degree.m3, Degree.P5, Degree.M7, Degree.M9],
    "minMaj7add11": [Degree.R, Degree.m3, Degree.P5, Degree.M7, Degree.P4],
    # Accordi di nona alterata
    "7(b9, #11)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m9, Degree.A4],
    "7(#9, #11)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m3, Degree.A4],
    "7(b9, b13)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m9, Degree.m6],
    "7(#9, b13)": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.m3, Degree.m6],
    "7(b9, #5, #11)": [
        Degree.R,
        Degree.M3,
        Degree.m6,
        Degree.m7,
        Degree.m9,
        Degree.A4,
    ],
    # Accordi alterati
    "13(#11)": [
        Degree.R,
        Degree.M3,
        Degree.P5,
        Degree.m7,
        Degree.M9,
        Degree.A4,
        Degree.M6,
    ],
    "min6(b9)": [Degree.R, Degree.m3, Degree.P5, Degree.M6, Degree.m9],
    "min11": [Degree.R, Degree.m3, Degree.P5, Degree.m7, Degree.M9, Degree.P4],
    "min11(b5)": [Degree.R, Degree.m3, Degree.A4, Degree.m7, Degree.M9, Degree.P4],
    # Add accordi con settima
    "7add13": [Degree.R, Degree.M3, Degree.P5, Degree.m7, Degree.M6],
    "min7add11": [Degree.R, Degree.m3, Degree.P5, Degree.m7, Degree.P4],
    "min7add13": [Degree.R, Degree.m3, Degree.P5, Degree.m7, Degree.M6],
    "maj7add9": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.M9],
    # Accordi sus estesi
    "7sus2": [Degree.R, Degree.M9, Degree.P5, Degree.m7],
    "7sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7],
    "9sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7, Degree.M9],
    "13sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7, Degree.M9, Degree.M6],
    # Accordi 6 e varianti
    "min6add9": [Degree.R, Degree.m3, Degree.P5, Degree.M6, Degree.M9],
}


def main() -> None:
    longest_chord_name = max(len(name) for name in CHORD_DEGREE_MAP)
    for chord, degrees in CHORD_DEGREE_MAP.items():
        print(
            f"{chord:{longest_chord_name}} "
            f"{', '.join([degree.name for degree in degrees])}",
        )


if __name__ == "__main__":
    main()
