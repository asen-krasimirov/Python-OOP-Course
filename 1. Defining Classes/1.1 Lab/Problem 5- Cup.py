

class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.size - self.quantity > 0:
            self.quantity += milliliters  # if self.quantity + milliliters > self.size else self.quantity-

            if self.quantity > self.size:
                self.quantity = self.size

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
