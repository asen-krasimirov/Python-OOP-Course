from typing import List, Dict
from .customer import Customer
from .dvd import DVD


class MovieWorld:
    name: str
    customers: List[Customer]
    dvds: List[DVD]

    customers_by_id: Dict['_id', Customer]
    dvds_by_id: Dict['_id', DVD]

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

        self.customers_by_id = {}
        self.dvds_by_id = {}

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) >= self.CUSTOMER_CAPACITY:
            return

        self.customers.append(customer)
        self.customers_by_id[customer.id] = customer

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) >= self.DVD_CAPACITY:
            return

        self.dvds.append(dvd)
        self.dvds_by_id[dvd.id] = dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.customers_by_id[customer_id]
        dvd = self.dvds_by_id[dvd_id]

        if customer.has_dvd(dvd):
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rent_dvd(dvd)
        dvd.switch_status()
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.customers_by_id[customer_id]
        dvd = self.dvds_by_id[dvd_id]

        if not customer.has_dvd(dvd):
            return f"{customer.name} does not have that DVD"

        # self.dvds.append(dvd)
        customer.return_dvd(dvd)
        dvd.switch_status()
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers = [customer.__repr__() for customer in self.customers]
        dvds = [dvd.__repr__() for dvd in self.dvds]

        return '\n'.join(customers + dvds)
