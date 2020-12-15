from abc import ABC, abstractmethod, abstractproperty
from typing import List


class Animal(ABC):
    
    def __init__(self, species):
        self.__species = species
    
    @property
    def species(self):
        return self.__species
    
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    
    def make_sound(self):
        return 'woof-woof'


class Chicken(Animal):
    
    def make_sound(self):
        return 'chick chirick'


"""
добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него                  
при добавяне на нови животни
"""


def animal_sound(animals: List[Animal]):

    for animal in animals:
        print(animal.make_sound())


def test_one():
    animals = [Cat('cat'), Dog('dog')]
    animals2 = [Cat('cat'), Dog('dog'), Chicken('chicken')]
    animal_sound(animals)
    print()
    animal_sound(animals2)


test_one()
