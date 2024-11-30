"""Computation of weighted average of squares."""

import argparse


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def read_numbers_from_file(filename):
    """Read numbers from a file, assuming a single line of space-separated numbers."""
    with open(filename, 'r') as file:
        line = file.readline()
        return [float(num) for num in line.split()]
    

def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


def process():
    parser = argparse.ArgumentParser(description="Compute the weighted average of squares of numbers.")

    parser.add_argument(
        "file_numbers",
        help="File containing a single row of numbers to compute the average of squares."
    )

    parser.add_argument(
        "--weights",
        help="A list of weights used for calculate weighted average."
    )

    args = parser.parse_args()

    numbers = read_numbers_from_file(args.file_numbers)

    weights = read_numbers_from_file(args.weights) if args.weights else None

    result = average_of_squares(numbers, weights)

    print(result)


if __name__ == "__main__":
    process()
