

class Subscription:
    date: str
    customer_id: int
    trainer_id: int
    exercise_id: int

    current_id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

        Subscription.current_id += 1
        self.id = Subscription.current_id

    @staticmethod
    def get_next_id():
        return Subscription.current_id + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
