# main.py

from regine_alpinist.n_queens_hill_climbing import solve_n_queens_hill_climbing, print_board

def main():
    N = 8  # Schimbă valoarea pentru a încerca alte dimensiuni ale tablei
    solution, solved = solve_n_queens_hill_climbing(N)
    
    if solved:
        print(f"O soluție pentru {N} regine este:")
        board = [[0]*N for _ in range(N)]
        for row in range(N):
            board[row][solution[row]] = 1
        print_board(board)
    else:
        print(f"Nu s-a găsit nicio soluție pentru {N} regine.")

if __name__ == "__main__":
    main()
