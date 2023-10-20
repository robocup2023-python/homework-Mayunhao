import random

# 打开文件以写入数据
with open('data.txt', 'w') as file:
    # 写入100,000行随机整数
    for _ in range(100000):
        random_integer = random.randint(1, 100)
        file.write(str(random_integer) + '\n')

print("文件 'data.txt' 已创建并写入随机整数。")
