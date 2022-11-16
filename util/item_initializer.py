from tabulate import tabulate
from entities.Item import *
import random as rd
from typing import List
from config import *


def print_items(items: List[Item]):
    table: list[any] = []

    for item in items:
        table.append([item.name, item.weight, item.value])

    print(tabulate(table, headers=["item_id", "weight", "value"], tablefmt="fancy_grid", numalign="center"))


def generate_items() -> List[Item]:
    items: List[Item] = []

    for i in range(NUMBER_OF_ITEMS):
        name: str = chr(i + 65)
        weight: int = rd.randint(1, MAX_ITEM_WEIGHT)
        value: int = rd.randint(1, MAX_ITEM_VALUE)

        items.append(Item(name, weight, value))

    return items