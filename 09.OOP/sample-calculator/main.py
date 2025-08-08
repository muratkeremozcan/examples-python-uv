from calculators.financial_calculator import FinancialCalculator

financial_calculator = FinancialCalculator()
monthly_interest = financial_calculator.monthly_interest_rate(0.06)
print(monthly_interest)
