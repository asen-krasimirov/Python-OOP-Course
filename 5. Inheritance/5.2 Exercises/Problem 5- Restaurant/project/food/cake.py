from project.food.dessert import Dessert


class Cake(Dessert):
    # TODO: this might be date to overwrite the data from the respective parent
    CAKE_GRAMS: int = 250
    CAKE_CALORIES: int = 1000
    CAKE_PRICE: int = 5

    def __init__(self, name: str):
        super().__init__(name, self.CAKE_PRICE, self.CAKE_GRAMS, self.CAKE_CALORIES)