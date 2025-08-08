# try/except/finally: Handle specific exceptions, with finally for cleanup
# Custom errors: Inherit from built-in exceptions for domain-specific validation
# Python: Use class hierarchies (BonusError < SalaryError < ValueError)
# TypeScript: Simpler errors or error codes are more common than deep hierarchies


def invert_at_index(x, ind):
    try:
        return 1 / x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Done")


a_list = [5, 6, 0, 7]

# Works okay
print(invert_at_index(a_list, 1))
# 0.16666666666666666

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))
# Cannot divide by zero!
# None

# Potential IndexError
print(invert_at_index(a_list, 5))
# Index out of range!
# None


###############

# Custom error classes can make your code more expressive and maintainable


class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError
        self.salary = salary

    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus is too high")
        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")
        self.salary += amount


# TypeScript/JavaScript, custom error classes aren't as commonly used as in Python.
# Python: More formal error hierarchies
# TypeScript/JavaScript: Often use error codes or simple error messages

# 	class SalaryError extends Error {
#     constructor(message: string = 'Invalid salary') {
#         super(message);
#         this.name = 'SalaryError';
#     }
# }

# class BonusError extends SalaryError {
#     constructor(message: string = 'Invalid bonus') {
#         super(message);
#         this.name = 'BonusError';
#     }
# }

# class Employee {
#     static readonly MIN_SALARY = 30000;
#     static readonly MAX_BONUS = 5000;

#     public salary: number;

#     constructor(public name: string, salary: number = 30000) {
#         if (salary < Employee.MIN_SALARY) {
#             throw new SalaryError('Salary is below minimum');
#         }
#         this.salary = salary;
#     }

#     giveBonus(amount: number): void {
#         if (amount > Employee.MAX_BONUS) {
#             throw new BonusError('The bonus is too high');
#         }
#         if (this.salary + amount < Employee.MIN_SALARY) {
#             throw new SalaryError('The salary after bonus is too low!');
#         }
#         this.salary += amount;
#     }
# }
