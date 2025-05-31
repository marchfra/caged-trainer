from enum import Enum, auto


class Roots(Enum):
    C = "C"
    C_SHARP = "C#"
    D = "D"
    D_SHARP = "D#"
    E = "E"
    F = "F"
    F_SHARP = "F#"
    G = "G"
    G_SHARP = "G#"
    A = "A"
    A_SHARP = "A#"
    B = "B"


class Thirds(Enum):
    MAJOR = auto()
    MINOR = auto()
    SUS2 = auto()
    SUS4 = auto()


class Fifths(Enum):
    PERFECT = auto()
    SHARP = auto()
    FLAT = auto()


class Sevenths(Enum):
    NONE = auto()
    MINOR = auto()
    MAJOR = auto()
    DIMINISHED = auto()


class Ninths(Enum):
    NONE = auto()
    MAJOR = auto()
    MINOR = auto()
    SHARP = auto()


class Elevenths(Enum):
    NONE = auto()
    PERFECT = auto()
    SHARP = auto()


class Thirteenths(Enum):
    NONE = auto()
    MAJOR = auto()
    MINOR = auto()


class Triads(Enum):
    MAJOR = "Major"
    MINOR = "Minor"
    AUGMENTED = "Augmented"
    DIMINISHED = "Diminished"
    SUS2 = "sus2"
    SUS4 = "sus4"


class Seventh(Enum):
    NONE = "NONE"
    DOMINANT = "7"
    DOMINANT_SHARP_5 = "7(#5)"
    MINOR = "min7"
    HALF_DIMINISHED = "min7(b5)"
    MAJOR = "Maj7"
    DIMINISHED = "dim7"
    MINOR_MAJOR = "minMaj7"
    MAJOR_SHARP_5 = "Maj7(#5)"
    MAJOR_SUS2 = "Maj7(sus2)"
    MAJOR_SUS4 = "Maj7(sus4)"
    SUS2 = "7(sus2)"
    SUS4 = "7(sus4)"


class Quadriads(Enum):
    # Ninths
    ADD_9 = "add9"
    FLAT_9 = "(b9)"
    SHARP_9 = "(#9)"
    # Elevenths
    ADD_11 = "add11"
    SHARP_11 = "(#11)"
    # Thirteenths
    ADD_13 = "add13"
    FLAT_13 = "(b13)"
    SHARP_13 = "(#13)"
    MAJOR_6 = "Maj6"
    MINOR_6 = "min6"
