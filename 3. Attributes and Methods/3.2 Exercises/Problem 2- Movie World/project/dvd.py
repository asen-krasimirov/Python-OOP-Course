

class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    month_by_number = {
        # TODO: 1 cloud be 01
        '1': 'January', '02': 'February',
        '03': 'March', '04': 'April',
        '05': 'May', '06': 'June',
        '07': 'July', '08': 'August',
        '09': 'September', '10': 'October',
        '11': 'November', '12': 'December'
    }

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> 'DVD':
        day, month, year, *_ = date.split('.')
        month = cls.month_by_number[month]
        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"

    def switch_status(self):
        self.is_rented = not self.is_rented