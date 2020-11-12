from random import choice


class RandomList(list):

    def get_random_element(self):
        return self.pop(self.index(choice(self)))


test_list = RandomList(["test", "Hello World!", "YES!"])
print(test_list.get_random_element())
print(test_list.get_random_element())
print(test_list)
