from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    name: str
    weight: float
    food_eaten: int

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = float(weight)
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Bird(Animal, ABC):
    wing_size: float

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name=name, weight=weight)
        self.wing_size = wing_size

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    living_region: str

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name=name, weight=weight)
        self.living_region = living_region

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
