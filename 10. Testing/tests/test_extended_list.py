from solutions.List.extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 4, 5)
        # self.default_integer_list_state = [1, 2, 3, 4, 5]

    def test_constructor_setting_right_arguments(self):
        result = self.integer_list.get_data()
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_add_operation_adds_elem_and_returns_the_list(self):
        self.assertEqual(self.integer_list.add(123), [1, 2, 3, 4, 5, 123])
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5, 123])

    def test_add_operation_raises_value_error_when_adding_non_integer(self):
        with self.assertRaises(ValueError):
            self.integer_list.add('test')

    def test_remove_index_operation_removes_elem_by_index_and_returns_it(self):
        self.assertEqual(self.integer_list.remove_index(0), 1)
        self.assertEqual(self.integer_list.get_data(), [2, 3, 4, 5])

    def test_remove_operation_raises_index_error_when_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(10)

    def test_init_method_should_only_take_integers_and_store_them(self):
        new_integer_list = IntegerList(1, 2, 3, 4, 5, 'test')
        self.assertEqual(new_integer_list.get_data(), [1, 2, 3, 4, 5])

    def test_get_method_returns_elem_by_index(self):
        elem = self.integer_list.get(0)
        self.assertEqual(elem, 1)

    def test_get_method_raises_index_error_when_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.integer_list.get(10)

    def test_insert_method_correctly_inserts_elem_in_the_integer_list(self):
        self.integer_list.insert(0, -1)
        self.assertEqual(self.integer_list.get_data(), [-1, 1, 2, 3, 4, 5])

    def test_insert_method_raises_index_error_when_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.integer_list.insert(10, -1)

    def test_insert_method_raises_value_error_when_elem_not_int(self):
        with self.assertRaises(ValueError):
            self.integer_list.insert(0, '-1')

    def test_get_biggest_method_returns_the_biggest_value(self):
        value = self.integer_list.get_biggest()
        self.assertEqual(5, value, value)

    def test_get_index_method_returns_the_index_on_that_value(self):
        index = self.integer_list.get_index(1)
        self.assertEqual(index, 0)


if __name__ == '__main__':
    unittest.main()
