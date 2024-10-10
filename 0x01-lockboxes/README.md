# Lockboxes

## Description
This project contains a solution to the Lockboxes problem, where we need to determine if all boxes in a set of locked boxes can be opened. Each box is numbered sequentially and contains keys to other boxes.

## Problem Statement
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes. Write a method that determines if all the boxes can be opened.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the `PEP 8` style (version 1.7.x)
- All files must be executable

### Function Requirements
- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

## Approach
The solution uses a Breadth-First Search (BFS) approach with the following strategy:

1. Start with box 0 (which is already unlocked)
2. Keep track of:
   - Boxes we've visited
   - Keys we've found but haven't used yet
3. For each new key we find:
   - If it opens a box we haven't visited:
     - Add any new keys from that box to our collection
     - Mark the box as visited
4. Continue until we either:
   - Visit all boxes (return True)
   - Run out of keys to try (return False)

## Time Complexity
- Time Complexity: O(N + K)
  - N is the number of boxes
  - K is the total number of keys across all boxes
- Space Complexity: O(N)
  - We store visited boxes and keys in sets/lists

## Usage
```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

## Examples
```python
# Example 1: All boxes can be opened
boxes = [[1], [2], [3], [4], []]
# Returns: True

# Example 2: All boxes can be opened (multiple keys)
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# Returns: True

# Example 3: Not all boxes can be opened
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# Returns: False
```

## Author
Mohammed Elgaily
