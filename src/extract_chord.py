from random import choice

from src.enums import Degree

CHORD_DEGREE_MAP: dict[str, list[Degree]] = {
    # Triadi
    "maj": [Degree.R, Degree.M3, Degree.P5],
    "min": [Degree.R, Degree.m3, Degree.P5],
    "dim": [Degree.R, Degree.m3, Degree.A4],
    "aug": [Degree.R, Degree.M3, Degree.m6],
    "sus2": [Degree.R, Degree.M9, Degree.P5],
    "sus4": [Degree.R, Degree.P4, Degree.P5],
    # Triadi add
    "add9": [Degree.R, Degree.M3, Degree.P5, Degree.M9],
    "add11": [Degree.R, Degree.M3, Degree.P5, Degree.P4],
    "add13": [Degree.R, Degree.M3, Degree.P5, Degree.M6],
    "min(add9)": [Degree.R, Degree.m3, Degree.P5, Degree.M9],
    "min(add11)": [Degree.R, Degree.m3, Degree.P5, Degree.P4],
    "min(add13)": [Degree.R, Degree.m3, Degree.P5, Degree.M6],
    "dim(add9)": [Degree.R, Degree.m3, Degree.A4, Degree.M9],
    "dim(add11)": [Degree.R, Degree.m3, Degree.A4, Degree.P4],
    "dim(add13)": [Degree.R, Degree.m3, Degree.A4, Degree.M6],
    "aug(add9)": [Degree.R, Degree.M3, Degree.m6, Degree.M9],
    "aug(add11)": [Degree.R, Degree.M3, Degree.m6, Degree.P4],
    "aug(add13)": [Degree.R, Degree.M3, Degree.m6, Degree.M6],
    # Settima
    "7": [Degree.R, Degree.M3, Degree.P5, Degree.m7],
    "min7": [Degree.R, Degree.m3, Degree.P5, Degree.m7],
    "min7b5": [Degree.R, Degree.m3, Degree.A4, Degree.m7],
    "maj7": [Degree.R, Degree.M3, Degree.P5, Degree.M7],
    "dim7": [Degree.R, Degree.m3, Degree.A4, Degree.M6],  # M6 = dim7 enharmonic
    "minMaj7": [Degree.R, Degree.m3, Degree.P5, Degree.M7],
    "maj7#5": [Degree.R, Degree.M3, Degree.m6, Degree.M7],
    "maj7b5": [Degree.R, Degree.M3, Degree.A4, Degree.M7],
    "7sus2": [Degree.R, Degree.M9, Degree.P5, Degree.m7],
    "7sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7],
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
}

CHORD_DEGREE_MAP.update(
    {
        # Accordi di settima ed estensioni variate
        "maj7(#11)": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.A4],
        "maj7add13": [Degree.R, Degree.M3, Degree.P5, Degree.M7, Degree.M6],
        "minMaj7": [Degree.R, Degree.m3, Degree.P5, Degree.M7],
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
        "7(#9, #5, b13)": [
            Degree.R,
            Degree.M3,
            Degree.m6,
            Degree.m7,
            Degree.m3,
            Degree.m6,
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
        "9sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7, Degree.M9],
        "13sus4": [Degree.R, Degree.P4, Degree.P5, Degree.m7, Degree.M9, Degree.M6],
        # Accordi 6 e varianti
        "min6add9": [Degree.R, Degree.m3, Degree.P5, Degree.M6, Degree.M9],
    }
)


def extract_chord() -> tuple[str, list[Degree]]:
    """Extract a random chord and its degrees."""

    chord_name = choice(list(CHORD_DEGREE_MAP.keys()))
    chord_degrees = CHORD_DEGREE_MAP[chord_name]
    return chord_name, chord_degrees


def main() -> None:
    """Main function to demonstrate chord extraction."""

    for _ in range(100):
        print(f"X{choice(list(CHORD_DEGREE_MAP.keys()))}")


if __name__ == "__main__":
    main()
