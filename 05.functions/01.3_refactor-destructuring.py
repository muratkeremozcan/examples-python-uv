from typing import Iterable, Tuple


def mean_and_median(values: Iterable[float]) -> Tuple[float, float]:
    """Get the mean and median of a sorted list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      tuple (float, float): The mean and median
    """
    mean = sum(values) / len(values)
    values = sorted(values)
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return mean, median


# refactor the above to be piece-meal
def mean(values: Iterable[float]) -> float:
    """Calculate the mean of a sequence of floats."""
    return sum(values) / len(values)


def median(values: Iterable[float]) -> float:
    values = sorted(values)
    midpoint = int(len(values) / 2)
    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return median


def mean_and_median(values: Iterable[float]) -> Tuple[float, float]:
    return mean(values), median(values)


######## usage

sample = [3.2, 3.8, 2.9, 3.5, 3.0]
# destructuring
mean, median = mean_and_median(sample)

print(f"Values: {sample}")
print(f"Mean: {mean}")
print(f"Median: {median}")
