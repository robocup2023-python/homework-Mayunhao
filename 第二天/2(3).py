height = 100
total_distance = 100
bounce_height = height

for i in range(2, 11):
    height /= 2
    total_distance += 2 * height
    bounce_height = height

print("第10次落地时，共经过的高度为:", total_distance)
print("第10次反弹的高度为:", bounce_height)

