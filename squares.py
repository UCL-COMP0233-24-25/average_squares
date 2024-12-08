"""Computation of weighted average of squares."""

import argparse

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values."""
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


if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description="Compute the average of squares for a list of numbers with optional weights.")
    
    # 添加参数
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="A list of numbers to compute the average of squares."
    )
    parser.add_argument(
        "--weights",
        metavar="W",
        type=float,
        nargs="+",
        help="An optional list of weights (must match the number of input numbers)."
    )
    
    # 解析参数
    args = parser.parse_args()
    numbers = args.numbers
    weights = args.weights

    # 验证权重（如果存在）
    if weights and len(weights) != len(numbers):
        raise ValueError("The number of weights must match the number of numbers.")
    
    # 调用主函数计算结果
    result = average_of_squares(numbers, weights)

    # 打印结果
    print(f"The average of squares is: {result}")
