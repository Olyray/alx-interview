#!/usr/bin/python3
"""A solution to the nqueens problem"""
import sys


def is_safe(board, row, col, n):
    """Function to check if a queen can be placed
    at board[row][col]"""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    """Recursive utility function to solve N-Queens problem"""
    if col >= n:
        solution = [[i, j] for i in range(n) for j in range(n) if board[i][j]]
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = False


def solve_n_queens(n):
    """Function to solve N-Queens problem using backtracking"""
    board = [[False for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = solve_n_queens(N)
for solution in solutions:
    print(solution)
