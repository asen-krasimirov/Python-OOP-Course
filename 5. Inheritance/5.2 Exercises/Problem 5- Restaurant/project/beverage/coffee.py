from project.beverage.hot_beverage import HotBeverage
# from beverage import HotBeverage


class Coffee(HotBeverage):
    COFFEE_MILLILITERS: int = 50
    COFFEE_PRICE: float = 3.50
    __caffeine: float

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.COFFEE_PRICE, self.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, new_value):
        self.__caffeine = new_value
