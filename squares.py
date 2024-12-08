"""Computation of weighted average of squares."""


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
    
    total_weight = sum(effective_weights)
    return sum(squares) / total_weight  # 改为返回加权平均值


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


if __name__ == "__main__":
    import argparse

    # 创建解析器
    parser = argparse.ArgumentParser(description="Compute the average of squares for a list of numbers.")
    
    # 添加命令行参数
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="A list of numbers to compute the average of squares."
    )
    
    # 解析参数
    args = parser.parse_args()
    numbers = args.numbers

    # 暂时不使用权重，固定为 None
    weights = None

    # 调用主函数计算结果
    result = average_of_squares(numbers, weights)

    # 打印结果
    print(f"The average of squares is: {result}")
