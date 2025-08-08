import pytest

# The autouse=True parameter makes this fixture run automatically for every test in this module,
# without needing to explicitly request it in the test function parameters.
#
# Setup with autouse fixtures:
# 1. They run automatically for every test in their scope (function, class, module, or session)
# 2. Useful for setup/teardown that applies to multiple tests

# We use `yield` to separate setup from teardown:
# - Code before `yield` runs before the test (setup)
# - Code after `yield` runs after the test (teardown)

# Jest/Jasmine        | # Pytest equivalent
# -------------------|--------------------
# beforeAll          | @pytest.fixture(scope="module", autouse=True)
# afterAll           | @pytest.fixture(scope="module", autouse=True) with yield
# beforeEach         | @pytest.fixture(autouse=True)
# afterEach          | Code after yield in an autouse fixture


@pytest.fixture(autouse=True)
def prepare_data():
    # Setup: Runs before each test
    data = [i for i in range(10)]

    # The test runs at this point
    yield data

    # Teardown: Runs after each test
    # Use yield if you need teardown code that runs after the test
    # Use return for simpler cases without teardown
    # in Pytest you never need teardown, it handles it (but these examples show it for some reason)
    # data.clear()


def test_elements(prepare_data):
    # prepare_data is automatically provided by the autouse fixture
    assert 9 in prepare_data
    assert 10 not in prepare_data


# Pytest is designed to handle cleanup automatically, just like Jest. The only times you'd need to think about teardown are the rare edge cases like:

# Working with files on disk
# Managing database connections
# Interacting with external services
# Using module/session-scoped fixtures that modify external state

#############

# there may be cases where you might not be using the RETURN/YIELD value from a fixture
# When it is so, there may be cases where you want to keep running the HOOK/FIXTURE before every test

# This is the purpose of autouse
# in the above example it is pointless, because the return value is being used anyway
