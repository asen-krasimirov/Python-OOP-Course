

class vowels:
    string: str

    def __init__(self, string: str):
        self.string = string
        self.index = 0
        self.vowel_chars = ''
        self._get_vowels()

    @staticmethod
    def is_vowel(char_: str):
        if char_.lower() not in 'aeiouy':
            return False
        return True

    def _get_vowels(self):
        for char in self.string:
            if self.is_vowel(char):
                self.vowel_chars += char

    def __iter__(self):
        return self

    def __next__(self):
        cur_idx, self.index = self.index, self.index + 1
        if cur_idx >= len(self.vowel_chars):
            raise StopIteration

        if self.is_vowel(self.vowel_chars[cur_idx]):
            return self.vowel_chars[cur_idx]


if __name__ == '__main__':
    my_string = vowels('Abcedifuty0o')
    for character in my_string:
        print(character)
