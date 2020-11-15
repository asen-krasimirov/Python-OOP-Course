from project.technology.technology import Technology
from project.capacity_mixin import CapacityMixin


class Laptop(Technology, CapacityMixin):

    def install_software(self, software: str, software_memory: float):
        result = super().get_capacity(self._memory, self._memory_taken + software_memory)
        if isinstance(result, str):
            result = f"You don't have enough space for {software}!"
        
        self._memory_taken += software_memory
        return result
