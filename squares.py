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


def read_numbers_from_file(file_path):
    """Read numbers from a text file, one per line."""
    with open(file_path, 'r') as file:
        return [float(line.strip()) for line in file.readlines()]


if __name__ == "__main__":
    #numbers_strings = ["1","2","4"]
    #weight_strings = ["1","1","1"]        

    parser = ArgumentParser(description="Computation of weighted average of squares")
    parser.add_argument('file_numbers', type=str)
    parser.add_argument('--file_weights', '-w', type=str)
    arguments= parser.parse_args()

    numbers = read_numbers_from_file(arguments.file_numbers)
    weights = read_numbers_from_file(arguments.file_weights) if arguments.file_weights else None

    result = average_of_squares(numbers, weights)

    print(result)