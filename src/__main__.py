import random
import sys

from chords import CHORD_DEGREE_MAP
from enums import Degree, Note, Shape
from modes import SCALES, find_compatible_scale


def main() -> None:
    note, chord_name, chord_degrees, shape = generate_chord()

    print(f"{note:2} {chord_name} in {shape} shape")

    user_modes = get_user_input()
    compatible_modes = find_compatible_scale(chord_degrees)

    compare_modes(user_modes, compatible_modes)


def generate_chord() -> tuple[Note, str, list[Degree], Shape]:
    """Generate a random chord with its note, name, and shape."""
    chord_name = random.choice(list(CHORD_DEGREE_MAP.keys()))
    chord_degrees = CHORD_DEGREE_MAP[chord_name]
    note = random.choice(list(Note)).value
    shape = random.choice(list(Shape)).value

    return note, chord_name, chord_degrees, shape


def get_nth_key_value_pair(d: dict, n: int) -> tuple[str, list]:
    """Get the nth key-value pair from a dictionary."""
    if n < 0 or n >= len(d):
        raise IndexError("Index out of range")
    key = list(d.keys())[n]
    value = d[key]
    return key, value


def get_user_input() -> set[str]:
    """Get user input for modes."""
    user_modes: dict[str, list[Degree]] = {}
    for scale in SCALES:
        print()
        # Print the modes available in the scale
        for i, mode in enumerate(scale):
            print(f"({i + 1}) {mode}")

        answer = input("Select modes: ")

        # Process the user's input
        for idx in answer.split():
            try:
                idx_int = int(idx) - 1
                mode, degrees = get_nth_key_value_pair(scale, idx_int)
                user_modes[mode] = degrees
            except (ValueError, IndexError):
                print(f"Invalid input: {idx + 1}. Please try again.")
                continue
    return set(user_modes.keys())


def compare_modes(user_modes: set[str], compatible_modes: set[str]) -> None:
    """Compare user modes with compatible modes and print results."""
    print(f"\nYou entered the following modes: {', '.join(user_modes)}")
    if user_modes == compatible_modes:
        print("\nYou found all compatible modes!")
    else:
        missing_modes = compatible_modes - user_modes
        if missing_modes:
            print(
                f"\nYou missed the following compatible modes: "
                f"{', '.join(missing_modes)}",
            )
        extra_modes = user_modes - compatible_modes
        if extra_modes:
            print(
                f"\nYou selected extra modes that are not compatible: "
                f"{', '.join(extra_modes)}",
            )


if __name__ == "__main__":
    while True:
        main()
        new_round = input("\nPress any key to continue or 'q' to quit: ")

        if new_round.lower() == "q":
            sys.exit(0)
