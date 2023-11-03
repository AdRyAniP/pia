import random
import timeit


def fitness(chromosome):
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                clashes += 1
    return clashes  # Lower clashes indicate a better fitness


def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + [queen for queen in parent2 if queen not in parent1[:crossover_point]]
    return child


def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        # Perform a swap mutation to maintain a valid solution
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome


def select_parents(population, fitness_fn, num_parents):
    total_fitness = sum(fitness_fn(chrom) for chrom in population)
    probabilities = [fitness_fn(chrom) / total_fitness for chrom in population]
    return random.choices(population, probabilities, k=num_parents)


def genetic_algorithm(pop_size, mutation_rate, generations):
    population = [list(range(8)) for _ in range(pop_size)]
    best_fitness = float('inf')
    best_chromosome = None
    no_improvement_count = 0

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            parents = select_parents(population, fitness, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        best_in_generation = min(population, key=fitness)
        if fitness(best_in_generation) < best_fitness:
            best_fitness = fitness(best_in_generation)
            best_chromosome = best_in_generation
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        if no_improvement_count >= 10:  # Termination condition
            break

    return best_chromosome


def main():
    best_solution = genetic_algorithm(pop_size=100, mutation_rate=0.1, generations=100)
    print("Mejor solución encontrada:", best_solution)


if __name__ == "__main__":
    result = timeit.timeit(stmt='main()', globals=globals(), number=1)
    print(f"Execution time is {result} seconds")
