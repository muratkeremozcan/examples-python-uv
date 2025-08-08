# private attributes and methods start with _ by convention


class BetterDate:
    _MAX_DAYS = 31
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod  # like static method in other languages
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    def _is_valid(self):
        return self.month <= BetterDate._MAX_MONTHS and self.day <= BetterDate._MAX_DAYS


bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())
