

class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    fuel: float
    horse_power = int

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int) -> None:
        if kilometers * self.fuel_consumption > self.fuel:
            return

        self.fuel -= kilometers * self.fuel_consumption

    # TODO: delete after testing
    def __repr__(self):
        return self.__class__.__name__
