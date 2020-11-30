from solutions.vehicle import Car, Truck
import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(10, 1.1)

    def test_drive_successfully_and_reduce_fuel(self):
        start_fuel_quantity = self.car.fuel_quantity
        self.car.drive(1)
        end_fuel_quantity = self.car.fuel_quantity
        result = start_fuel_quantity - end_fuel_quantity

        self.assertEqual(2, result, result)

    def test_drive_not_enough_fuel_to_finish_the_ride(self):
        self.car.drive(6)

        self.assertEqual(10, self.car.fuel_quantity)

    def test_refuel_all_of_the_fuel(self):
        self.car.refuel(1)

        self.assertEqual(11, self.car.fuel_quantity)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(10, 0.4)

    def test_drive_successfully_and_reduce_fuel(self):
        start_fuel_quantity = self.truck.fuel_quantity
        self.truck.drive(1)
        end_fuel_quantity = self.truck.fuel_quantity
        result = start_fuel_quantity - end_fuel_quantity

        self.assertEqual(2, result, result)

    def test_drive_not_enough_fuel_to_finish_the_ride(self):
        self.truck.drive(6)

        self.assertEqual(10, self.truck.fuel_quantity)

    def test_refuel_all_of_the_fuel(self):
        self.truck.refuel(1)

        self.assertEqual(10.95, self.truck.fuel_quantity)


if __name__ == '__main__':
    unittest.main()
