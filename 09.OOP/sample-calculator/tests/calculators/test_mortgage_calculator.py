"""Tests for the MortgageCalculator class."""

from decimal import Decimal

import pytest

# Import the module under test
from calculators.mortgage_calculator import MortgageCalculator

# Test data: (loan_amount, annual_interest_rate, years, expected_monthly_payment)
MORTGAGE_TEST_CASES = [
    # Basic test case - standard 30-year mortgage
    (300000, 0.06, 30, 1798.65),
    # 15-year mortgage with higher rate
    (200000, 0.075, 15, 1854.02),
    # 10-year mortgage with lower rate
    (150000, 0.045, 10, 1554.58),
    # Edge case: 1-year mortgage
    (100000, 0.05, 1, 8560.74),
    # Edge case: very high interest rate (100%)
    (10000, 1.0, 1, 1349.96),
]


@pytest.mark.parametrize("loan_amount,annual_rate,years,expected", MORTGAGE_TEST_CASES)
def test_calculate_monthly_payment(
    loan_amount: float, annual_rate: float, years: int, expected: float
):
    """Test the monthly payment calculation with various scenarios."""
    # Arrange
    calculator = MortgageCalculator(loan_amount, annual_rate, years)

    # Act
    result = calculator.monthly_payment

    # Assert
    assert isinstance(result, float)
    assert result > 0
    assert abs(result - expected) < 0.1  # Allow small floating point differences


def test_mortgage_calculator_initialization():
    """Test that MortgageCalculator initializes with correct attributes."""
    # Arrange & Act
    calculator = MortgageCalculator(300000, 0.06, 30)

    # Assert
    assert calculator.loan_amount == 300000
    assert calculator.monthly_interest_rate == pytest.approx(0.06 / 12)
    assert calculator.months == 30 * 12
    assert hasattr(calculator, "monthly_payment")
    assert isinstance(calculator.monthly_payment, float)


def test_monthly_interest_calculation():
    """Test that monthly interest is calculated correctly."""
    # Arrange
    calculator = MortgageCalculator(300000, 0.06, 30)

    # Act
    monthly_rate = calculator.monthly_interest(0.06)  # 6% annual

    # Assert
    assert monthly_rate == pytest.approx(0.06 / 12)


def test_months_from_years():
    """Test that years are correctly converted to months."""
    # Arrange
    calculator = MortgageCalculator(300000, 0.06, 30)

    # Act & Assert
    assert calculator.month_from_years(1) == 12
    assert calculator.month_from_years(5) == 60
    assert calculator.month_from_years(0.5) == 6


def test_zero_interest_edge_case():
    """Test the edge case where interest rate is 0%."""
    # Arrange & Act
    calculator = MortgageCalculator(120000, 0.0, 10)  # $120,000 over 10 years at 0%

    # Assert - should be exactly 1/120th of the loan amount per month
    expected_payment = 120000 / (10 * 12)
    assert calculator.monthly_payment == pytest.approx(expected_payment)


def test_negative_values_error():
    """Test that negative values raise appropriate errors."""
    # Test negative loan amount
    with pytest.raises(ValueError):
        MortgageCalculator(-100000, 0.05, 30)

    # Test negative interest rate
    with pytest.raises(ValueError):
        MortgageCalculator(100000, -0.05, 30)

    # Test negative years
    with pytest.raises(ValueError):
        MortgageCalculator(100000, 0.05, -30)


def test_zero_loan_amount():
    """Test that a zero loan amount results in zero monthly payment."""
    # Arrange & Act
    calculator = MortgageCalculator(0, 0.05, 30)

    # Assert
    assert calculator.monthly_payment == 0.0


# Test with decimal.Decimal for financial precision
def test_decimal_precision():
    """Test that calculations maintain sufficient precision."""
    # Use exact decimal representation to avoid floating point errors
    loan_amount = Decimal("300000")
    annual_rate = Decimal("0.06")
    monthly_rate = annual_rate / Decimal("12")
    months = Decimal("360")

    # Exact calculation using decimal
    numerator = monthly_rate * ((1 + monthly_rate) ** months)
    denominator = (1 + monthly_rate) ** months - 1
    expected_payment = float(loan_amount * (numerator / denominator))

    # Test with float inputs
    calculator = MortgageCalculator(float(loan_amount), float(annual_rate), 30)

    # Allow for small floating point differences
    assert abs(calculator.monthly_payment - expected_payment) < 0.01
