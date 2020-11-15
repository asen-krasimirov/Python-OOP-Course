from project.vehicle.vehicle import Vehicle
from project.capacity_mixin import CapacityMixin


class Plane(Vehicle, CapacityMixin):
    __seats_available: dict

    def __init__(self, available_seats: int, rows: int, seats_per_row: int):
        super().__init__(available_seats)
        self.__seats_available = {
            row: seats_per_row
            for row in range(1, rows)  # Note: might the rows start from 0
        }  # Note: the dict might be empty by initialization

    def buy_tickets(self, row_number: int, tickets_count: int):
        if row_number not in self.__seats_available:
            return f"There is no row {row_number} in the plane!"

        result = super().get_capacity(self.__seats_available[row_number], tickets_count)
        if isinstance(result, str):
            return f"Not enough tickets on row {row_number}!"
        
        self.__seats_available[row_number] -= tickets_count
        return tickets_count
