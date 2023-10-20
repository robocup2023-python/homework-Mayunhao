def calculate(*args):
    if len(args) == 0:
        return (0, [])

    average = sum(args) / len(args)
    above_average_indices = [i for i, num in enumerate(args) if num > average]

    return (average, above_average_indices)

# 示例用法
result = calculate(1, 2, 3, 4, 5)
print("平均值:", result[0])
print("大于平均值的索引:", result[1])
