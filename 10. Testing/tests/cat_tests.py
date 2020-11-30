from solutions.cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Boris')

    def test_initialization(self):

        self.assertEqual(self.cat.name, 'Boris')

    def test_cat_size_increases_after_eating(self):
        start_result = self.cat.size
        self.cat.eat()
        end_result = self.cat.size
        final_result = end_result - start_result
        self.assertEqual(final_result, 1, final_result)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        result = self.cat.fed
        self.assertTrue(result)

    def test_cat_cannot_eat_when_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_sleep_when_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
