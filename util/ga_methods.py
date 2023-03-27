from typing import Tuple

from config import *
from entities.Individual import *
import random as rd
from items import items


def generate_initial_population(count=POPULATION_SIZE) -> List[Individual]:
    population = set()

    # generate initial population
    while len(population) != count:
        # Generate random bit values
        bits = [
            rd.choice([0, 1])
            for _ in range(len(items))
        ]
        population.add(Individual(bits))

    return list(population)


# tournament selection
def selection(population: List[Individual]) -> List[Individual]:
    parents: List[Individual] = []

    rd.shuffle(population)

    # tournament selection between all individuals
    for i in range(len(population)):
        j = rd.randint(0, len(population) - 1)
        if population[i].fitness() > population[j].fitness():
            parents.append(population[i])
        else:
            parents.append(population[j])

    # This returns a list of the two fittest individuals after performing tournament selection.
    return sorted(parents, key=lambda x: x.fitness(), reverse=True)[:2]


# random one-point crossover
def crossover(parents: List[Individual]) -> List[Individual]:
    N = NUMBER_OF_ITEMS
    crossover_point = rd.randint(1, N-1)

    child1 = parents[0].bits[:crossover_point] + parents[1].bits[crossover_point:]
    child2 = parents[1].bits[:crossover_point] + parents[0].bits[crossover_point:]

    return [Individual(child1), Individual(child2)]


def mutate(individuals: List[Individual]) -> None:
    for individual in individuals:
        for i in range(len(individual.bits)):
            if rd.random() < MUTATION_RATE:
                # bit flip
                if individual.bits[i] == 1:
                    individual.bits[i] = 0
                else:
                    individual.bits[i] = 1


def next_generation(population: List[Individual]) -> List[Individual]:
    next_gen = []

    # Elitism: keep the best individual from the previous generation
    best_individual = max(population, key=lambda x: x.fitness())
    next_gen.append(best_individual)

    while len(next_gen) < len(population):
        children = []

        # we run selection and get parents
        parents = selection(population)

        if rd.random() < REPRODUCTION_RATE:
            children = parents
        else:
            # crossover
            if rd.random() < CROSSOVER_RATE:
                children = crossover(parents)

            # mutation
            if rd.random() < MUTATION_RATE:
                mutate(children)

        next_gen.extend(children)

    return next_gen[:len(population)]


def print_generation(population: List[Individual]):
    for individual in population:
        print(individual.bits, individual.fitness())
    print()
    print("Average fitness", average_fitness(population))
    print("-" * 32)


# Returns the average fitness for the current population
def average_fitness(population: List[Individual]) -> float:
    return sum([i.fitness() for i in population]) / len(population)


def solve_knapsack() -> Tuple[Individual, int]:
    population: List[Individual] = generate_initial_population()

    best_fitness = float('-inf')
    num_of_evolutions = 0
    generations_without_improvement = 0

    for _ in range(MAX_NUMBER_OF_GENERATIONS):
        # Terminate if there has been no improvement in the best fitness for a given number of generations
        if generations_without_improvement > TERMINATION_CONDITION:
            break

        population = next_generation(population)
        num_of_evolutions += 1

        # Check for improvement in the best fitness
        population = sorted(population, key=lambda i: i.fitness(), reverse=True)
        current_best_fitness = population[0].fitness()
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1

    # Returns the fittest individual
    return population[0], num_of_evolutions