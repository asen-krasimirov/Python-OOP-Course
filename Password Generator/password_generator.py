from random import randint


class PasswordGenerator:

    def __init__(self, file_name: str):
        self.__password_file = file_name
        self.__splitter = '<-username - password->'

        with open(self.__password_file) as file:
            self.lines = file.readlines()

    @staticmethod
    def __get_new_password(length):
        return list(chr(randint(33, 126)) for _ in range(length))

    def generate_password(self, key, length):
        password = self.__get_new_password(length)
        data = f"{key}{self.__splitter}{''.join(password)}"

        with open(self.__password_file, 'a') as file:
            file.write('\n' + data)

        with open(self.__password_file, "r") as file:
            self.lines = file.readlines()

    def delete_password(self, key):

        with open(self.__password_file, "w") as file:

            for line in self.lines:
                if line.strip("\n").split(self.__splitter)[0] != key:
                    file.write(line)
        with open(self.__password_file, "r") as file:
            self.lines = file.readlines()

    def find_password(self, key) -> 'str: password':

        for line in self.lines:
            data = line.strip("\n").split(self.__splitter)
            if data[0] == key:
                return data[1]

    def show_all_keys(self):

        keys = []

        for line in self.lines:
            data = line.strip("\n").split(self.__splitter)
            keys.append(f'-- {data[0]}')

        return '\n'.join(keys)

