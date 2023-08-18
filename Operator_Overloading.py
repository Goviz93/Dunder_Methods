"""

    Course: Python objects with special methods - Create better classes!.
    Section: 6 More Operators.
    Chapter: 19. Operator Overloading.

    Dunder methods:
        __mul__ -> Enable an object be multiplied.
        __add__ -> Enable an object be added.

"""
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


V1 = Vector(4,3)
print(V1.magnitude())
V1 = V1 * 2
print(V1.magnitude())
V2 = Vector(4,2) + Vector(1,2)
print(V2.magnitude())