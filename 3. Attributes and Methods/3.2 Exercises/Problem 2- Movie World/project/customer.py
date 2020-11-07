from typing import List
from .dvd import DVD


class Customer:
    name: str
    age: int
    id: int
    rented_dvds: List[DVD]

    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})"

    def has_dvd(self, dvd: DVD):
        return dvd.id in [d.id for d in self.rented_dvds]

    def rent_dvd(self, dvd: DVD):
        self.rented_dvds.append(dvd)

    def return_dvd(self, dvd: DVD):
        self.rented_dvds.remove(dvd)
