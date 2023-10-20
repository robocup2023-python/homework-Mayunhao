total_people = 233
step = 3

# 初始化人员列表
people = list(range(1, total_people + 1))

# 初始化计数器
count = 0

# 初始化当前位置
position = 0

while len(people) > 1:
    count += 1
    position += 1

    if position >= len(people):
        position = 0

    if count == step:
        people.pop(position)
        position -= 1  # 删除元素后，需要减1来保持正确的位置
        count = 0

print("最后留下的是原来的第", people[0], "号")
