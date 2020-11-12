from project.food.food import Food


class Dessert(Food):
    _calories: float

    def __init__(self, name: str, price: float, grams: float, calories: float):
        super().__init__(name, price, grams)
        self._calories = calories

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, new_value):
        self._calories = new_value
