
import sys
import alg_calirii_simulate.algoritm as alg_calirii_simulate
import alg_comis_voiajorului.algoritm as alg_comis_voiajorului
import regine_alpinist.n_queens_hill_climbing as regine_alpinist
import comis_voiajor_vecin.tsp_nearest_neighbor as comis_voiajor_vecin
import regine_bkt_recursiv.algoritm as regine_bkt_recursiv
import regine_algoritm_genetic.algotithm as regine_algoritm_genetic
import grafic_genetic.algoritm as grafic_genetic
import time
import matplotlib.pyplot as plt



def info():
    print("Echipa formata din: Halevici Diana , Stefan Constantin , Luta Gheorghe si Robert Franciuc")

def plot_chart(n_values_list, times_list, labels, linestyles=None):
    for i, times in enumerate(times_list):
        linestyle = linestyles[i] if linestyles else '-'
        plt.plot(n_values_list[i], times, label=labels[i], linestyle=linestyle)
    
    plt.xlabel('n')
    plt.ylabel('Timp (s)')
    plt.yscale('log')  # Setăm scala logaritmică pentru axa y pentru a vizualiza mai bine diferențele mari de timp
    plt.grid()
    plt.legend()
    plt.show()


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
        print("h. Plotare grafice problema comis-voiajorului")
        print("x. Info")
        print("y. Exit")

        optiune = input("Selectează o opțiune: ")

        if optiune == "a":
            solution = regine_bkt_recursiv.solve_n_queens(8)
            if solution:
                regine_bkt_recursiv.print_board(solution)
            else:
                print("Soluția nu a fost găsită:")
            
        elif optiune == "b":
           
            solution = regine_alpinist.hill_climbing(10)
            if solution:
                 print("Soluție găsită:")
                 regine_alpinist.print_board(solution)
            else:
                print("Soluția nu a fost găsită:")
           
            
        elif optiune == "c":
           alg_calirii_simulate.problema_reginei()
        elif optiune == "d":
            

            delay = .2
            solution = grafic_genetic.hill_climbing(8, delay)
            print("Soluție găsită:")
            grafic_genetic.plt.show()  
        elif optiune == "e":
            quens_n = [8, 10, 15, 20, 30]
            quens_times = [0.0019974708557128906, 0.0009987354278564453, 0.016996145248413086, 2.273759841918945, 1377.3080117702484]

            hill_n = [8, 10, 15, 20, 30, 50]
            hill_times = [0.0023665428161621094, 0.0019996166229248047, 0.024106264114379883, 0.052093505859375, 0.3319993019104004, 3.8466508388519287]

            simulated_n = [8, 10, 15, 20, 30, 50]
            simulated_times = [0.0010044574737548828, 0.0009989738464355469, 0.00971531867980957, 0.030997514724731445, 0.2919731140136719, 2.7361652851104736]

            genetics_n = [8, 10, 15, 20, 30, 50]
            genetic_times = [0.3528597354888916, 0.4942154884338379, 0.9322991371154785, 1.558121681213379, 3.7329616531140147, 4.637095267181819]

            n_values_list = [quens_n, hill_n, simulated_n, genetics_n]
            times_list = [quens_times, hill_times, simulated_times, genetic_times]
            labels = ['Backtracking', 'Hill Climb', 'Simulated Annealing', 'Genetic Algorithm']
            linestyles = ['-', '--', ':', '-.']  # Stiluri de linii diferite pentru fiecare algoritm

            plot_chart(n_values_list, times_list, labels, linestyles)


            
           
                 
        elif optiune == "f":
            alg_comis_voiajorului.rezolvare_comis_voiajor()
        elif optiune == "g":
            cities = [
                (0, 0), (1, 5), (2, 3), (5, 2), (6, 6)
            ]

            tour, distance = comis_voiajor_vecin.solve_tsp_nearest_neighbor(cities)
            
            print("Ordinea orașelor în tur:")
            for index in tour:
                print(f"Oraș {index} -> ", end="")
            print("Oraș 0")  # Presupunem că turul începe și se termină în orașul inițial

            print(f"Distanța totală a turului: {distance:.2f}")
        
        elif optiune == "h":
           
            n_values_bkt = [7, 11, 12, 13, 14, 15]
            execution_times_bkt = [0.0019996166229248047, 0.11960077285766602, 0.2956719398498535, 1.668032169342041, 10.81715178489685, 186.42819786071777]

            n_values_informed = [7, 11, 12, 13, 14, 15]
            execution_times_informed = [2.239999594166875e-05, 7.229999755509198e-05, 3.6299985367804766e-05, 3.819999983534217e-05, 4.75000124424696e-05, 4.549999721348286e-05]

            n_values_list = [n_values_bkt, n_values_informed]
            times_list = [execution_times_bkt, execution_times_informed]
            labels = ['Backtracking', 'Informed Search']
            linestyles = ['-', '--']  # Stiluri de linii diferite pentru fiecare algoritm

            plot_chart(n_values_list, times_list, labels, linestyles)


        elif optiune == "x":
            info()
        elif optiune == "y":
            print("EXIT")
            sys.exit()
        else:
            print("Opțiune invalidă. Te rog să selectezi o opțiune validă.")

if __name__ == "__main__":
    main()
