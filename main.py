import random

from src.enums import Degree, Note, Shape
from src.extract_chord import extract_chord
from src.modes import SCALES, find_compatible_scale


def get_nth_key_value_pair(d: dict, n: int) -> tuple[str, list]:
    """Get the nth key-value pair from a dictionary."""

    if n < 0 or n >= len(d):
        raise IndexError("Index out of range")
    key = list(d.keys())[n]
    value = d[key]
    return key, value


def main() -> None:
    chord = extract_chord()
    note = random.choice(list(Note))
    shape = random.choice(list(Shape))

    print(f"{note.value:2} {chord[0]} in {shape.value} shape")

    compatible_modes = find_compatible_scale(chord[1])
    user_modes: dict[str, list[Degree]] = {}
    for scale in SCALES:
        print()
        for i, mode in enumerate(scale):
            print(f"({i + 1}) {mode}")
        answer = input("Select modes separated by a space (or 'q' to quit): ")
        if answer.lower() == "q":
            break
        for idx in answer.split():
            try:
                idx = int(idx) - 1
                mode, degrees = get_nth_key_value_pair(scale, idx)
                user_modes[mode] = degrees
            except (ValueError, IndexError):
                print(f"Invalid input: {idx + 1}. Please try again.")
                continue

    user_set = set(user_modes.keys())
    compatible_set = set(compatible_modes.keys())
    if user_set == compatible_set:
        print("\nYou found all compatible modes!")
    else:
        missing_modes = compatible_set - user_set
        if missing_modes:
            print(
                f"\nYou missed the following compatible modes: {', '.join(missing_modes)}"
            )
        extra_modes = user_set - compatible_set
        if extra_modes:
            print(
                f"\nYou selected extra modes that are not compatible: {', '.join(extra_modes)}"
            )


if __name__ == "__main__":
    main()
