def factorial(n):
    if n == 0:
        return 1
    elif isinstance(n, int):
        return n * factorial(n - 1)
    else:
        return -1


def test_regular():
    assert factorial(5) == 120


def test_zero():
    assert factorial(0) == 1


def test_str():
    assert factorial("5") == -1
