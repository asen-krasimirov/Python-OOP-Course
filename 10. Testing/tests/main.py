# testing unittest
import unittest


class DummyTester(unittest.TestCase):
    def setUp(self):
        self.dummy_class = DummyTester()  # delete before runing

    def returns_dummy_age_plus_one(self):
        self.assertNotEqual(self.dummy_class, 'Sixty Four')


if __name__ == '__main__':
    unittest.main()
