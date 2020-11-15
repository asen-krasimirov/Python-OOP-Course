from project.technology.technology import Technology
from project.capacity_mixin import CapacityMixin


class SmartPhone(Technology, CapacityMixin):

    def install_apps(self, app: str, app_memory: float):
        result = super().get_capacity(self._memory, self._memory_taken + app_memory)
        if isinstance(result, str):
            result = f"You don't have enough space for {app}!"

        self._memory_taken += app_memory
        return result
