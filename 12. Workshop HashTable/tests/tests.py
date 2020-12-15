from main.main import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable()

    def get_current_elements(self):
        return [
            item
            for elem in self.table.array
            if elem is not None
            for item in elem
        ]

    def test_hash_returns_proper_index(self):
        self.assertIs(int, type(self.table.hash('test')))

    def test_add_adds_key_value_pair_in_array(self):
        pair = 'test', 'test'
        pair2 = 'test2', 'test2'
        self.table.add(*pair)
        self.table.add(*pair2)

        present_elements = self.get_current_elements()
        self.assertIn(pair, present_elements)

    def test_add_overwrites_value_when_the_same_key_is_given(self):
        pair = 'test', 'test'
        pair2 = 'test', 'test1'
        self.table.add(*pair)
        self.table.add(*pair2)

        present_elements = self.get_current_elements()
        self.assertNotIn(pair, present_elements)
        self.assertIn(pair2, present_elements)

    def test_get_method_returns_value_by_key(self):
        pair = 'test', 'test123'
        self.table.add(*pair)

        result = self.table.get('test')
        self.assertEqual('test123', result)

    def test_table_gets_double_length_if_too_many_pairs_are_given(self):
        for i in range(5):
            self.table.add(f'key_test{i}', f'value_test{i}')

        self.assertEqual(8, self.table.capacity)

    def test_table_supports_item_assignment(self):
        self.table['key_test'] = 'value_test'
        present_elements = self.get_current_elements()
        self.assertIn(('key_test', 'value_test'), present_elements)

    def test_table_can_be_subscriptable(self):
        self.table.add(f'key_test', f'value_test')
        self.assertEqual('value_test', self.table['key_test'])

    def test_table_length_returns_number_of_all_keys_and_values(self):
        for i in range(5):
            self.table.add(f'key_test{i}', f'value_test{i}')

        self.assertEqual(10, len(self.table))


if __name__ == '__main__':
    unittest.main()
