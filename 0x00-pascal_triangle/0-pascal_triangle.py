#!/usr/bin/python3
"""A module for working with Pascal's Triangle."""


def pascal_triangle(n):
    """Creates a list of lists representing Pascal's Triangle."""
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
