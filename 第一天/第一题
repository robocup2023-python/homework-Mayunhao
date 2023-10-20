count = 0  # 用于计数符合条件的三位数的个数

# 使用三重循环遍历百位、十位和个位
for i in range(1, 5):  # 百位
    for j in range(1, 5):  # 十位
        for k in range(1, 5):  # 个位
            # 判断是否数字互不相同
            if i != j and i != k and j != k:
                # 组合成三位数
                num = i * 100 + j * 10 + k
                print(num)  # 打印满足条件的三位数
                count += 1

print("总共有", count, "个满足条件的三位数。")
