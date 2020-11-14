from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return 'Squeak'

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity
        self.food_eaten += food.quantity
