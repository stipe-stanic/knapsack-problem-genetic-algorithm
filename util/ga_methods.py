from typing import Tuple

from config import *
from entities.Individual import *
import random as rd
from items import items
from statistics import mean


def generate_initial_population(count=POPULATION_SIZE) -> List[Individual]:
    population = set()

    # generate initial population
    while len(population) != count:
        bits = [
            rd.choice([0, 1])
            for _ in items
        ]
        population.add(Individual(bits))

    return list(population)


# k(4) - tournament selection
def selection(population: List[Individual]) -> List[Individual]:
    parents: List[Individual] = []

    rd.shuffle(population)

    # tournament between first and second
    if population[0].fitness() > population[1].fitness():
        parents.append(population[0])
    else:
        parents.append(population[1])

    # tournament between third and fourth
    if population[2].fitness() > population[3].fitness():
        parents.append(population[2])
    else:
        parents.append(population[3])

    return parents


# one-point crossover
def crossover(parents: List[Individual]) -> List[Individual]:
    N = NUMBER_OF_ITEMS

    child1 = parents[0].bits[:N // 2] + parents[1].bits[N // 2:]
    child2 = parents[0].bits[N // 2:] + parents[1].bits[:N // 2]

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
    while len(next_gen) < len(population):
        children = []

        # we run selection and get parents
        parents = selection(population)

        # elitism
        if rd.random() < REPRODUCTION_RATE:
            children = parents
        else:
            # crossover
            if rd.random() < CROSSOVER_RATE:
                children = crossover(parents)

            # mutation
            ##if rd.random() < MUTATION_RATE:
                ##mutate(children)

        next_gen.extend(children)

    return next_gen[:len(population)]


def print_generation(population: List[Individual]):
    for individual in population:
        print(individual.bits, individual.fitness())
    print()
    print("Average fitness", sum([x.fitness() for x in population]) / len(population))
    print("-" * 32)


def average_fitness(population: List[Individual]) -> float:
    return sum([i.fitness() for i in population]) / len(population)


def solve_knapsack() -> Tuple[Individual, int]:
    population: List[Individual] = generate_initial_population()

    avg_fitness = []
    num_of_evolutions = 0

    for _ in range(MAX_NUMBER_OF_GENERATIONS):
        if len(avg_fitness) > TERMINATION_CONDITION:
            # if (average_fitness(population)) > 500:
            #     break
            curr_pop_fitness = average_fitness(population)
            mean_pop = mean(avg_fitness[-TERMINATION_CONDITION:])

            if mean_pop == curr_pop_fitness:
                break
            else:
                avg_fitness.append(curr_pop_fitness)
                population = next_generation(population)
                num_of_evolutions += 1
        else:
            if (average_fitness(population)) > 500:
                break
            avg_fitness.append(average_fitness(population))

            population = next_generation(population)
            num_of_evolutions += 1

    population = sorted(population, key=lambda i: i.fitness(), reverse=True)
    return population[0], num_of_evolutions