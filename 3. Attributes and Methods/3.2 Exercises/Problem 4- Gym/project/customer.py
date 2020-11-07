

class Customer:
    name: str
    address: str
    email: str

    current_id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

        Customer.current_id += 1
        self.id = Customer.current_id

    @staticmethod
    def get_next_id():
        return Customer.current_id + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
