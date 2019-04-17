import numpy as np
import pandas
import operator
import random
import sys
import multiprocessing
import time
import objects

# Randomizes the cities and returns as a route
def create_route(cities):
    size = len(cities)
    route = random.sample(cities, size)
    # print(route, "\n")
    return route

# Creates a population of size size of routes
def initial_population(size, cities):
    population = []
    for i in range(size):
        population.append(create_route(cities))
    return population

# Ranks each route in the population and sorts it by their fitness
def rank_routes(population):
    fitness = {}
    for i in range(len(population)):
        fitness[i] = objects.Fitness(population[i]).route_fitness()
    sorted_list = sorted(fitness.items(), key = operator.itemgetter(1), reverse = True) 
    # print(sorted_list,'\n')
    return sorted_list

# Selects a population of routes and saves selected indexes routes 
def mate(ranked_population, save_size,  population):
    selected = []
    data_frame = pandas.DataFrame(np.array(ranked_population), columns = ["Index", "Fitness"]) # Two-dimensional size-mutable with labeled axes (rows and columns)
    data_frame['cum_sum'] = data_frame.Fitness.cumsum()
    data_frame['percentage'] = (data_frame.cum_sum * 100) / data_frame.Fitness.sum()
    # print(data_frame)
    for i in range(save_size): # Save the top 'save_size' contenders
        selected.append(ranked_population[i][0])
    for i in range((len(ranked_population) - save_size)):
        random_pick = random.random() * 100
        for i in range(len(ranked_population)):
            if random_pick <= data_frame.iat[i, 3]:
                selected.append(ranked_population[i][0])
                break
    # print(select)
    pool = []
    for i in range(len(selected)):
        index = selected[i]
        # print(population[index])
        pool.append(population[index])
    # print(pool)
    return pool

# Takes two parents, get random 'genes' from them and splice them together in the same order
def breed(father, mother):
    child = []
    genes_father = []
    genes_mother = []
    gene1 = int(random.random() * len(father))
    gene2 = int(random.random() * len(mother))
    start = min(gene1, gene2)
    end = max(gene1, gene2)
    for i in range(start, end):
        genes_father.append(father[i])
    # print(genes_father)
    genes_mother = [item for item in mother if item not in genes_father] # Keep genes not being kept in father's
    # print(genes_mother)
    child = genes_father + genes_mother
    # print(child)
    return child

# Runs breeding function over the entire population but saving 'save_selection' of top routs without changing
def breed_pop(pool, save_size):
    children = []
    keep = len(pool) - save_size
    selection = random.sample(pool, len(pool))
    for i in range(save_size):
        children.append(pool[i])
    for i in range(keep):
        child = breed(selection[i], selection[len(pool) - i - 1])
        children.append(child)
    return children

# Randomly 'mutates' a child by swapping random locations
def mutate(child, mutation_rate):
    for i in range(len(child)):
        if (random.random() < mutation_rate):
            j = int(random.random() * len(child))
            city1 = child[i]
            city2 = child[j]
            child[j] = city1
            child[i] = city2
    return child

# Runs mutate function over entire population
def mutate_pop(population, mutation_rate):
    mutated = []
    for i in range(len(population)):
        child = mutate(population[i], mutation_rate)
        mutated.append(child)
    return mutated

# Takes a generation, ranks them, mates them and saves the next generation
def next_generation(current_generation, save_size, mutation_rate):
    pop_ranked = rank_routes(current_generation)
    pool = mate(pop_ranked, save_size, current_generation)
    children = breed_pop(pool, save_size)
    next_generation = mutate_pop(children, mutation_rate)
    return next_generation

# Runs program over certain time limit or till all generations have been made
def find_tsp(population, pop_size, save_size, mutation_rate, generations, t_end):
    current_gen = initial_population(pop_size, population)
    for i in range(generations):
        if time.time() >= t_end:
            print('Time limit exceeded. Ending Program.')
            break
        current_gen = next_generation(current_gen, save_size, mutation_rate)
    best_route = current_gen[rank_routes(current_gen)[0][0]]
    distance = str(1 / rank_routes(current_gen)[0][1])
    return best_route, distance

# Create timer and run code
def main():
    if len(sys.argv) < 4:
        print('Need correct args, run with: \ngenetic.py <input> <output> <time>')
        return
    t_end = time.time() + int(sys.argv[3]) - 1
    cityList = []
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    f = open(input_file, "r") # Open file
    for line in f:
        line = line.strip('\n') # Strip off new line character
        split = line.split(" ", 3) # Split into three parts
        cityList.append(objects.City(x = int(float(split[1])), y = int(float(split[2])), node_id = int(split[0])))
    f.close()
    print('Running for ' + sys.argv[3] + ' seconds.')
    rout, distance = find_tsp(population = cityList, pop_size = 250, save_size = 20, mutation_rate = 0.01, generations = 150000, t_end = t_end)
    f = open(output_file, 'w')
    f.write(distance + '\n')
    for city in rout:
        f.write(str(city))
        f.write(' ')
    f.write(str(rout[0]))
    print(rout)

if __name__ == "__main__":
    main()