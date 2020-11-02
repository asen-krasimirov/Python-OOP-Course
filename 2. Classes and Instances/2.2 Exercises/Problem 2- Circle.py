

class Circle:
    pi = 3.14
    radius: int

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        result = Circle.pi * (self.radius ** 2)
        return float(f"{result :.2f}")

    def get_circumference(self) -> float:
        result = 2 * Circle.pi * self.radius
        return float(f"{result :.2f}")


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
