num = int(input("请输入一个正整数: "))
num_str = str(num)

if num_str == num_str[::-1]:
    print("是回文数")
else:
    print("不是回文数")
