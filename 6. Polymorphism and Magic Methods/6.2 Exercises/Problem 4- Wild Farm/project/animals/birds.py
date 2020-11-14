from project.animals.animal import Bird
from project.food import *


class Owl(Bird):

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):

    @staticmethod
    def make_sound():
        return 'Cluck'

    def feed(self, food: Food):

        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
