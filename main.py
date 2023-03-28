from util.ga_methods import *
import time

if __name__ == '__main__':
    start_time = time.time()
    solution, num_of_evo = solve_knapsack()

    print(f'{solution}\n{solution.fitness()}')
    print((time.time() - start_time) * 1000, "ms")
    print(num_of_evo)