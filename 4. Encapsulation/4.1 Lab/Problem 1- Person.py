

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


person = Person("George", 32)

person.name = "Stoqn"
person.age = 12

print(person.name)
print(person.age)
