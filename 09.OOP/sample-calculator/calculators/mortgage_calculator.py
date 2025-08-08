from .financial_calculator import FinancialCalculator


class MortgageCalculator(FinancialCalculator):
    """
    A class for calculating mortgage-related values.
    Inherits from FinancialCalculator to utilize financial calculation methods.

    Attributes
    ----------
    loan_amount : float
        The total loan amount in dollars (must be non-negative)
    monthly_interest_rate : float
        The monthly interest rate (annual rate / 12, must be non-negative)
    months : int
        The loan term in months (years * 12, must be positive)
    """

    def __init__(self, loan_amount: float, annual_interest_rate: float, years: int):
        # Validate inputs
        if loan_amount < 0:
            raise ValueError("Loan amount cannot be negative")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative")
        if years <= 0:
            raise ValueError("Loan term must be positive")

        super().__init__
        self.loan_amount: float = loan_amount
        self.months: int = self.month_from_years(years)

        # Handle zero interest rate case
        if annual_interest_rate == 0:
            self.monthly_interest_rate = 0.0
            self.monthly_payment: float = self.loan_amount / self.months
        else:
            self.monthly_interest_rate: float = self.monthly_interest(
                annual_interest_rate
            )
            self.monthly_payment: float = self.calculate_monthly_payment()

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly mortgage payment.

        Returns:
            float: The monthly payment amount
        """
        if self.monthly_interest_rate == 0:
            return self.loan_amount / self.months

        # Standard mortgage payment formula:
        # P = L[c(1 + c)^n]/[(1 + c)^n - 1]
        # Where:
        # P = monthly payment
        # L = loan amount
        # c = monthly interest rate
        # n = number of months

        # Calculate (1 + c)^n
        rate_factor = (1 + self.monthly_interest_rate) ** self.months

        # Calculate the payment
        if rate_factor == 1:  # This handles the case where monthly_interest_rate is 0
            return self.loan_amount / self.months

        monthly_payment = (
            self.loan_amount
            * (self.monthly_interest_rate * rate_factor)
            / (rate_factor - 1)
        )
        return round(monthly_payment, 2)


# use help(...object...) to get documentation
# use dir(...object...) to get list of attributes and methods
# print(help(FinancialCalculator))
# print(dir(FinancialCalculator))


mortgage_calculator = MortgageCalculator(300000, 0.059, 10)
print(
    f"Your monthly mortgage payment is ${round(mortgage_calculator.monthly_payment, 2)}."
)
