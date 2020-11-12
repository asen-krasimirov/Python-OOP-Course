from project.product import Product
# from project import Product


class Food(Product):
    _grams: float

    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self._grams = grams

    @property
    def grams(self):
        return self._grams

    @grams.setter
    def grams(self, new_value):
        self._grams = new_value
