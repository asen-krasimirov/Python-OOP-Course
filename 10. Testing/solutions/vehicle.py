from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    BONUS_FUEL_CONSUMPTION: float = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumed_fuel = distance * (self.fuel_consumption + self.BONUS_FUEL_CONSUMPTION)
        if self.fuel_quantity >= consumed_fuel:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    BONUS_FUEL_CONSUMPTION: float = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumed_fuel = distance * (self.fuel_consumption + self.BONUS_FUEL_CONSUMPTION)
        if self.fuel_quantity >= consumed_fuel:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
