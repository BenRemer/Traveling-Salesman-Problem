import numpy as np
import pandas as pd
import operator
import random
import sys
import multiprocessing
import time
import objects



def create_route(cityList):
    route = random.sample(cityList, len(cityList))
    return route

def initial_population(pop_size, city_list):
    population = []
    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population

def rank_routes(population):
    return_vals = {}
    for i in range(len(population)):
        return_vals[i] = objects.Fitness(population[i]).route_fitness()
    return sorted(return_vals.items(), key = operator.itemgetter(1), reverse = True) 

def selection(pop_ranked, save_size):
    return_vals = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    for i in range(save_size):
        return_vals.append(pop_ranked[i][0])
    for i in range(len(pop_ranked) - save_size):
        pick = random.random() * 100
        for i in range(len(pop_ranked)):
            if pick <= df.iat[i,3]:
                return_vals.append(pop_ranked[i][0])
                break
    return return_vals

def mate(pop, select):
    pool = []
    for i in range(len(select)):
        index = select[i]
        pool.append(pop[index])
    return pool

def breed(father, mother):
    child = []
    child_father = []
    child_mother = []
    gene1 = int(random.random() * len(father))
    gene2 = int(random.random() * len(mother))
    start = min(gene1, gene2)
    end = max(gene1, gene2)
    for i in range(start, end):
        child_father.append(father[i])
    child_mother = [item for item in mother if item not in child_father]
    child = child_father + child_mother
    return child

def breed_pop(pool, save_size):
    children = []
    keep = len(pool) - save_size
    selection = random.sample(pool, len(pool))
    for i in range(save_size):
        children.append(pool[i])
    for i in range(keep):
        child = breed(selection[i], selection[len(pool)-i-1])
        children.append(child)
    return children

def mutate(child, mutation_rate):
    for i in range(len(child)):
        if (random.random() < mutation_rate):
            j = int(random.random() * len(child))
            town1 = child[i]
            town2 = child[j]
            child[j] = town1
            child[i] = town2
    return child

def mutate_pop(population, mutation_rate):
    mutated = []
    for i in range(len(population)):
        new_child = mutate(population[i], mutation_rate)
        mutated.append(new_child)
    return mutated

def next_generation(current_generation, save_size, mutation_rate):
    pop_ranked = rank_routes(current_generation)
    selec = selection(pop_ranked, save_size)
    pool = mate(current_generation, selec)
    children = breed_pop(pool, save_size)
    next_generation = mutate_pop(children, mutation_rate)
    return next_generation

def genetic_algorithm(population, pop_size, save_size, mutation_rate, generations, t_end):
    pop = initial_population(pop_size, population)
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))
    for i in range(generations):
        if time.time() >= t_end:
            print('Time limit exceeded. Ending Program.')
            break
        pop = next_generation(pop, save_size, mutation_rate)
    print('Final distance:', str(1 / rank_routes(pop)[0][1]))
    best_route = pop[rank_routes(pop)[0][0]]
    return best_route

def main():
    if len(sys.argv) < 4:
        print('Need correct args, run with: \ngenetic.py <input> <output> <time>')
        return
    t_end = time.time() + int(sys.argv[3])
    cityList = []
    input_file = sys.argv[1]
    f = open(input_file, "r") # Open file
    for line in f:
        line = line.strip('\n') # Strip off new line character
        split = line.split(" ", 3) # Split into three parts
        cityList.append(objects.Town(x=float(split[1]), y=float(split[2])))
    f.close()
    
    rout = genetic_algorithm(population = cityList, pop_size = 250, save_size = 20, mutation_rate = 0.01, generations = 1500, t_end = t_end)
    print(rout)

if __name__ == "__main__":
    main()