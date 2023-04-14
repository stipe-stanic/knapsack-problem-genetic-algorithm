import matplotlib.pyplot as plt
from typing import List
def plot_comparison(end_times_ga: List[float], end_times_conv: List[float], sizes: List[int]):
    max_xlim = max(max(end_times_ga), max(end_times_conv))

    plt.ylim(0, max_xlim + (0.15 * max_xlim))
    plt.xlim(0, max(sizes))
    plt.plot(sizes, end_times_ga, label='Genetic Algorithm')
    plt.plot(sizes, end_times_conv, label='Conventional Algorithm')

    plt.xlabel('Size (number_of_items * knapsack_capacity)')
    plt.ylabel('Solution Time (ms)')
    plt.legend(loc='upper left')
    plt.show()
