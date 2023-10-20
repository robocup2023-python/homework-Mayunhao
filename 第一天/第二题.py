x = int(input("请输入第一个整数 x: "))
y = int(input("请输入第二个整数 y: "))
z = int(input("请输入第三个整数 z: "))

# 比较 x 和 y，确保 x 存储最小的值
if x > y:
    x, y = y, x

# 再比较 x 和 z，确保 x 存储最小的值
if x > z:
    x, z = z, x

# 此时 x 包含最小值，接下来比较 y 和 z
if y > z:
    y, z = z, y

print("从小到大排序后的结果为:", x, y, z)
