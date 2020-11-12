from project.product import Product
# from project import Product


class Beverage(Product):
    _milliliters: float

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, new_value):
        self._milliliters = new_value
