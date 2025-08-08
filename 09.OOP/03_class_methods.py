# Class methods are bound to the class, not the instance:
## they receive the class (cls) as their first argument instead of the instance (self).
# Alternative constructors: Often used to create factory methods that return class instance
# They can be used to enforce restrictions on instance creation (singleton - db connections or config come to mind)


class Person:
    CURRENT_YEAR = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = Person.CURRENT_YEAR - birth_year
        return cls(name, age)


p1 = Person("John", 30)
p2 = Person.from_birth_year("John", 1990)

print(p1.age)
print(p2.age)

print("-----------")
# class Person {
#     static CURRENT_YEAR = 2025;

#     constructor(public name: string, public age: number) {}

#     // Static factory method (TypeScript's equivalent to @classmethod)
#     static fromBirthYear(name: string, birthYear: number): Person {
#         const age = Person.CURRENT_YEAR - birthYear;
#         return new Person(name, age);
#     }
# }

# const p1 = new Person("John", 30);
# const p2 = Person.fromBirthYear("John", 1990);

from datetime import datetime


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # year, month, day = map(int, datestr.split('-')) # better way
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, datetime):
        year, month, day = datetime.year, datetime.month, datetime.day
        return cls(year, month, day)


xmas = BetterDate.from_str("2025-12-25")
print(xmas.year, xmas.month, xmas.day)

xmas2 = BetterDate.from_datetime(datetime(2025, 12, 25))
print(xmas2.year, xmas2.month, xmas2.day)

# class BetterDate {
#     constructor(
#         public year: number,
#         public month: number,
#         public day: number
#     ) {}

#     // Static factory method using array destructuring
#     static fromStr(dateStr: string): BetterDate {
#         const [year, month, day] = dateStr.split('-').map(Number);
#         return new BetterDate(year, month, day);
#     }

#     static fromDatetime(date: Date): BetterDate {
#         const year = date.getFullYear();
#         const month = date.getMonth() + 1;
#         const day = date.getDate();
#         return new BetterDate(year, month, day);
#     }
# }

# // Usage
# const xmas = BetterDate.fromStr("2025-12-25");
# console.log(xmas.year, xmas.month, xmas.day);

# const xmas2 = BetterDate.fromDatetime(new Date(2025, 11, 24));
# console.log(xmas2.year, xmas2.month, xmas2.day);

## realistic example


class DatabaseConnection:
    _instance = None

    def __init__(self):
        if DatabaseConnection._instance is not None:
            raise Exception("This class is a singleton - use get_instance()")
        # Initialize connection
        self.connection = "Connected"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()  # Creates the one and only instance
        return cls._instance


# Usage
db1 = DatabaseConnection.get_instance()  # Creates new instance
db2 = DatabaseConnection.get_instance()  # Returns same instance as db1
# This would raise an exception because we're trying to create a second instance
# db3 = DatabaseConnection()  # Raises Exception
