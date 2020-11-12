

class Product:
    _name: str
    _price: float

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_value):
        self._price = new_value