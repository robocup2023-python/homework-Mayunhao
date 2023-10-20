a = input("请输入一个数字 a: ")
n = int(input("请输入重复次数 n: "))
total = 0
current = int(a)

for i in range(n):
    total += current
    current = current * 10 + int(a)

print("s =", total)
