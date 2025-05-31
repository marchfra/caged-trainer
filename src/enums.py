from enum import Enum


class Degree(Enum):
    R = "Root"
    m9 = "b9"
    M9 = "9"
    m3 = "b3"
    M3 = "3"
    P4 = "4"
    A4 = "#4"
    P5 = "5"
    m6 = "b6"
    M6 = "6"
    m7 = "b7"
    M7 = "7"


class Note(Enum):
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


class Shape(Enum):
    C = "C"
    A = "A"
    G = "G"
    E = "E"
    D = "D"
