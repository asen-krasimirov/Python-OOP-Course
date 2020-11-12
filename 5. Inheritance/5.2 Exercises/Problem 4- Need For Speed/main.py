from project import *


all_objects_ = [
    Vehicle(1000, 1),
    Motorcycle(1000, 2),
    RaceMotorcycle(1000, 3),
    CrossMotorcycle(1000, 4),
    Car(1000, 5),
    FamilyCar(1000, 6),
    SportCar(1000, 7),
]


variable_fuel_consumption_values = [
    Vehicle(1000, 1),
    SportCar(1000, 7),
    RaceMotorcycle(1000, 3),
    Car(1000, 5)
]


def attribute_presence():
    for object_ in all_objects_:
        assert hasattr(object_, 'fuel_consumption'), 'missing fuel_consumption var'
        assert hasattr(object_, 'fuel'), 'missing fuel var '
        assert hasattr(object_, 'horse_power'), 'missing •	horse_power var'
    print('test passed')


def mro_test():
    for object_ in all_objects_:
        print(f'object name: {object_} mro: {[ob.__name__ for ob in object_.__class__.mro()]}')
    print('test completed')


def fuel_consumption_value_test():
    for object_ in variable_fuel_consumption_values:
        error_msg = 'wrong default value'
        if object_.__class__.__name__ == 'Vehicle':
            assert object_.__class__.DEFAULT_FUEL_CONSUMPTION == 1.25, error_msg
        if object_.__class__.__name__ == 'SportCar':
            assert object_.__class__.DEFAULT_FUEL_CONSUMPTION == 10, error_msg
        if object_.__class__.__name__ == 'RaceMotorcycle':
            assert object_.__class__.DEFAULT_FUEL_CONSUMPTION == 8, error_msg
        if object_.__class__.__name__ == 'Car':
            assert object_.__class__.DEFAULT_FUEL_CONSUMPTION == 3, error_msg
    print('test passed')


print('attribute tests: ')
attribute_presence()
print('mro_tests: ')
mro_test()
print('fuel_value tests: ')
fuel_consumption_value_test()
