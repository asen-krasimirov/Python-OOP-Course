from operator import add, mul, truediv, sub
from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(add, args)

    @staticmethod
    def multiply(*args):
        return reduce(mul, args)

    @staticmethod
    def divide(*args):
        return reduce(truediv, args)

    @staticmethod
    def subtract(*args):
        return reduce(sub, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
