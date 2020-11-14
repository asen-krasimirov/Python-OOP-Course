from project.food import *
from project.animals.birds import *
from project.animals.mammals import *


all_animals = [
    Owl('owl1', 10, 19),
    Hen('hen1', 10, 19),
    Mouse('hen1', 10, 'ananas palace'),
    Dog('hen1', 10, 'ananas palace'),
    Cat('hen1', 10, 'ananas palace'),
    Tiger('hen1', 10, 'ananas palace')
]


def main():
    def animal_feed_properly_test(animal_type, food_type, expected_weight):
        food = food_type(10)
        cur_animal = animal_type('Pilly', 10, 19)
        cur_animal.feed(food)
        assert cur_animal.weight == expected_weight, cur_animal.weight
        assert cur_animal.food_eaten == 10, cur_animal.food_eaten
        print(f'all_animal_feed_properly_test for {animal_type.__name__} Test passed')

    def feed_tests():
        print('Feed tests: ')
        animal_feed_properly_test(Owl, Meat, 12.5)
        animal_feed_properly_test(Hen, Meat, 13.5)
        animal_feed_properly_test(Mouse, Vegetable, 11)
        animal_feed_properly_test(Mouse, Fruit, 11)
        animal_feed_properly_test(Cat, Vegetable, 13)
        animal_feed_properly_test(Cat, Meat, 13)
        animal_feed_properly_test(Dog, Meat, 14)
        animal_feed_properly_test(Tiger, Meat, 20)

    def wrong_animal_feed_properly_test(animal_type, food_type):
        food = food_type(10)
        cur_animal = animal_type('Pilly', 10, 19)

        assert cur_animal.feed(food) == f"{animal_type.__name__} does not eat {food_type.__name__}!"
        print(f'wrong_food_owl_test for {animal_type.__name__} Test passed')

    def wrong_feed_tests():
        print('Wrong feed tests: ')
        wrong_animal_feed_properly_test(Owl, Fruit)
        wrong_animal_feed_properly_test(Mouse, Meat)
        wrong_animal_feed_properly_test(Cat, Fruit)
        wrong_animal_feed_properly_test(Dog, Fruit)
        wrong_animal_feed_properly_test(Tiger, Fruit)

    def sound_making_test():
        print('Animal sound tests:')
        for animal in all_animals:
            print(animal.make_sound())
        print('sound_making_test Test completed')

    def print_repr_():
        print('__repr__ tests:')
        food = Meat(4)
        for animal in all_animals:
            animal.feed(food)
            print(animal)
        print('__repr__ completed')

    feed_tests()
    wrong_feed_tests()
    print_repr_()
    sound_making_test()


def test_one():
    owl = Owl("Pip", 10, 10)
    print(owl)
    meat = Meat(4)
    print(owl.make_sound())
    owl.feed(meat)
    veg = Vegetable(1)
    print(owl.feed(veg))
    print(owl)


def test_two():
    hen = Hen("Harry", 10, 10)
    veg = Vegetable(3)
    fruit = Fruit(5)
    meat = Meat(1)
    print(hen)
    print(hen.make_sound())
    hen.feed(veg)
    hen.feed(fruit)
    hen.feed(meat)
    print(hen)


if __name__ == '__main__':
    main()
    # test_one()
    # test_two()
