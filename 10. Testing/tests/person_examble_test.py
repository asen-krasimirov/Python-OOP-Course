from solutions.person_example import Person
import unittest


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = Person('Firstname', 'Lastname', 16)

    def test_all_attributes_test(self):
        self.assertEqual(self.person.first_name, 'Firstname')
        self.assertEqual(self.person.last_name, 'Lastname')
        self.assertEqual(self.person.age, 16)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        self.assertTrue(result == self.person.first_name + ' ' + self.person.last_name)
        self.assertEqual(result, 'Firstname Lastname', self.person.get_full_name())

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = 'Firstname Lastname is 16 years old'
        self.assertEqual(result, expected_result, 'get_info method is wrong')


if __name__ == '__main__':
    unittest.main()
