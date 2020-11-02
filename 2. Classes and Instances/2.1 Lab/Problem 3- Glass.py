

class Glass:
    capacity = 250
    content: int

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if (Glass.capacity - ml) >= 0:
            Glass.capacity -= ml
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        Glass.capacity = 250
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{Glass.capacity} ml left"
