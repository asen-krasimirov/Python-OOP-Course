from abc import abstractmethod, ABC
from typing import List


class Robot:
    def __init__(self, type):
        self.__type = type

    @property
    def type(self):
        return self.__type

    @abstractmethod
    def sensors_count(self):
        pass


class Android(Robot):

    def sensors_count(self):
        return 4


class Chappie(Robot):
    def sensors_count(self):
        return 6


def count_robot_senzors(robots: List[Robot]):
    for robot in robots:
        print(robot.type)
        print(robot.sensors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)


class Product(ABC):

    @abstractmethod
    def get_product_information(self):
        pass

    @abstractmethod
    def buy_product(self):
        pass


class Stake(Product):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_bought = False

    def get_product_information(self):
        return name, price

    def buy_product(self):
        self.is_bought = True