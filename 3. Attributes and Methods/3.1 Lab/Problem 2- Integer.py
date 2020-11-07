from typing import Union


class Integer:
    value: int

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float) -> Union[str, 'Integer']:
        if not isinstance(value, float):
            return "value is not a float"
        new_value = int(value)
        return cls(new_value)

    @classmethod
    def from_roman(cls, value: str) -> 'Integer':
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        index = 0
        new_value = 0
        while index < len(value):
            if index + 1 < len(value) and value[index:index + 2] in roman:
                new_value += roman[value[index:index + 2]]
                index += 2
            else:
                # print(i)
                new_value += roman[value[index]]
                index += 1
        return cls(new_value)

    @classmethod
    def from_string(cls, value: str) -> Union[str, 'Integer']:
        if not isinstance(value, str):
            return "wrong type"

        new_value = int(value)
        return cls(new_value)

    def add(self, integer: 'Integer') -> Union[str, int, float]:
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
