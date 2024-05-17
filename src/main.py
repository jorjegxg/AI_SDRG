
import sys
import alg_calirii_simulate.algoritm as alg_calirii_simulate
import alg_comis_voiajorului.algoritm as alg_comis_voiajorului
import regine_alpinist.n_queens_hill_climbing as regine_alpinist
import comis_voiajor_vecin.tsp_nearest_neighbor as comis_voiajor_vecin
import regine_bkt.algoritm as regine_bkt


def info():
    print("Echipa formata din: Luta Gheorghe, Stefan Constantin, Halevici Diana si Robert")

def main():
    while True:
        print("\nMeniu:")
        print("a. Problema celor N regine (backtracking recursiv)")
        print("b. Problema celor N regine (alg. alpinistului)")
        print("c. Problema celor N regine (alg. calirii simulate)")
        print("d. Problema celor N regine (alg. genetic)")
        print("e. Plotare grafice problema celor N regine")
        print("f. Problema comis-voiajorului (backtracking recursiv)")
        print("g. Problema comis-voiajorului (alg. celui mai apropiat vecin)")
        print("x. Info")
        print("y. Exit")

        optiune = input("Selectează o opțiune: ")

        if optiune == "a":
            N = int(input("Introduceți lungimea tablei (N): "))
            if N <= 0:
                raise ValueError("Lungimea tablei trebuie să fie un număr întreg pozitiv.")
            
            solution = regine_bkt.solve_n_queens(N)
            if solution:
                regine_bkt.print_board(solution)

            print('a')
            
        elif optiune == "b":
            N = 8  # Schimbă valoarea pentru a încerca alte dimensiuni ale tablei
            solution, solved = regine_alpinist.solve_n_queens_hill_climbing(N)
            
            if solved:
                print(f"O soluție pentru {N} regine este:")
                board = [[0]*N for _ in range(N)]
                for row in range(N):
                    board[row][solution[row]] = 1
                regine_alpinist.print_board(board)
            else:
                print(f"Nu s-a găsit nicio soluție pentru {N} regine.")
            
        elif optiune == "c":
           alg_calirii_simulate.problema_reginei()
        elif optiune == "d":
            print('d')
        elif optiune == "e":
            print('e')
        elif optiune == "f":
            alg_comis_voiajorului.rezolvare_comis_voiajor()
        elif optiune == "g":
             # Exemplu de coordonate pentru orașe
            cities = [
                (0, 0), (1, 5), (2, 3), (5, 2), (6, 6)
            ]

            tour, distance = comis_voiajor_vecin.solve_tsp_nearest_neighbor(cities)
            
            print("Ordinea orașelor în tur:")
            for index in tour:
                print(f"Oraș {index} -> ", end="")
            print("Oraș 0")  # Presupunem că turul începe și se termină în orașul inițial

            print(f"Distanța totală a turului: {distance:.2f}")
            
        elif optiune == "x":
            info()
        elif optiune == "y":
            print("EXIT")
            sys.exit()
        else:
            print("Opțiune invalidă. Te rog să selectezi o opțiune validă.")

if __name__ == "__main__":
    main()
