# with doctest, you basically write the test inside the docstring

import doctest
from collections import Counter

from text_analyzer import Document, sum_counters


def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2, '1': 1, '2': 1, '4': 1, '7': 1, '8': 1, '11': 1, '13': 1, '14': 1})
    """
    return sum(counters, Counter())


doctest.testmod()
