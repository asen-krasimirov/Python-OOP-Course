

class Trainer:
    name: str

    current_id = 0

    def __init__(self, name: str):
        self.name = name

        Trainer.current_id += 1
        self.id = Trainer.current_id

    @staticmethod
    def get_next_id():
        return Trainer.current_id + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"