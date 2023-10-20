import math

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Point({self.x}, {self.y}, {self.z})")

    def __del__(self):
        print(f"销毁了Point({self.x}, {self.y}, {self.z})")

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Unsupported operation: Point + Point")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Unsupported operation: Point - Point")

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.distance_to_origin() < other.distance_to_origin()
        raise TypeError("Unsupported operation: Point < Vector")

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Vector({self.x}, {self.y}, {self.z})")

    def __del__(self):
        print(f"销毁了Vector({self.x}, {self.y}, {self.z})")

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Unsupported operation: Vector + Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Unsupported operation: Vector - Vector")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __mul__(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        new_x = self.x * math.cos(angle_radians) - self.y * math.sin(angle_radians)
        new_y = self.x * math.sin(angle_radians) + self.y * math.cos(angle_radians)
        return Vector(new_x, new_y, self.z)

    def __truediv__(self, angle_degrees):
        return self * (-angle_degrees)

# 示例用法
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(p1 + v1)
print(p1 - p2)
print(p1 == Point(1, 2, 3))
print(p1 < p2)
print(v1 * 30)
print(v1 / 30)
