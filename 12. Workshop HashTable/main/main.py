from typing import List, Union


class HashTable:
    array: List[Union[list, None]]

    def __init__(self, capacity=4):
        self.array = [None] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, key: str):
        index = self.hash(key)

        is_key_present = self.__is_key_already_present(key, index)
        if is_key_present is not False:
            sub_index = is_key_present
            return self.array[index][sub_index][-1]

    def add(self, key: str, value):
        index = self.hash(key)
        if self.array[index] is None:
            self.array[index] = []

        is_key_present = self.__is_key_already_present(key, index)
        if is_key_present is not False:
            sub_index = is_key_present
            self.__change_key(key, value, index, sub_index)
            return

        self.array[index].append((key, value))

        self.length += 1
        if self.length >= self.capacity:
            self.__double_array_length()

    def hash(self, key: str):
        return hash(key) % self.capacity

    def __is_key_already_present(self, key, index):
        for i in range(len(self.array[index])):
            if key in self.array[index][i]:
                return i
        return False

    def __change_key(self, key, value, index, i):
        self.array[index][i] = key, value

    def __double_array_length(self):
        new_table = HashTable(self.capacity*2)
        for i in range(self.length):
            if self.array[i] is not None:
                for pair in self.array[i]:
                    new_table.add(*pair)

        self.array = new_table.array
        self.capacity = new_table.capacity

    def __len__(self):
        return self.length * 2

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.add(key, value)
