import random
import matplotlib.pyplot as plt
import time

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

def plot_board(board, ax, fig, delay):
    N = len(board)
    ax.clear()
    # Desenează tabla de șah
    for x in range(N):
        for y in range(N):
            if (x + y) % 2 == 0:
                color = 'white'
            else:
                color = 'gray'
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color=color))
    
    # Desenează reginele
    for col in range(N):
        row = board[col]
        ax.add_patch(plt.Circle((col + 0.5, row + 0.5), 0.3, color='black'))
    
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(range(N))
    ax.set_yticks(range(N))
    ax.invert_yaxis()
    plt.draw()
    plt.pause(delay)

def hill_climbing(N, delay):
    board = generate_board(N)
    conflicts = calculate_conflicts(board)
    
    # Pregătește figura pentru plotare
    fig, ax = plt.subplots()
    
    while conflicts > 0:
        plot_board(board, ax, fig, delay)
        new_board, new_conflicts = get_best_move(board)
        if new_conflicts >= conflicts:
            # Dacă nu se găsește o îmbunătățire, reîncepe cu o configurație nouă
            board = generate_board(N)
            conflicts = calculate_conflicts(board)
        else:
            board = new_board
            conflicts = new_conflicts
    
    plot_board(board, ax, fig, delay)
    return board