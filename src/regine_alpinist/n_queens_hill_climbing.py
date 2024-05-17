# algorithms/n_queens_hill_climbing.py
import random

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def conflicts(board):
    N = len(board)
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_board(N):
    return [random.randint(0, N - 1) for _ in range(N)]

def get_neighbors(board):
    N = len(board)
    neighbors = []
    for row in range(N):
        for col in range(N):
            if col != board[row]:
                neighbor = list(board)
                neighbor[row] = col
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(N):
    current_board = generate_board(N)
    current_conflicts = conflicts(current_board)
    
    while True:
        neighbors = get_neighbors(current_board)
        neighbor_conflicts = [(conflicts(neighbor), neighbor) for neighbor in neighbors]
        neighbor_conflicts.sort(key=lambda x: x[0])
        
        if neighbor_conflicts[0][0] >= current_conflicts:
            break
        
        current_conflicts, current_board = neighbor_conflicts[0]
    
    return current_board, current_conflicts

def solve_n_queens_hill_climbing(N):
    board, conflicts_count = hill_climbing(N)
    return board, conflicts_count == 0
