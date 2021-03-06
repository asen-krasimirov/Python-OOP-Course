from collections import defaultdict
from typing import Dict, Union


class PizzaDelivery:
    name: str
    price: float
    ingredients: Dict[str, int]
    ordered: bool

    def __init__(self, name: str, price: float, ingredients: Dict[str, int]):
        self.name = name
        self.price = price
        self.ingredients = defaultdict(int, ingredients)
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float) -> Union[str, None]:

        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        self.ingredients[ingredient] += quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float) -> Union[str, None]:

        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def pizza_ordered(self) -> str:
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{ingredient}: {quantity}' for ingredient, quantity in self.ingredients.items()])} and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))
print(Margarita.remove_ingredient('cheese', 1, 1))
