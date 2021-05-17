import time
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from random import choices, randint, randrange, random
from typing import List, Callable, Tuple
from collections import namedtuple
from functools import partial

fitness_type = input(f"Fitness Type: Knapsack = 0, Test = 1:  ")
selection_type = input(f"Selection Type: Elitism = 0, Roulette = 1, Rank = 2, Tournament = 3 : ")
crossover_type = input(f"Crossover Type: Single = 0, Multi = 1, Uniform = 2: ")
mutation_type = input(f"Mutation Type: Random Flip = 0, Test = 1:  ")


value_population_limit = 10 #int(input("Enter Population Size: "))  # 10
value_generation_limit = 100 #int(input("Enter Generation Limit: "))  # 100
value_fitness_limit = 1000 #int(input("Enter Fitness Score Limit(0-1410): "))  # 1310
value_weight_limit = 750 #int(input("Enter Max Weight(25-3648): "))  # 3000

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
PrinterFunc = Callable[[Population, int, FitnessFunc], None]
Thing = namedtuple('Thing', ['name', 'value', 'weight'])




things = [
    Thing('Laptop', 500, 2200),
    Thing('Headphones', 150, 160),
    Thing('Coffee Mug', 60, 350),
    Thing('Notepad', 40, 333),
    Thing('Water Bottle', 30, 192),
]

more_things = [
                  Thing('Mints', 5, 25),
                  Thing('Socks', 10, 38),
                  Thing('Tissues', 15, 80),
                  Thing('Phone', 500, 200),
                  Thing('Baseball Cap', 100, 70)
              ] + things


def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num + 1)]


def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)


def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    #print(f"fitness")
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")

    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value

def fitness1(genome: Genome, things: [Thing], weight_limit: int) -> int:
    #print(f"fitness1")
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")

    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value

def elitism(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2

    )


def tournament(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2

    )


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")

    length = len(a)
    if length < 2:
        return a, b
    #print(f"This is single")
    p = randint(1, length - 1)

    return a[0:p] + b[p:], b[0:p] + a[p:]


def multi_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")
    #print(f"This is multi")
    length = len(a)
    if length < 2:
        return a, b

    p1 = randint(1, length)
    p2 = randint(1, length - 1)
    if p2 >= p1:
        p2 += 1

    else:
        p1, p2 = p2, p1

    a[p1:p2], b[p1:p2] \
        = b[p1:p2], a[p1:p2]

    return a, b


def uniform_crossover(a: Genome, b: Genome, abpb: Genome, ) -> Tuple[Genome, Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")

    length = len(a)
    if length < 2:
        return a, b, abpb

    for i in randrange(length):
        if random() < abpb:
            a[i], b[i] = b[i], a[i]

    return a, b, abpb


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:

    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
        #print(f"mutation")
    return genome

def mutation1(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:

    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
        #print(f"mutation1")
    return genome


dispatcher = {'0': single_point_crossover,'1': multi_point_crossover,'2': uniform_crossover}
dispatcher2 = {'0': mutation,'1': mutation1}
dispatcher3 = {'0': elitism,'1': tournament}


def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int = value_fitness_limit,
        selection_func: SelectionFunc = dispatcher3[selection_type],
        crossover_func: CrossoverFunc = dispatcher[crossover_type],
        mutation_func: MutationFunc = dispatcher2[mutation_type],
        generation_limit: int = value_generation_limit,

) -> Tuple[Population, int]:
    population = populate_func()



    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)

        if fitness_func(population[0]) >= fitness_limit:
            break


        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)

    return population, i

dispatcher1 = {'0': fitness,'1': fitness1}
start = time.time()

population, generations = run_evolution(
    populate_func=partial(
        generate_population, size=value_population_limit, genome_length=len(more_things)
    ),
    fitness_func=partial(
        dispatcher1[fitness_type], things=more_things, weight_limit=value_weight_limit
    ),
    fitness_limit=value_fitness_limit,
    generation_limit=value_generation_limit
)
end = time.time()


def genome_to_things(genome: Genome, things: [Thing]) -> [Thing]:
    result = []
    total_fitness_score = 0
    total_weight = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing.name]
            total_fitness_score += thing.value
            total_weight += thing.weight

    success_rate = total_fitness_score * 100 / value_fitness_limit
    load_rate = total_weight * 100 / value_weight_limit

    print(f"Fitness Score: {total_fitness_score}")
    print(f"Success Rate %{success_rate}")
    print(f"Total Weight: {total_weight}")
    print(f"Load Rate % {load_rate} ")

    return result


print(f"Number of Generations: {generations}")
print(f"Total Running Time: {end - start}s")
print(f"Best Solution: {genome_to_things(population[0], more_things)}")




myfunct(main.all)