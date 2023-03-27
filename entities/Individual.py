from typing import List
from config import KNAPSACK_CAPACITY
from items import items


class Individual:
    def __init__(self, bits: List[int]):
        self.bits = bits

    def __str__(self):
        return repr(self.bits)

    def __hash__(self):
        return hash(str(self.bits))

    def fitness(self) -> float:
        if len(items) != len(self.bits):
            raise ValueError("Length of items and bits do not match")

        total_value = sum([
            bit * item.value
            for item, bit in zip(items, self.bits)
        ])

        total_weight = sum([
            bit * item.weight
            for item, bit in zip(items, self.bits)
        ])

        if total_weight <= KNAPSACK_CAPACITY:
            return total_value
        else:
            return 0.0
