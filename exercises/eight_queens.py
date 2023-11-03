import random


def fitness(chromosome):
    # Función de aptitud: cuántas reinas no se amenazan mutuamente
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                clashes += 1
    return n - clashes


def select_parents(population, fitness_fn, num_parents):
    parents = []
    for _ in range(num_parents):
        # Realizar la selección por ruleta
        total_fitness = sum(fitness_fn(chrom) for chrom in population)
        pick = random.uniform(0, total_fitness)
        current_fitness = 0
        for chrom in population:
            current_fitness += fitness_fn(chrom)
            if current_fitness > pick:
                parents.append(chrom)
                break

    if len(parents) < 2:
        parents = select_parents(population, fitness_fn, num_parents)  # Realizar una nueva selección si no se obtienen suficientes padres

    return parents


def crossover(parent1, parent2):
    # Cruce de dos padres para producir un descendiente
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(chromosome, mutation_rate):
    # Mutación de un cromosoma con una cierta probabilidad
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome


def genetic_algorithm(pop_size, mutation_rate, generations):
    # Algoritmo genético principal
    # Starts the initial population with an initial population of pop_size and with the chromosome [0,1,2,3,4,5,6,7]
    population = [list(range(8)) for _ in range(pop_size)]
    for gen in range(generations): # Generate a new generation by mutating the current population
        new_population = []
        for _ in range(pop_size):
            # Select the best parent from the population according to the fitness function
            parents = select_parents(population, fitness, 2)
            # Create a new child by crossing the parents' genomes
            child = crossover(parents[0], parents[1])
            # Generate a mutation in the new child with a max mutation rate of mutation_rate
            child = mutate(child, mutation_rate)
            # Add the new child to the population (new generation)
            new_population.append(child)
        # Replace the current population with the new generation
        population = new_population
    # Select the best chromosome from the population according to the fitness function
    best_chromosome = max(population, key=fitness)
    # Return the best chromosome
    return best_chromosome


def main():
    best_solution = genetic_algorithm(pop_size=100, mutation_rate=0.1, generations=100)
    print("Mejor solución encontrada:", best_solution)


if __name__ == "__main__":
    main()
