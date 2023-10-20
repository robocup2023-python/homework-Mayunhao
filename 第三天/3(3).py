num = int(input("请输入一个正整数: "))
num_str = str(num)
num_length = len(num_str)

print(f"它是{num_length}位数")
print("逆序打印各位数字:")
for i in range(num_length - 1, -1, -1):
    print(num_str[i])
