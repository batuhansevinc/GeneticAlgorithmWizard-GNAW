import random
from statistics import mean
from fitness import *
from gui import crossover_type


crossover_type = "0"
import os



mutation_val = 0.1 #float(input(f"Set Mutation Probablity: "))


def generate_individual():

    return [random.randint(0, 6) for i in range(0, 243)]


def mutation(ind, m):
    for k, v in enumerate(ind):
        if random.random() < m:
            ind[k] = random.randint(0, 6)
    return ind


def crossover_singlepoint(ind1, ind2):
    # print(f"111111")
    p = random.randint(0, len(ind1))
    c1 = ind1[0: p] + ind2[p:]
    c2 = ind2[0: p] + ind1[p:]
    return c1, c2


def crossover_multipoint(ind1, ind2):
    # print(f"222222")
    p3 = random.randint(0, len(ind1))
    p4 = random.randint(0, len(ind1) - 1)
    c1 = ind1[p3: p4] + ind2[p3:p4]
    c2 = ind2[p4: p3] + ind1[p4:p3]

    return c1, c2



class bam:

      def __init__(self):
            super().__init__()

            self.p = None

      def start_f(self):
        # genetic algorithm:

        N = 100 #input(int(f"number of individuals in population"))  # number of individuals in population 100
        G = 200 #input(int(f"umber of generations"))  # number of generations 200
        pop = list()
        # init pop
        for i in range(N):
            pop.append(generate_individual())

        dispatcher = {'0': crossover_singlepoint, '1': crossover_multipoint}
        # genetic algorithm loop
        for i in range(G):
            f_vals = list()  # a place for fitness values of each individual
            for ind in pop:
                f_vals.append(fitness(ind))  # compute fitness for all in the population
            newpop = list()  # the NEXT generation...
            bfitpop = max(f_vals)
            while len(newpop) < N:  # keep doing this until we have N number of inds in newpop

                idx = random.choices(range(0, len(pop)), k=16)  # -> randomly selects 16 inds
                val = [f_vals[p] for p in idx]  # -> grabs the fitness values for selected idx
                p1 = pop[idx[val.index(max(val))]]
                # do it again
                # burada aynı idx geliyor olmasın? üstteki listeden iki tane en iyi seçmeyi deneyelim
                idx.pop(val.index(max(val)))  # remove max
                val.pop(val.index(max(val)))

                p2 = pop[idx[val.index(max(val))]]

                m = mutation_val
                # children
                c1 = list()
                c2 = list()
                c1, c2 = dispatcher[crossover_type](p1, p2)
                c1 = mutation(c1, m)
                c2 = mutation(c2, m)
                newpop.append(c1)
                newpop.append(c2)
            pop = newpop
            print("mean: " + str(mean(f_vals)) + ", best: " + str(bfitpop))




