#!/usr/bin/python3
"""
Module to rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The input matrix to be rotated
    """
    n = len(matrix)

    # First, transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then, reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
