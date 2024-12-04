#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.

This module provides a function that determines the perimeter of an island
represented in a 2D grid where 1 represents land and 0 represents water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
        grid (List[List[int]]): A 2D grid representing land and water.
                                0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if current cell is land
            if grid[row][col] == 1:
                # Check all 4 adjacent sides (up, down, left, right)

                # Check top side
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1

                # Check bottom side
                if row == len(grid) - 1 or grid[row+1][col] == 0:
                    perimeter += 1

                # Check left side
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1

                # Check right side
                if col == len(grid[0]) - 1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
