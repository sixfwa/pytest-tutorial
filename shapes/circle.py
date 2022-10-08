import math


class Circle:

    def __init__(self, radius):
        if radius < 1:
            raise ValueError("The radius must be greater than 0.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2