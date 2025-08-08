# Dynamic Attribute Control: getattr and setattr allow you to intercept and manage attribute access and modification dynamically.
# they help enforce rules (like allowed attributes) and add validation, preventing invalid states or attributes.
# While powerful, they can make code harder to understand and maintain. (Blasphemy for the FP'er)


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number

    def __getattr__(self, name):
        print(
            f"{name} is not defined in BankAccount object.\nPlease define this attribute if needed."
        )

    def __setattr__(self, name, value):
        if name in ["account_number", "balance"]:
            print(f"{name} is an allowed attribute")
            self.__dict__[name] = value
        else:
            print(f"Invalid Argument: {name}")


# Create a BankAccount object, reference routing_number
checking_account = BankAccount("123456")
checking_account.routing_number
checking_account.account_number

savings_account = BankAccount("12345678")
savings_account.balance = 100
savings_account.beneficiary = "Anna Wu"
