# What value does a fixture bring?
# 1. Isolation: Each test gets its own copy of the data, preventing test pollution.
# In the below example with no fixture if one test modified the global data list, it would affect other tests.
# 2. Reusability: Fixtures can be reused across multiple tests, reducing code duplication.
# 3. Parameterization: Fixtures can be parameterized to run tests with different inputs.
import pytest


# define the fixture decorator
@pytest.fixture
def prepare_data():
    return [i for i in range(10)]


# pass the fixture as an arg
def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data


##########

# no fixture version
data = [i for i in range(10)]


def test_elements2():
    assert 9 in data
    assert 10 not in data
