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
        effective_weights = [x/len(list_of_numbers) for x in list_of_weights]
    else:
        effective_weights = [1/len(list_of_numbers)] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
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




def read_numbers_from_file(filename):
    """Read numbers from a text file, assuming each number is on a new line or space-separated."""
    with open(filename, 'r') as file:
        content = file.read()
        return [float(x) for x in content.split()]
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the average of squares of given numbers")
    parser.add_argument(
        'file_numbers',
        type=str,  # Accept one or more numbers
        help='A sequence of numbers to be processed'
    )
    parser.add_argument(
        '--weights',
        type=str,  # Accept one or more numbers
        help='A sequence of weights to be processed'
    )
    


    # Parse the arguments
    args = parser.parse_args()
    
    numbers = read_numbers_from_file(args.file_numbers)
    
    # Read weights if the --weights argument is provided
    if args.weights:
        weights = read_numbers_from_file(args.weights)
    else:
        weights = None   
    
    result = average_of_squares(numbers, weights)
    
    print(result)