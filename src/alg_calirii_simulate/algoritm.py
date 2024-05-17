import random
import math


#problema celor N regine (alg. calirii simulate)

def generare_stare_initiala(dimensiune):
   
    return [random.randint(0, dimensiune-1) for _ in range(dimensiune)]

def cost(stare):
   
    conflicts = 0
    dimensiune = len(stare)
    for i in range(dimensiune):
        for j in range(i+1, dimensiune):
            if stare[i] == stare[j] or abs(stare[i] - stare[j]) == j - i:
                conflicts += 1
    return conflicts

def simulated_annealing(dimensiune, temperatura_maxima=1000, rata_racire=0.95, nr_iteratii=1000):
    stare_curenta = generare_stare_initiala(dimensiune)
    cost_curent = cost(stare_curenta)

    temperatura = temperatura_maxima

    for _ in range(nr_iteratii):
        temperatura *= rata_racire
        if temperatura == 0:
            break

        vecin = stare_curenta[:]
        coloana = random.randint(0, dimensiune-1)
        noua_linie = random.randint(0, dimensiune-1)
        vecin[coloana] = noua_linie
        cost_vecin = cost(vecin)

        delta_cost = cost_vecin - cost_curent

        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperatura):
            stare_curenta = vecin
            cost_curent = cost_vecin

    return stare_curenta

def afisare_tabla(stare):
    dimensiune = len(stare)
    for linie in range(dimensiune):
        for coloana in range(dimensiune):
            if stare[coloana] == linie:
                print("X ", end="")
            else:
                print(". ", end="")
        print()


def problema_reginei():
    dimensiune = int(input("Introduceți dimensiunea tablei de șah (numărul de regine): "))
    solutie = simulated_annealing(dimensiune)
    print("Soluția găsită:")
    afisare_tabla(solutie)