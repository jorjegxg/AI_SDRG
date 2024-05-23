def is_safe(board, row, col, N):
    # Verifică rândul de la stânga la dreapta
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Verifică diagonala principală (de sus în stânga la jos în dreapta)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Verifică diagonala secundară (de jos în stânga la sus în dreapta)
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, N):
    # Dacă toate reginele sunt plasate, întoarce True
    if col >= N:
        return True
    
    # Încearcă să plasezi regina în fiecare rând din această coloană
    for i in range(N):
        if is_safe(board, i, col, N):
            # Plasează regina
            board[i][col] = 1
            
            # Recursiv, încearcă să plasezi restul reginelor
            if solve_n_queens_util(board, col + 1, N):
                return True
            
            # Dacă plasarea reginei în rândul curent nu duce la o soluție, o elimină (backtrack)
            board[i][col] = 0
    
    # Dacă regina nu poate fi plasată în niciun rând din această coloană, întoarce False
    return False

def solve_n_queens(N):
    # Inițializează tabla cu 0-uri
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Nu există o soluție")
        return None
    
    # Returnează tabla cu soluția
    return board

# Funcție pentru a afișa tabla
def print_board(board):
    for row in board:
        print(" ".join(str(e) for e in row))
