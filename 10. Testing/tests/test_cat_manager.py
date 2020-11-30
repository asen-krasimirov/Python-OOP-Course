from solutions.CarManager.car_manager import Car
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Volkswagen', 'Golf', 2, 10)

    def test_init_correctly_creates_attributes(self):
        make, model, fuel_consumption, fuel_capacity, fuel_amount = \
            self.car.make, self.car.model, self.car.fuel_consumption, self.car.fuel_capacity, self.car.fuel_amount

        self.assertEqual(make, 'Volkswagen')
        self.assertEqual(model, 'Golf')
        self.assertEqual(fuel_consumption, 2)
        self.assertEqual(fuel_capacity, 10)
        self.assertEqual(fuel_amount, 0)

    def test_car_make_setter_correct_and_wrong(self):
        self.car.make = 'test'
        self.assertEqual('test', self.car.make)

        with self.assertRaises(Exception):
            self.car.make = ''

        with self.assertRaises(Exception):
            self.car.make = None

    def test_car_model_setter_correct_and_wrong(self):
        self.car.model = 'test'
        self.assertEqual('test', self.car.model)

        with self.assertRaises(Exception):
            self.car.model = ''

        with self.assertRaises(Exception):
            self.car.model = None

    def test_car_fuel_consumption_setter_correct_and_wrong(self):
        self.car.fuel_consumption = 3
        self.assertEqual(3, self.car.fuel_consumption)

        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_car_fuel_capacity_setter_correct_and_wrong(self):
        self.car.fuel_capacity = 3
        self.assertEqual(3, self.car.fuel_capacity)

        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1
    
    def test_car_fuel_amount_setter_correct_and_wrong(self):
        self.car.fuel_amount = 3
        self.assertEqual(3, self.car.fuel_amount)

        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel_method_refuels_given_amount(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_refuel_method_refuels_up_to_fuel_capacity_if_amount_is_more_then_it(self):
        self.car.refuel(11)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_method_raises_exception_when_given_amount_if_zero_or_negative(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_drive_method_drives_given_distance_and_decrements_fuel_amount(self):
        self.car.refuel(10)
        self.car.drive(1)
        self.assertEqual(9.98, self.car.fuel_amount, self.car.fuel_amount)

    def test_drive_method_not_enough_fuel_to_drive_the_distance(self):
        with self.assertRaises(Exception):
            self.car.drive(1)


if __name__ == '__main__':
    unittest.main()
