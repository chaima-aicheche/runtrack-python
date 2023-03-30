# Job 0

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

num = int(input("Entrez un nombre entier : "))
if num < 0:
    print("Erreur: Le nombre doit être positif.")
else:
    print("La factorielle de", num, "est", recursive_factorial(num))

# Job 01

def recursive_power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return recursive_power(x*x, n//2)
    else:
        return x * recursive_power(x*x, (n-1)//2)

x = int(input("Entrez un nombre entier x: "))
n = int(input("Entrez un nombre entier positif n: "))
if n < 0:
    print("Erreur: n doit être positif.")
else:
    print(x, "puissance", n, "est", recursive_power(x, n))

# Job 03

def print_board(board):
    for row in board:
        print(' '.join(row))

def is_valid_move(board, row, col):
    n = len(board)
    # Check row
    for i in range(n):
        if board[row][i] == 'X':
            return False
    # Check column
    for i in range(n):
        if board[i][col] == 'X':
            return False
    # Check diagonal (top-left to bottom-right)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j] == 'X':
            return False
    # Check diagonal (bottom-left to top-right)
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'X':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 'X':
            return False
    return True

def solve_n_queens(board, n, col):
    if col == n:
        return True
    for i in range(n):
        if is_valid_move(board, i, col):
            board[i][col] = 'X'
            if solve_n_queens(board, n, col+1):
                return True
            board[i][col] = 'O'
    return False

n = int(input("Entrez la taille du plateau: "))
board = [['O' for _ in range(n)] for _ in range(n)]
if solve_n_queens(board, n, 0):
    print_board(board)
else:
    print("Impossible de placer les dames sur le plateau.")

