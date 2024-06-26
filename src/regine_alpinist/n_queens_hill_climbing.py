import random

def generate_board(N):
    # Generează o configurație inițială aleatoare
    return [random.randint(0, N-1) for _ in range(N)]

def calculate_conflicts(board):
    conflicts = 0
    N = len(board)
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_best_move(board):
    N = len(board)
    min_conflicts = calculate_conflicts(board)
    best_board = board[:]
    
    for col in range(N):
        for row in range(N):
            if board[col] != row:
                new_board = board[:]
                new_board[col] = row
                new_conflicts = calculate_conflicts(new_board)
                if new_conflicts < min_conflicts:
                    min_conflicts = new_conflicts
                    best_board = new_board[:]
    
    return best_board, min_conflicts

def hill_climbing(N):
    board = generate_board(N)
    conflicts = calculate_conflicts(board)
    
    while conflicts > 0:
        new_board, new_conflicts = get_best_move(board)
        if new_conflicts >= conflicts:
            # Dacă nu se găsește o îmbunătățire, reîncepe cu o configurație nouă
            board = generate_board(N)
            conflicts = calculate_conflicts(board)
        else:
            board = new_board
            conflicts = new_conflicts
    
    return board

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