# Pascal's Triangle

This project contains a Python implementation of Pascal's Triangle. The main function returns a representation of Pascal's Triangle based on a given number of rows.

## Description

Pascal's Triangle is a triangular array of the binomial coefficients. Each number is the sum of the two numbers directly above it.

Example of Pascal's Triangle with 5 rows:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

## Function Description

### `pascal_triangle(n)`

Returns a list of lists of integers representing Pascal's triangle of height `n`.

**Parameters:**
- `n`: Integer representing the number of rows to generate

**Returns:**
- If `n <= 0`: Returns an empty list
- Otherwise: Returns a list of lists representing Pascal's Triangle

**Example Usage:**
```python
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Test with n = 5
triangle = pascal_triangle(5)
print_triangle(triangle)
```

**Output:**
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Requirements
* Python 3.x
* All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files end with a new line
* First line of all files: `#!/usr/bin/python3`
* Code uses the pycodestyle style (version 2.8.*)
* All modules have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Files
* `0-pascal_triangle.py`: Contains the implementation of the pascal_triangle function
* `0-main.py`: Main file for testing the function

## License
This project is licensed under the terms of the MIT license.
