from project.product import Product
from project.food.cake import Cake
from project.food.dessert import Dessert
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.salmon import Salmon
from project.food.soup import Soup
from project.food.starter import Starter
from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.cold_beverage import ColdBeverage
from project.beverage.hot_beverage import HotBeverage
from project.beverage.tea import Tea


# objects = [
#     Product('product', 1.1),
#     Food('food', 2.2, 100),
#     MainDish('main dish', 3.3, 200),
#     Salmon('salmon', 4.4, 300),
#     Dessert('dessert', 5.5, 300, 100),
#     Cake('cake', 6.6, 400, 200),
#     Starter('starter', 7.7, 500),
#     Soup('soup', 8.8, 600),
#     Beverage('beverage', 9.9, 100),
#     HotBeverage('hot beverage', 10.10, 200),
#     Coffee('coffee', 11.11, 300, 100),
#     Tea('tea', 12.12, 400),
#     ColdBeverage('cold beverage', 13.13, 500),
# ]


def mro_test():
    print('mro tests:')
    for object_ in objects:
        object_name = object_.__class__.__name__
        object_mro_names = [ob.__name__ for ob in object_.__class__.mro()]
        print(f'name: {object_name} mro: {object_mro_names}')
    print('test completed')


attributes = {
    'Product': ('name', 'price'),
    'Food': ('name', 'price', 'grams'),
    'Beverage': ('name', 'price', 'milliliters'),
    'MainDish': ('name', 'price', 'grams'),
    'Starter': ('name', 'price', 'grams'),
    'Dessert': ('name', 'price', 'grams', 'calories'),
    'Cake': ('name', 'price', 'grams', 'calories'),
    'Salmon': ('name', 'price', 'grams'),
    'Soup': ('name', 'price', 'grams'),
    'HotBeverage': ('name', 'price', 'milliliters'),
    'ColdBeverage': ('name', 'price', 'milliliters'),
    'Tea': ('name', 'price', 'milliliters'),
    'Coffee': ('name', 'price', 'milliliters', 'caffeine'),
}


def attribute_test():
    print('attribute tests')
    for object_ in objects:
        object_name = object_.__class__.__name__
        present_attribute = attributes[object_name]
        correct_presence = all([hasattr(object_, attr) for attr in present_attribute])
        assert correct_presence, 'missing attribute'
    print('tests passed')


special_var_objects = [
    Coffee('name', 100),
    Dessert('name', 123, 123, 123),
    Cake('name'),
    Salmon('name', 123)
]


def special_var_test():
    print('special vat tests:')
    for special_object in special_var_objects:
        object_name = special_object.__class__.__name__
        if object_name == 'Coffee':
            loc_special_vars = all([
                hasattr(special_object.__class__, 'COFFEE_MILLILITERS'),
                hasattr(special_object.__class__, 'COFFEE_PRICE'),
                hasattr(special_object, 'caffeine')
            ])
            assert loc_special_vars
        if object_name == 'Dessert':
            loc_special_vars = all([
                hasattr(special_object, 'calories')
            ])
            assert loc_special_vars
        if object_name == 'Cake':
            loc_special_vars = [
                hasattr(special_object.__class__, 'CAKE_GRAMS'),
                hasattr(special_object.__class__, 'CAKE_CALORIES'),
                hasattr(special_object.__class__, 'CAKE_PRICE')
            ]
            for loc_var in loc_special_vars:
                assert loc_var, loc_var
        if object_name == 'Salmon':
            loc_special_vars = all([
                hasattr(special_object.__class__, 'SALMON_GRAMS')
            ])
            assert loc_special_vars
    print('test passed')


def getter_test():
    print('getter tests')
    for local_object in objects:
        if 'calories' in attributes[local_object.__class__.__name__]:
            print('calories')
            print(local_object.calories)
        if 'milliliters' in attributes[local_object.__class__.__name__]:
            print('milliliters')
            print(local_object.milliliters)
        if 'caffeine' in attributes[local_object.__class__.__name__]:
            print('caffeine')
            print(local_object.caffeine)
    print('test passed')


# attribute_test()
# mro_test()
#
# salmon = Salmon('salmon', 4.44)
# print(salmon.grams)
# cake = Cake('cake')
# print(cake.__dict__)
special_var_test()
