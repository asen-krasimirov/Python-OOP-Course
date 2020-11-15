from project.vehicle.vehicle import Vehicle
from project.capacity_mixin import CapacityMixin


class Car(Vehicle, CapacityMixin):
    __fuel_tank: int
    __fuel_consumption: float
    __fuel: float

    def __init__(self, available_seats: int, __fuel_tank: int, __fuel_consumption: float, fuel: float):
        super().__init__(available_seats)
        self.__fuel_tank = __fuel_tank
        self.__fuel_consumption = __fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    def drive(self, distance):
        if self.fuel < distance * self.__fuel_consumption:
            return

        self.__fuel -= distance * self.__fuel_consumption
        return "We've enjoyed the travel!"

    def refuel(self, liters):
        
        result = super().get_capacity(self.__fuel_tank, self.__fuel + liters)
        if not isinstance(result, str):
            self.__fuel += liters

        return result
