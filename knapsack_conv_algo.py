import time
from config import *
import random as rd

start_time = time.time()


def knapsack(W, wt, val, n):
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


# Driver code
items_val = []
items_weights = []
for i in range(NUMBER_OF_ITEMS):
    weight: int = rd.randint(1, MAX_ITEM_WEIGHT)
    value: int = rd.randint(1, MAX_ITEM_VALUE)

    items_val.append(value)
    items_weights.append(weight)


W = KNAPSACK_WEIGHT
n = NUMBER_OF_ITEMS
print(knapsack(W, items_val, items_weights, n))
print((time.time() - start_time) * 1000, "ms")