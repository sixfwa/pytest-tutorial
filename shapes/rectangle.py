class Rectangle:
    def __init__(self, width, height):
        if width < 1 or height < 1:
            raise ValueError("The width and height must be greater than 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def is_square(self):
        return self.width == self.height

