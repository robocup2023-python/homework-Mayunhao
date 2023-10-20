# 定义一个递归函数来生成斐波那契数列的前20项
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 输出前20项斐波那契数列
for i in range(20):
    print(fibonacci(i), end=" ")
两种方法都会生成斐波那契数列的前20项并进行输
