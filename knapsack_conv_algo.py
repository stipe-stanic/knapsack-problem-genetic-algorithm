import time
from config import *
import random as rd
from typing import List


def knapsack(W: int, val: List[int], wt: List[int], n: int):
    """
    :param W: knapsack capacity
    :param val: items values
    :param wt: items weights
    :param n: number of items
    :return: knapsack with maximum possible value
    """
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


if __name__ == "__main__":
    start_time = time.time()

    items_val: List[int] = []
    items_weights: List[int] = []
    for i in range(NUMBER_OF_ITEMS):
        weight: int = rd.randint(1, MAX_ITEM_WEIGHT)
        value: int = rd.randint(1, MAX_ITEM_VALUE)

        items_weights.append(weight)
        items_val.append(value)

    print(knapsack(KNAPSACK_CAPACITY, items_val, items_weights, NUMBER_OF_ITEMS))
    print((time.time() - start_time) * 1000, "ms")