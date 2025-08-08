# Properties let you expose “public” attributes while keeping a private backing field (e.g. _balance),
## so you can enforce checks (like non-negative values) on get/set without changing client code.

# Read-Only vs. Writable: Simply define @property for a read-only attribute;
## add a @<prop>.setter decorated method to allow controlled mutation.

# Transparent API: Consumers access cust.balance just like a regular attribute,
## hiding method calls behind simple attribute syntax—cleaner than explicit getters/setters.


class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance")
        self._balance = new_bal

    # by convention, the name of the property should be the same as the private attribute without the _
    @property
    def balance(self):
        return self._balance

    # if it is not a readonly property, we can define a setter
    @balance.setter
    def balance(self, new_bal):
        if new_bal < 0:
            raise ValueError("Invalid balance")
        self._balance = new_bal


cust = Customer("Belinda Lutz", 2000)
cust.balance = 3000
print(cust.balance)

# cust.balance = -1000 # ValueError: Invalid balance


# @dataclass version
# When to Use @dataclass:

# Data Containers: For classes primarily holding data
# Type Hints: When using type hints (common in modern Python)
# Reduced Boilerplate: For classes with many attributes
# Modern Codebases: In new projects using Python 3.7+

# When to Avoid:
# Simple Classes: For classes with <3 attributes
# Complex Initialization: When you need custom init logic
# Performance-Critical Code: Where __slots__ is needed
# Python <3.7: If you need to support older versions


# @dataclass
# class Customer:
#     name: str
#     _balance: float = field(default=0, repr=False)  # Hide _balance from repr

#     def __post_init__(self):
#         if self._balance < 0:
#             raise ValueError('Invalid balance')


#######

# TS version

# class Customer {
#   constructor(
#     public name: string,
#     private _balance: number
#   ) {
#     if (_balance < 0) throw new Error('Invalid balance');
#   }

#   get balance() {
#     return this._balance;
#   }

#   set balance(value: number) {
#     if (value < 0) throw new Error('Invalid balance');
#     this._balance = value;
#   }
# }


#######
# Improved LoggedDF from 01_1_basic_class.py

############

from datetime import datetime

import pandas as pd


class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        return pd.DataFrame.to_csv(temp, *args, **kwargs)

    @property
    def created_at(self):
        return self._created_at


####### another example


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return f"${round(self._balance, 2)}"

    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self._balance = new_balance

    @balance.deleter
    def balance(self):
        print("Deleting the 'balance' attribute")
        del self._balance


checking_account = BankAccount(100)
print(checking_account.balance)

checking_account.balance = 150
print(checking_account.balance)

del checking_account.balance

########

# dataclass version
# Dataclasses auto-generate __init__, __repr__, and comparison methods,
# removing boilerplate for simple data containers.
# For controlled access or complex logic (getters/setters), stick with manual @property definitions.


from dataclasses import dataclass


@dataclass
class BankAccount:
    balance: float


checking_account = BankAccount(100)
print(checking_account.balance)

checking_account.balance = 150
print(checking_account.balance)
