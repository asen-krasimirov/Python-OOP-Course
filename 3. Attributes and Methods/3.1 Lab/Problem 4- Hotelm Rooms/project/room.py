from typing import Union


class Room:
    number: int
    capacity: int
    guests: int
    is_taken: bool

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Union[str, None]:
        if self.is_taken or people > (self.capacity - self.guests):
            return f"Room number {self.number} cannot be taken"

        self.guests += people
        self.is_taken = True  # TODO: potential error- when make is_taken=True

    def free_room(self) -> Union[str, None]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = not self.is_taken
        self.guests = 0  # TODO: potential error- do guest need to be 0
