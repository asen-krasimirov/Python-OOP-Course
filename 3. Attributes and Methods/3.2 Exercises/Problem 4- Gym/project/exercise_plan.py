

class ExercisePlan:
    trainer_id: int
    equipment_id: int
    duration: int

    current_id = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

        ExercisePlan.current_id += 1
        self.id = ExercisePlan.current_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    @staticmethod
    def get_next_id():
        return ExercisePlan.current_id + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
