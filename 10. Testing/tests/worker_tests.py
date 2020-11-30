from solutions.worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Boris', 20, 16)

    def test_attributes(self):
        name, salary, energy, money = self.worker.name, self.worker.salary, self.worker.energy, self.worker.money

        self.assertEqual(name, "Boris")
        self.assertEqual(salary, 20)
        self.assertEqual(energy, 16)
        self.assertEqual(money, 0)

        self.assertNotEqual(name, "Deqn")
        self.assertNotEqual(salary, 30)
        self.assertNotEqual(energy, 59)
        self.assertNotEqual(money, 1)

    def test_energy_incremented_when_rest(self):
        energy = self.worker.energy
        self.worker.rest()
        result = self.worker.energy - energy

        self.assertEqual(result, 1, result)
        self.assertNotEqual(result, 3, result)

    def test_working_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as exc:
            self.worker.work()
            self.assertEqual(str(exc), 'Not enough energy.')

    def test_working_with_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as exc:
            self.worker.work()
            self.assertEqual(str(exc), 'Not enough energy.')

    def test_working_with_enough_energy(self):
        self.worker.energy = 2
        self.worker.work()
        self.assertEqual(self.worker.energy, 1, self.worker.energy)

    def test_money_increases_by_salary_after_work(self):
        start_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money, start_money + self.worker.salary, self.worker.salary)

    def test_energy_decreases_after_working(self):
        start_energy = self.worker.energy
        self.worker.work()
        end_energy = self.worker.energy
        result = start_energy - end_energy

        self.assertEqual(result, 1, result)

    def test_get_info_returns_proper_string(self):
        result = self.worker.get_info()
        expected_result = f'Boris has saved 0 money.'

        self.assertEqual(result, expected_result, result)


if __name__ == '__main__':
    unittest.main()
