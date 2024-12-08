"""Computation of weighted average of squares."""

import argparse

def average_of_squares(list_of_numbers, list_of_weights=None):
    # 同之前定义，不需要改动
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

def read_numbers_from_file(filename):
    """从文件中读取数字，每行一个数字"""
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file.readlines()]

if __name__ == "__main__":
    # 创建解析器
    parser = argparse.ArgumentParser(description="Compute the average of squares for a list of numbers.")
    
    # 添加参数，支持文件输入
    parser.add_argument(
        "file_numbers",
        metavar="file_numbers",
        type=str,
        help="A text file containing numbers (one per line)."
    )
    parser.add_argument(
        "--weights",
        metavar="file_weights",
        type=str,
        help="An optional text file containing weights (one per line)."
    )
    
    # 解析参数
    args = parser.parse_args()
    
    # 从文件中读取数字和权重
    numbers = read_numbers_from_file(args.file_numbers)
    weights = read_numbers_from_file(args.weights) if args.weights else None

    # 计算结果
    result = average_of_squares(numbers, weights)

    # 打印结果
    print(f"The average of squares is: {result}")
