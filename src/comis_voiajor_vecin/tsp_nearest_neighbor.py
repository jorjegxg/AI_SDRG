# algorithms/tsp_nearest_neighbor.py
import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_algorithm(cities):
    num_cities = len(cities)
    unvisited = list(range(num_cities))
    tour = [unvisited.pop(0)]  # Start with the first city

    while unvisited:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(cities[last_city], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)

    return tour

def total_distance(cities, tour):
    return sum(distance(cities[tour[i]], cities[tour[i - 1]]) for i in range(len(tour)))

def solve_tsp_nearest_neighbor(cities):
    tour = nearest_neighbor_algorithm(cities)
    tour_distance = total_distance(cities, tour)
    return tour, tour_distance
