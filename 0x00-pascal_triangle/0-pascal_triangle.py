#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n.

    Args:
        n: integer representing the number of rows

    Returns:
        List of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    # Initialize triangle with first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        # Previous row
        prev_row = triangle[-1]
        # Start new row with 1
        current_row = [1]

        # Calculate middle values
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])

        # End row with 1
        current_row.append(1)

        # Add row to triangle
        triangle.append(current_row)

    return triangle
