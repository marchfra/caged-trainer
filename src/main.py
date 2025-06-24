import random
import sys
from typing import TYPE_CHECKING

from chords import CHORD_DEGREE_MAP
from enums import Degree, Note, Shape
from modes import SCALES, find_compatible_scale

if TYPE_CHECKING:
    from custom_types import IntervalStructure


def main() -> None:
    note, chord_name, chord_degrees, shape = generate_chord()

    print(f"{note:2} {chord_name} in {shape} shape")

    user_modes = get_user_input()
    compatible_modes = find_compatible_scale(chord_degrees)

    output = compare_modes(user_modes, compatible_modes)
    print(output)


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
    """Prompt the user to select modes for each scale defined in SCALES.

    For each scale, displays the available modes and asks the user to input their
    selections by entering space-separated numbers corresponding to the modes. The
    function processes the input, validates it, and collects the selected modes.

    Returns:
        set[str]: A set containing the names of the selected modes.

    Raises:
        None directly, but prints error messages for invalid input (non-integer or
        out-of-range values).

    """
    user_modes: IntervalStructure = {}
    for name, scale in SCALES.items():
        print(f"\n{name}:")
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


def compare_modes(user_modes: set[str], compatible_modes: set[str]) -> str:
    """Compare the user's modes with a set of compatible modes and generate a message.

    Args:
        user_modes : set[str]
                The set of modes entered by the user.
        compatible_modes : set[str]
                The set of modes considered compatible.

    Returns:
        str: A formatted string summarizing:
            - The modes entered by the user.
            - Whether all compatible modes were found.
            - Any compatible modes that were missed.
            - Any extra modes selected by the user that are not compatible.

    """
    output = ""
    if user_modes:
        output += f"\nYou entered the following modes: {', '.join(user_modes)}\n"
    if user_modes == compatible_modes:
        output += "\nYou found all compatible modes!"
    else:
        missing_modes = compatible_modes - user_modes
        if missing_modes:
            output += "\nYou missed the following compatible modes: "
            output += f"{', '.join(missing_modes)}\n"

        extra_modes = user_modes - compatible_modes
        if extra_modes:
            output += "\nYou selected extra modes that are not compatible: "
            output += f"{', '.join(extra_modes)}\n"

    return output


if __name__ == "__main__":
    while True:
        main()
        new_round = input("\nPress any key to continue or 'q' to quit: ")

        if new_round.lower() == "q":
            sys.exit(0)
