from .basic_calculator import BasicCalculator


class FinancialCalculator(BasicCalculator):
    def monthly_interest(self, annual_interest_rate: float) -> float:
        return self.divide(annual_interest_rate, 12)

    def month_from_years(self, years: int) -> int:
        return self.multiply(years, 12)
