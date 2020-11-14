from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius**2

    def calculate_perimeter(self):
        return 2*pi * self.__radius


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2*(self.__height+self.__width)


def circle_test():
    circle = Circle(5)
    assert circle.calculate_area() == 78.53981633974483
    assert circle.calculate_perimeter() == 31.41592653589793


def rectangle_test():
    rectangle = Rectangle(10, 20)
    assert rectangle.calculate_area() == 200
    assert rectangle.calculate_perimeter() == 60


circle_test()
rectangle_test()
