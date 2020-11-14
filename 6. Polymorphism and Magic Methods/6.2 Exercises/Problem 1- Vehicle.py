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


def car_test():
    car = Car(20, 5)
    car.drive(3)
    assert car.fuel_quantity == 2.299999999999997, car.fuel_quantity
    car.refuel(10)
    assert car.fuel_quantity == 12.299999999999997, car.fuel_quantity


def truck_test():
    truck = Truck(100, 15)
    truck.drive(5)
    assert truck.fuel_quantity == 17.0, fuel_quantity
    truck.refuel(50)
    assert truck.fuel_quantity == 64.5, fuel_quantity


car_test()
print('car passed')
truck_test()
print('truck passed')
