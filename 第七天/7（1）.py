import random
import statistics

# 创建一个包含随机数的文件
with open('data.txt', 'w') as file:
    for _ in range(10):
        row = [random.randint(1, 100) for _ in range(3)]
        file.write(','.join(map(str, row)) + '\n')

# 读取文件并解析数据
data = []
with open('data.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        data.append(int(values[1]))  # 第二列的值

# 计算第二列的最大值、最小值、平均值和中位数
max_value = max(data)
min_value = min(data)
average_value = sum(data) / len(data)
median_value = statistics.median(data)

print("第二列的最大值:", max_value)
print("第二列的最小值:", min_value)
print("第二列的平均值:", average_value)
print("第二列的中位数:", median_va
