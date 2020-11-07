class AnimalBase:
    _needs = None

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return self._needs

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @classmethod
    def type(cls):
        return cls.__name__
