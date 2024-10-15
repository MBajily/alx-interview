# Minimum Operations

## Description
This project contains a Python function that calculates the fewest number of operations needed to result in exactly n 'H' characters in a text file. The text editor can execute only two operations: Copy All and Paste.

## Problem Statement
Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n 'H' characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If n is impossible to achieve, return 0

## Example
```python
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```

## Implementation
The solution is implemented in the file `0-minoperations.py`. It uses the concept of prime factorization to efficiently calculate the minimum number of operations.

### Algorithm
1. If n is less than or equal to 1, return 0 (no operations needed).
2. Initialize a variable to keep track of the total operations.
3. Start with the smallest prime number (2) as the divisor.
4. While n is greater than 1:
   - If n is divisible by the current divisor:
     - Add the divisor to the total operations.
     - Divide n by the divisor.
   - If n is not divisible by the divisor, increment the divisor.
5. Return the total number of operations.

## Usage
To use this function, import it into your Python script:

```python
from 0-minoperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## File Structure
- `0-minoperations.py`: Contains the implementation of the `minOperations` function.
- `0-main.py`: Main file for testing the function.

## Author
Mohammed Elgaily
