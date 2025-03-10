import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

def test_shapes():
    rect = Rectangle(4, 5)
    rect_area = rect.area()
    print(f"Plocha obdélníku: {rect_area}")
    assert rect_area == 20

    circle = Circle(3)
    circle_area = circle.area()
    print(f"Plocha kruhu: {circle_area}")
    assert round(circle_area, 1) == 28.3

if __name__ == "__main__":
    test_shapes()
    print("Všechny testy proběhly úspěšně!")
