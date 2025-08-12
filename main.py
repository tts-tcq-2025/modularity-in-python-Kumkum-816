# main.py
# Entry point for running tests and printing the reference manual.

from color_code_test import test_number_to_pair, test_pair_to_number
from color_code_functions import print_reference_manual


if __name__ == "__main__":
    # Run tests
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)
    test_pair_to_number("Red", "Orange", 7)

    print("All tests passed \n")

    # Print reference manual
    print("Telecom Color Code Reference Manual:\n")
    print_reference_manual()
