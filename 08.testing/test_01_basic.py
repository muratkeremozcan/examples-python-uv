# need to add a context for an exception test: with pytest.raises(ValueError):
# run a single file:  poetry run pytest 08.testing/test_01_basic.py
# run a single test:  poetry run pytest -k "test_zero", poetry run pytest -k "numbers"
# @pytest.mark.skip # you can use test markers
# @pytest.mark.skipif('2 * 2 = 5') # skip with a condition
# @pytest.mark.xfail # expect to fail
from datetime import datetime

import pytest


def multiple_of_two(num):
    if num == 0:
        raise (ValueError)
    return num % 2 == 0


def test_numbers():
    assert multiple_of_two(2) == True
    assert multiple_of_two(3) == False


def test_zero():
    # need to add a context for an exception test
    with pytest.raises(ValueError):
        multiple_of_two(0)


@pytest.mark.skip(reason="skipping this test")
def test_fails():
    # Write any assert test that will fail
    assert multiple_of_two(5) == True


####

day_of_week = datetime.now().isoweekday()


def get_unique_values(lst):
    return list(set(lst))


@pytest.mark.skipif("day_of_week == 6")
def test_function():
    # Complete the assertion tests here
    assert get_unique_values([1, 2, 3]) == [1, 2, 3]
    assert get_unique_values([1, 2, 3, 1]) == [1, 2, 3]
