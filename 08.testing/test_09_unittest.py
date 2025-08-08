# unittest is built into Python's standard library, making it ideal for
# environments with strict dependency management or limited internet access.

import math
import unittest


def func_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative values")
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial


def is_prime(num):
    if num < 2:  # 0, 1, and negative numbers are not prime
        return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True


class TestFactorial(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(func_factorial(5), 120)

    def test_zero(self):
        self.assertEqual(func_factorial(0), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            func_factorial(-1)


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(1))


# running the tests in CLI
# python -m unittest test_10_unittest.py
# python -m unittest test_10_unittest.py -v # for verbose
# python -m unittest test_10_unittest.py -v -k TestFactorial # for running specific test with fail fast
