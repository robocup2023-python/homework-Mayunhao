n = int(input("请输入一个正整数: "))
print(f"{n}=", end="")

for i in range(2, n + 1):
    while n % i == 0:
        if n == i:
            print(i, end="")
        else:
            print(i, end="*")
        n //= i
        if n == 1:
            break
