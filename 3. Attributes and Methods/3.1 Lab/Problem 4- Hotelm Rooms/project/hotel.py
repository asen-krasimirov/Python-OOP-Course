from .room import Room


class Hotel:
    name: str
    rooms: list
    guest: int

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> 'Hotel':
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                if isinstance(room.take_room(people), str):
                    break
                self.guests += people
                return

    def free_room(self, room_number: int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()
                return

    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        # hotel_information = [
        #     f"Hotel {self.name} has {self.guests} total guests",
        #     f"Free rooms: {', '.join(free_rooms)}",
        #     f"Taken rooms: {', '.join(taken_rooms)}"
        # ]

        # print('\n'.join(hotel_information))

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")

