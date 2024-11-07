#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen on board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions.
    """
    def backtrack(board, col, solutions):
        """
        Recursive function to solve the N Queens problem.
        """
        if col == n:
            solutions.append([row.copy() for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                backtrack(board, col + 1, solutions)
                board[i][col] = 0

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)

    for solution in solutions:
        print([[i, solution[i].index(1)] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
