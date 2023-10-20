n = int(input("请输入列表中的元素个数 n: "))
m = int(input("请输入向后移动的位置 m: "))

my_list = []
for i in range(n):
    my_list.append(int(input(f"请输入第 {i + 1} 个整数: "))

for i in range(m):
    my_list.insert(0, my_list.pop())

print("移动后的列表:", my_list)
