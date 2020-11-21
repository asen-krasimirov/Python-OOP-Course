

class vowels:
    string: str

    def __init__(self, string: str):
        self.string = string
        self.index = 0

    @staticmethod
    def is_vowel(char_: str):
        return char_.lower() in 'aeiouy'

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if self.is_vowel(char):
                return char
        raise StopIteration


if __name__ == '__main__':
    my_string = vowels('Abcedifuty0o')
    for character in my_string:
        print(character)
