class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


r = float(input("Enter the radius of circle: "))
circle = Circle(r)

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
rec = Rectangle(l, b)

h = int(input("Enter the height of triangle: "))
b = int(input("Enter the base of triangle: "))
triangle = Triangle(b, h)

shapes = [circle, rec, triangle]

for shape in shapes:
    print("Area of", type(shape).__name__, "=", shape.area())