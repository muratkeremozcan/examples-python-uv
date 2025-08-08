# Custom comparison methods (__eq__, __lt__, etc.) enable object comparison in Python
# Always check types and return NotImplemented for unsupported comparisons
# __str__ for user-friendly output, __repr__ for debugging/REPL


class BankAccount:
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number
        self._dynamic_attributes = {}  # Dictionary to store dynamic attributes

    def __getattr__(self, name):
        """
        Called when an attribute lookup fails.
        This allows for dynamic attribute access and lazy loading.
        """
        if name in self._dynamic_attributes:
            return self._dynamic_attributes[name]

        # For attributes that start with 'get_', you could implement dynamic getters
        if name.startswith("get_") and name[4:] in self._dynamic_attributes:
            return lambda: self._dynamic_attributes[name[4:]]

        # Raise AttributeError for undefined attributes
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __setattr__(self, name, value):
        """
        Intercept all attribute assignments.
        This allows for validation, computed properties, or read-only attributes.
        """
        # Allow setting of _dynamic_attributes in __init__
        if name == "_dynamic_attributes":
            super().__setattr__(name, value)
            return

        # Allow direct assignment to existing attributes. __dict__ is an instance variable storage
        if name in self.__dict__ or hasattr(self.__class__, name):
            super().__setattr__(name, value)
        else:
            # For new attributes, store them in _dynamic_attributes
            self._dynamic_attributes[name] = value

    def withdraw(self, amount):
        self.balance -= amount

    @classmethod
    def _is_bank_account(cls, obj) -> bool:
        # Check that verifies if other is an instance of the same class as self
        return isinstance(obj, cls)

    # Overriding the __eq__ method
    # return True if the number attribute is the same and the type() of both objects passed to it is the same.
    def __eq__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return (self.number == other.number) and (self.balance == other.balance)

    def __ne__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return self != other

    def __lt__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return self.balance < other.balance

    def __le__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return self.balance <= other.balance

    def __gt__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return self.balance > other.balance

    def __ge__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return self.balance >= other.balance

    def __add__(self, other):
        if not self._is_bank_account(other):
            return NotImplemented
        return BankAccount(self.number, self.balance + other.balance)

    # Provides a complete, unambiguous string representation of an object
    def __repr__(self):
        return f"BankAccount(number={self.number}, balance={self.balance})"

    # Provides a human-readable string representation of an object (informal, for end-users)
    def __str__(self):
        return f"BankAccount(number={self.number}, balance={self.balance})"


acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
print(acct1 + acct2)


class Phone:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))


pn = Phone(873555333)
acct4 = BankAccount(873555333)
print(pn == acct4)

# Example usage of __getattr__ and __setattr__
print("\n--- Dynamic Attributes Example ---")
account = BankAccount(999, 5000)

# 1. Normal attribute access (goes through __dict__)
print(f"Initial balance: {account.balance}")

# 2. Dynamic attribute assignment (goes through __setattr__)
account.owner = "John Doe"  # This will be stored in _dynamic_attributes
account.email = "john@example.com"

# 3. Dynamic attribute access (goes through __getattr__)
print(f"Owner: {account.owner}")
print(f"Email: {account.email}")

# 4. Try to access non-existent attribute
try:
    print(account.non_existent)
except AttributeError as e:
    print(f"Error: {e}")

# 5. View the internal storage
print(f"\nInternal state:")
print(f"__dict__: {account.__dict__}")
print(f"_dynamic_attributes: {account._dynamic_attributes}")

# 6. Type safety note (this is where TypeScript would help!)
# In TypeScript, these dynamic attributes would be caught at compile time
# In Python, they're only caught at runtime
account.balance = (
    "not a number"  # This is allowed in Python but would be a type error in TypeScript
)
print(
    f"\nAfter bad assignment - balance: {account.balance} (type: {type(account.balance)})"
)

# 7. Making attributes read-only
del BankAccount.__setattr__  # Remove our custom __setattr__


class ReadOnlyAccount(BankAccount):
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError(f"Can't modify attribute '{name}' after creation")
        super().__setattr__(name, value)


print("\n--- Read-Only Example ---")
read_only = ReadOnlyAccount(100, 1000)
read_only.balance = 2000  # This will raise an error

# This demonstrates why you might want these methods in Python, even though
# they're not common in TypeScript. Python's dynamic nature allows for powerful
# metaprogramming features that can be very useful in certain scenarios, but
# should be used judiciously to maintain code clarity and type safety.

# class BankAccount {
#   constructor(
#     public readonly number: number,
#     private _balance: number = 0
#   ) {}

#   withdraw = (amount: number): void => { this._balance -= amount; }
#   get balance(): number { return this._balance; }

#   private static isBankAccount = (obj: any): obj is BankAccount =>
#     obj instanceof BankAccount;

#   equals = (other: unknown): boolean =>
#     BankAccount.isBankAccount(other) &&
#     this.number === other.number &&
#     this._balance === other._balance;

#   notEquals = (other: unknown): boolean => !this.equals(other);
#   lessThan = (other: BankAccount): boolean => this._balance < other._balance;
#   lessThanOrEqual = (other: BankAccount): boolean => this._balance <= other._balance;
#   greaterThan = (other: BankAccount): boolean => this._balance > other._balance;
#   greaterThanOrEqual = (other: BankAccount): boolean => this._balance >= other._balance;
#   toString = (): string => [BankAccount(number=${this.number}, balance=${this._balance})];
# }

# // Example usage
# const [acct1, acct2, acct3] = [
#   new BankAccount(123, 1000),
#   new BankAccount(123, 1000),
#   new BankAccount(456, 2000)
# ];

# console.log(acct1.equals(acct2));  // true
# console.log(acct1.notEquals(acct3)); // true
# console.log(acct1.lessThan(acct3)); // true

# // Phone class example
# class Phone {
#   constructor(public number: number) {}
#   equals = (other: unknown): boolean =>
#     other instanceof Phone && this.number === other.number;
# }

# console.log(acct1.equals(new Phone(123)));  // false
