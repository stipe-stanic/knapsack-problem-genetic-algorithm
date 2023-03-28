## Description

- Genes can have a value of 0 or 1. 1 represents the item inside the knapsack, while 0 represents otherwise.
- Chromosome represents one solution to the problem and holds N number of genes.
- Population is a set of solutions of size M.
- Fitness function calculates the fitness value of every solution(chromosome) based on the value and weight of each item.

## Genetic algorithm methods

- K-tournament selection: two winning parents with the highest fitness value are selected
- Recombination: random one-point crossover
- Mutation: flipping of bits, binary encoding


## Comparison

- After an input size of 4 million, the genetic algorithm takes less time to execute and find the optimal solution.

<img alt="Comparison of execution times of solving knapsack problem using a conventional algorithm and genetic algorithm" height="600" src="/plots/conv_vs_genetic.png" width="600"/>