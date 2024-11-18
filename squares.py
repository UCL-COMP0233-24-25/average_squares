"""Computation of weighted average of squares."""
from argparse import ArgumentParser

def average_of_squares(list_of_numbers, list_of_weights=None):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Parameters
    ----------
    list_of_strings : list of str
        A list of strings where each string contains one or more numbers
        separated by whitespace.

    Returns
    -------
    list of int
        A list of integers parsed from the input strings.

    Examples
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]
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
    total_weight = sum(effective_weights)
    return sum(squares) / total_weight


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Parameters
    ----------
    list_of_strings : list of str
        A list of strings where each string contains one or more numbers
        separated by whitespace.

    Returns
    -------
    list of int
        A list of integers parsed from the input strings.

    Examples
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]
    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend(s.split())
    # ...then convert each substring into a number
    return [int(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    #numbers_strings = ["1","2","4"]
    #weight_strings = ["1","1","1"]        

    parser = ArgumentParser(description="Computation of weighted average of squares")
    parser.add_argument('numbers_strings', nargs="+")
    parser.add_argument('--weight_strings', '-w',  nargs="*")
    arguments= parser.parse_args()

    numbers = convert_numbers(arguments.numbers_strings)
    weights = convert_numbers(arguments.weight_strings)
    result = average_of_squares(numbers, weights)

    print(result)