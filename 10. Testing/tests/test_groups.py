from solutions.groups import Person, Group
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.person_one = Person('Name One', 'Surname One')
        self.person_two = Person('Name Two', 'Surname Two')


class TestPerson(TestMain):

    def test_init_method_creates_proper_attributes(self):
        name, surname = self.person_one.name, self.person_one.surname

        self.assertEqual(name, 'Name One')
        self.assertEqual(surname, 'Surname One')

    def test_magic_method_add_creates_new_person_with_name_of_first_person_and_surname_of_second(self):
        result = self.person_one + self.person_two
        expected_result = 'Name One Surname Two'

        self.assertEqual(expected_result, str(result), str(result))

    def test_magic_method_represent_returns_name_and_surname(self):
        self.assertEqual('Name One Surname One', str(self.person_one))


class TestGroup(TestMain):
    def setUp(self):
        super().setUp()
        self.group_one = Group('Group Name One', [self.person_one, self.person_two])

    def test_init_method_creates_proper_attributes(self):
        name, people = self.group_one.name, self.group_one.people

        self.assertEqual(name, 'Group Name One')
        self.assertEqual(people, [self.person_one, self.person_two])

    def test_magic_method_add_creates_new_group_with_people_from_first_and_second(self):
        new_group = self.group_one + self.group_one
        self.assertEqual(
            [self.person_one, self.person_two] * 2,
            new_group.people
        )

    def test_magic_method_len_returns_the_len_of_people_attr_of_group(self):
        self.assertEqual(2, len(self.group_one))

    def test_magic_method_repr(self):
        result_information = str(self.group_one)
        expected_result = 'Group Group Name One with members Name One Surname One, Name Two Surname Two'
        self.assertEqual(expected_result, result_information, result_information)

    def test_getting_items_from_people_attr_vie_indexing_on_group_object(self):
        item = self.group_one[0]
        expected_result = f'Person 0: {self.person_one}'
        self.assertEqual(expected_result, item, item)

    def test_iterating_though_group_object(self):
        expected_result = "Person 0: Name One Surname One\nPerson 1: Name Two Surname Two"

        # result = []
        # for name in self.group_one:
        #     result.append(name)
        #
        # result = '\n'.join(result)

        def local_name_generator():
            for name in self.group_one:
                yield name

        result = '\n'.join(
            local_name_generator()
        )

        self.assertEqual(expected_result, result, result)


if __name__ == '__main__':
    unittest.main()
