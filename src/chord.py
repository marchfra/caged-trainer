import random
from dataclasses import dataclass
from enum import Enum

from enums import (
    Elevenths,
    Fifths,
    Ninths,
    Roots,
    Seventh,
    Sevenths,
    Thirds,
    Thirteenths,
    Triads,
)
from exceptions import ChordError, SeventhError, TriadError


@dataclass
class Chord:
    root: Roots
    third: Thirds
    fifth: Fifths
    seventh: Sevenths = Sevenths.NONE
    ninth: Ninths = Ninths.NONE
    eleventh: Elevenths = Elevenths.NONE
    thirteenth: Thirteenths = Thirteenths.NONE

    def __init__(self) -> None:
        super().__init__()
        self.root = random.choice(list(Roots))
        self.fifth = self.set_fifth()
        self.third = self.set_third()
        self.components: dict[str, Enum] = {"3": self.third, "5": self.fifth}
        self.triad_type = self.get_triad()
        self.suspended = self.triad_type in (Triads.SUS2, Triads.SUS4)
        self.seventh = self.set_seventh()
        self.components["7"] = self.seventh
        self.seventh_type = self.get_seventh()
        # self.ninth = self.set_ninth()
        # self.components["9"] = self.ninth
        # self.eleventh = self.set_eleventh()
        # self.components["11"] = self.eleventh
        # self.thirteenth = self.set_thirteenth()
        # self.components["13"] = self.thirteenth

    def get_components(self) -> str:
        formatted_components: str = ""
        for key, value in self.components.items():
            if value.name != "NONE":
                formatted_components += f"{key}: {value.name}\n"
        return formatted_components[:-1]

    def set_third(self) -> Thirds:
        if self.fifth == Fifths.SHARP:
            return Thirds.MAJOR
        if self.fifth == Fifths.FLAT:
            return Thirds.MINOR
        return random.choice(list(Thirds))

    def set_fifth(self) -> Fifths:
        return random.choice(list(Fifths))

    def set_seventh(self) -> Sevenths:
        min_weight, maj_weight, dim_weight = 1, 1, 1
        if self.triad_type == Triads.DIMINISHED:
            maj_weight = 0
        elif self.triad_type == Triads.AUGMENTED:
            dim_weight = 0
            min_weight = 0
        else:
            dim_weight = 0
        weights = [1, min_weight, maj_weight, dim_weight]
        return random.choices(list(Sevenths), weights=weights)[0]

    def set_ninth(self) -> Ninths:
        if self.suspended:
            return Ninths.NONE
        if self.third != Thirds.MAJOR:
            aug_weight = 0
        else:
            aug_weight = 1
        weights = [1] * (len(Ninths) - 1) + [aug_weight]
        return random.choices(list(Ninths), weights=weights)[0]

    def set_eleventh(self) -> Elevenths:
        if self.suspended:
            return Elevenths.NONE
        return random.choice(list(Elevenths))

    def set_thirteenth(self) -> Thirteenths:
        if self.seventh == Sevenths.DIMINISHED:
            return Thirteenths.NONE
        return random.choice(list(Thirteenths))

    def is_triad(self) -> bool:
        return (
            self.seventh == Sevenths.NONE
            and self.ninth == Ninths.NONE
            and self.eleventh == Elevenths.NONE
            and self.thirteenth == Thirteenths.NONE
        )

    def get_triad(self) -> Triads:
        if self.fifth == Fifths.PERFECT:
            if self.third == Thirds.MAJOR:
                return Triads.MAJOR
            elif self.third == Thirds.MINOR:
                return Triads.MINOR
            elif self.third == Thirds.SUS2:
                return Triads.SUS2
            elif self.third == Thirds.SUS4:
                return Triads.SUS4
        elif self.fifth == Fifths.SHARP:
            if self.third == Thirds.MAJOR:
                return Triads.AUGMENTED
            else:
                raise TriadError(self.get_components())
        elif self.fifth == Fifths.FLAT:
            if self.third == Thirds.MINOR:
                return Triads.DIMINISHED
            else:
                raise TriadError(self.get_components())
        else:
            raise TriadError(self.get_components())

    def is_seventh(self) -> bool:
        return (
            self.seventh != Sevenths.NONE
            and self.ninth == Ninths.NONE
            and self.eleventh == Elevenths.NONE
            and self.thirteenth == Thirteenths.NONE
        )

    def get_seventh(self) -> Seventh:
        if self.seventh == Sevenths.MINOR:
            if self.triad_type == Triads.MAJOR:
                return Seventh.DOMINANT
            elif self.triad_type == Triads.MINOR:
                return Seventh.MINOR
            elif self.triad_type == Triads.DIMINISHED:
                return Seventh.HALF_DIMINISHED
            elif self.triad_type == Triads.SUS2:
                return Seventh.SUS2
            elif self.triad_type == Triads.SUS4:
                return Seventh.SUS4
            else:
                raise SeventhError(self.get_components())
        elif self.seventh == Sevenths.MAJOR:
            if self.triad_type == Triads.MAJOR:
                return Seventh.MAJOR
            elif self.triad_type == Triads.MINOR:
                return Seventh.MINOR_MAJOR
            elif self.triad_type == Triads.AUGMENTED:
                return Seventh.MAJOR_SHARP_5
            elif self.triad_type == Triads.SUS2:
                return Seventh.MAJOR_SUS2
            elif self.triad_type == Triads.SUS4:
                return Seventh.MAJOR_SUS4
            else:
                raise SeventhError(self.get_components())
        elif self.seventh == Sevenths.DIMINISHED:
            if self.triad_type == Triads.DIMINISHED:
                return Seventh.DIMINISHED
            else:
                raise SeventhError(self.get_components())
        else:
            return Seventh.NONE

    def __str__(self) -> str:
        if self.is_triad():
            return f"{self.root.value:2} {self.get_triad().value}"
        elif self.is_seventh():
            return f"{self.root.value:2} {self.get_seventh().value}"
        else:
            raise ChordError(f"Invalid chord configuration\n{self.get_components()}")


def main() -> None:
    for _ in range(100):
        chord = Chord()
        print(chord)


if __name__ == "__main__":
    main()
