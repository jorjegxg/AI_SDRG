# main.py

from algorithms.tsp_nearest_neighbor import solve_tsp_nearest_neighbor

def main():
    # Exemplu de coordonate pentru orașe
    cities = [
        (0, 0), (1, 5), (2, 3), (5, 2), (6, 6)
    ]

    tour, distance = solve_tsp_nearest_neighbor(cities)
    
    print("Ordinea orașelor în tur:")
    for index in tour:
        print(f"Oraș {index} -> ", end="")
    print("Oraș 0")  # Presupunem că turul începe și se termină în orașul inițial

    print(f"Distanța totală a turului: {distance:.2f}")

if __name__ == "__main__":
    main()
