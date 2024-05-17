import random

def generate_individual(N):
    # Generează un individ (soluție posibilă) aleatoriu
    return [random.randint(0, N-1) for _ in range(N)]

def calculate_fitness(individual):
    # Fitness-ul este numărul de perechi de regine care nu se atacă
    non_attacking_pairs = 0
    N = len(individual)
    
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
    
    return non_attacking_pairs

def crossover(parent1, parent2):
    # Realizează crossover-ul între doi părinți pentru a genera un copil
    N = len(parent1)
    crossover_point = random.randint(1, N - 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    # Realizează mutații asupra unui individ cu o anumită rată de mutație
    N = len(individual)
    for i in range(N):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, N - 1)
    return individual

def genetic_algorithm(N, population_size=100, generations=1000, mutation_rate=0.01):
    # Generează populația inițială
    population = [generate_individual(N) for _ in range(population_size)]
    
    for generation in range(generations):
        # Calculează fitness-ul pentru fiecare individ
        fitness_scores = [(individual, calculate_fitness(individual)) for individual in population]
        
        # Sortează populația după fitness
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Dacă am găsit o soluție perfectă (fitness maxim), o returnăm
        if fitness_scores[0][1] == N * (N - 1) // 2:
            return fitness_scores[0][0]
        
        # Selectează părinții (cu probabilitate proporțională cu fitness-ul)
        selected_parents = [individual for individual, fitness in fitness_scores[:population_size//2]]
        
        # Creează noua generație prin crossover și mutație
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
    
    # Returnează cea mai bună soluție găsită
    return fitness_scores[0][0]

def print_board(board):
    N = len(board)
    for row in range(N):
        line = ""
        for col in range(N):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")