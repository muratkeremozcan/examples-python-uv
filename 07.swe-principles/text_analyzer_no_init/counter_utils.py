from collections import Counter

import matplotlib.pyplot as plt


def plot_counter_most_common(items):
    labels, values = zip(*items)
    plt.figure()
    plt.barh(range(len(labels)), values, tick_label=labels)
    plt.show()


def sum_counters(counters):
    return sum(counters, Counter())


def plot_counter(counter, n_most_common=5):
    top_items = counter.most_common(n_most_common)
    plot_counter_most_common(top_items)
