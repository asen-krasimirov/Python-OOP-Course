

class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"unsupported operand type")

        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"unsupported operand type")

        return Group(name=self.name, people=self.people+other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item]}'

    def __repr__(self):
        people = ', '.join([str(p) for p in self.people])
        return f"Group {self.name} with members {people}"


# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
# p5 = p0 + p1
# # print(p5)
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
# forth_group = third_group + first_group
#
# # print(len(first_group))
# # print(len(second_group))
# # print(len(third_group))
# # print()
# # print(first_group)
# # print(second_group)
# # print(third_group)
# # print(forth_group)
# # print()
# # print(first_group[0])
# # print(second_group[0])
# # print(third_group[0])
#
# # print()
# for person in third_group:
#     print(person)
