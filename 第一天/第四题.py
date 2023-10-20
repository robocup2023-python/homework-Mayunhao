for i in range(1, 10):
    for j in range(1, i+1):
        # 计算乘积
        product = i * j
        # 使用制表符"\t"来对齐输出
        print(f"{i} x {j} = {product}\t", end="")
    # 换行
    print()
