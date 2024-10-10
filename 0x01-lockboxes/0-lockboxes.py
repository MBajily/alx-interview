#!/usr/bin/python3
"""Module for determining if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list contains
                              keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = {0}  # Set to keep track of boxes we can open
    keys = boxes[0]  # Start with keys from the first box
    new_keys = boxes[0]  # Keys we haven't used yet

    # While we have keys we haven't tried yet
    while new_keys:
        current_key = new_keys.pop()

        # If this is a valid box number we haven't visited
        if isinstance(current_key, int) and \
           0 <= current_key < n and \
           current_key not in visited:

            # Add any new keys we find to our set of keys to try
            new_keys.extend(boxes[current_key])
            # Mark this box as visited
            visited.add(current_key)

    # Check if we can open all boxes
    return len(visited) == n
