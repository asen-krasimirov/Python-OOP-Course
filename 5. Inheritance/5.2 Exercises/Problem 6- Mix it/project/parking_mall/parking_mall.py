from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    _max_lots: int = None
    _parking_lots: int

    def __init__(self, parking_lots: int):
        self._parking_lots = parking_lots

    def check_availability(self):
        # Note: possible off by one mistake
        result = super().get_capacity(self._max_lots, self._parking_lots)
        if isinstance(result, str) or result == 0:
            return "There are no more parking lots!"

        return f"Parking lots available: {result}"
