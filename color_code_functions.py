# Core logic for color <-> pair number conversion.

from color_code_constants import MAJOR_COLORS, MINOR_COLORS


def color_pair_to_string(major_color: str, minor_color: str) -> str:
    """Return formatted string from major and minor color."""
    return f"{major_color} {minor_color}"


def get_color_from_pair_number(pair_number: int) -> tuple[str, str]:
    """
    Get major and minor colors from pair number.
    Pair numbers start from 1.
    """
    if pair_number < 1 or pair_number > len(MAJOR_COLORS) * len(MINOR_COLORS):
        raise ValueError("Pair number out of range")

    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)

    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color: str, minor_color: str) -> int:
    """Get pair number from major and minor colors."""
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise ValueError(f"Invalid major color: {major_color}")

    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise ValueError(f"Invalid minor color: {minor_color}")

    return major_index * len(MINOR_COLORS) + minor_index + 1


def print_reference_manual() -> None:
    """Prints the telecom color code mapping for all pairs."""
    print(f"{'Pair No':<7} | {'Major Color':<12} | {'Minor Color'}")
    print("-" * 35)
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major, minor = get_color_from_pair_number(pair_number)
        print(f"{pair_number:<7} | {major:<12} | {minor}")
