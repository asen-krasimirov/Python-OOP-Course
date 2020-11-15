from project.vehicle.vehicle import Vehicle
from project.capacity_mixin import CapacityMixin


class Bus(Vehicle, CapacityMixin):
    __ticket_price: float
    __tickets_sold: int

    def __init__(self, available_seats: int, ticket_price: float):
        super().__init__(available_seats)
        self.__ticket_price = ticket_price
        self.__tickets_sold = 0

    def get_ticket(self, tickets_count: int):
        result = super().get_capacity(self._available_seats, self.__tickets_sold + tickets_count)
        if isinstance(result, str):
            return result

        self.__tickets_sold += tickets_count

    def get_total_profit(self):
        return self.__tickets_sold * self.__ticket_price
