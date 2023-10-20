import os
import random
import time

class Universe:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.world = [[False] * width for _ in range(height)]
        self.new_world = [[False] * width for _ in range(height)]

    def seed(self):
        for row in range(self.height):
            for col in range(self.width):
                if random.random() < 0.25:
                    self.world[row][col] = True

    def show(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in range(self.height):
            for col in range(self.width):
                print('*' if self.world[row][col] else ' ', end=' ')
            print()
        time.sleep(0.2)

    def is_alive(self, row, col):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return False
        return self.world[row][col]

    def count_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if self.is_alive(row + dr, col + dc):
                    count += 1
        return count

    def next(self):
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)
                if self.world[row][col]:
                    if neighbors < 2 or neighbors > 3:
                        self.new_world[row][col] = False
                    else:
                        self.new_world[row][col] = True
                else:
                    if neighbors == 3:
                        self.new_world[row][col] = True
        self.world, self.new_world = self.new_world, self.world

def main():
    height = 15
    width = 80
    universe = Universe(height, width)
    universe.seed()

    while True:
        universe.show()
        universe.next()

if __name__ == "__main__":
    main()
