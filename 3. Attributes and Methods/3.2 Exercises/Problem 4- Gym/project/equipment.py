

class Equipment:
    name: str

    current_id = 0

    def __init__(self, name: str):
        self.name = name

        Equipment.current_id += 1
        self.id = Equipment.current_id

    @staticmethod
    def get_next_id():
        return Equipment.current_id + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
