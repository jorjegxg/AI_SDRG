import sys
#Problema comis-voiajorului (Backtracking recursiv)
def problema_comis_voiajor(distante):
    numar_orase = len(distante)
    ruta_optima = [0] * (numar_orase + 1)
    vizitat = [False] * numar_orase
    vizitat[0] = True
    cost_minim = sys.maxsize

    def backtracking(oras_curent, lungime_ruta, nivel):
        nonlocal cost_minim

        if nivel == numar_orase:
            if distante[oras_curent][0] != 0 and lungime_ruta + distante[oras_curent][0] < cost_minim:
                cost_minim = lungime_ruta + distante[oras_curent][0]
                ruta_optima[:numar_orase] = orase_vizitate[:]
                ruta_optima[numar_orase] = 0
            return

        for oras_urmator in range(numar_orase):
            if not vizitat[oras_urmator] and distante[oras_curent][oras_urmator] != 0:
                vizitat[oras_urmator] = True
                orase_vizitate.append(oras_urmator)
                backtracking(oras_urmator, lungime_ruta + distante[oras_curent][oras_urmator], nivel + 1)
                vizitat[oras_urmator] = False
                orase_vizitate.pop()

    orase_vizitate = [0]
    backtracking(0, 0, 1)

    return ruta_optima, cost_minim

def afisare_ruta(ruta):
    print("Ruta optimă:", ruta[:-1])
    print("Cost minim:", ruta[-1])


def rezolvare_comis_voiajor():
    print("Ai selectat problema comis-voiajorului (backtracking recursiv).")
    distante = [
        [0, 10, 15, 20], #de la orașul 0 la celelalte orașe
        [10, 0, 35, 25], #de la orașul 1 la celelalte orașe
        [15, 35, 0, 30], #de la orașul 2 la celelalte orașe
        [20, 25, 30, 0] #de la orașul 3 la celelalte orașe
    ]
    ruta_optima, cost_minim = problema_comis_voiajor(distante)
    print("Ruta optimă:", ruta_optima)
    print("Cost minim:", cost_minim)