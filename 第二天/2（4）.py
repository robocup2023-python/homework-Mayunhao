for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    sum_of_cubes = hundreds ** 3 + tens ** 3 + ones ** 3

    if num == sum_of_cubes:
        print(num)
