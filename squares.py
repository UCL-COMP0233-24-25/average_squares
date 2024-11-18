"""Computation of weighted average of squares."""

from argparse import ArgumentParser


def average_of_squares(list_of_numbers, list_of_weights=None):
    """Return the weighted average of a list of values.

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
        assert len(list_of_weights) == len(
            list_of_numbers
        ), "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)

    weighted_squares = [
        weight * number * number
        for number, weight in zip(list_of_numbers, effective_weights)
    ]
    total_weight = sum(effective_weights)

    return sum(weighted_squares) / total_weight


if __name__ == "__main__":
    parser = ArgumentParser(description="Compute weighted average of squares")
    parser.add_argument(
        "numbers",
        type=float,
        nargs="+",
        help="A list of numbers to calculate average weighted squares of",
    )

    parser.add_argument(
        "--weights",
        type=float,
        nargs="+",
        help="A list of numbers to use as weights",
    )

    args = parser.parse_args()

    result = average_of_squares(args.numbers, args.weights)

    print(result)
