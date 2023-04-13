class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def Area(self):
        return self.pi * self.radius ** 2

    def Perimeter(self):
        return 2 * self.pi * self.radius

    def Display(self):
        print("Perimeter:",self.Perimeter())
        print("Area:",self.Area())

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
circle.Display()