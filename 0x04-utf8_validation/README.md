# UTF-8 Validation

## Overview
This project contains a Python implementation of a UTF-8 validator. The validator determines if a given data set represents a valid UTF-8 encoding.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Files
- `0-validate_utf8.py`: Contains the implementation of the UTF-8 validation function
- `0-main.py`: Main file for testing the implementation

## Function Description
```python
def validUTF8(data)
```
This function determines if a given data set represents a valid UTF-8 encoding.

### Parameters
- `data`: List of integers where each integer represents 1 byte of data

### Returns
- `True` if data is a valid UTF-8 encoding
- `False` otherwise

### UTF-8 Encoding Rules
- A character in UTF-8 can be 1 to 4 bytes long
- For 1-byte characters: First bit is 0 (0xxxxxxx)
- For n-byte characters (n > 1):
  * First byte starts with n ones followed by a 0 (110xxxxx for 2 bytes)
  * Continuation bytes start with 10 (10xxxxxx)

## Usage
```bash
# Make the file executable
chmod +x 0-main.py

# Run the tests
./0-main.py
```

## Example
```python
# Test with simple ASCII character
data = [65]
print(validUTF8(data))  # Output: True

# Test with multiple ASCII characters
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

# Test with invalid UTF-8 encoding
data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Author
Mohammed Elgaily

