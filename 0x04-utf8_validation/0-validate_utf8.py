#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: List of integers where each integer represents 1 byte of data

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the binary representation of the least significant 8 bits
        byte = num & 0xFF

        # If we are not currently in a UTF-8 character
        if n_bytes == 0:
            # Get the number of 1s in the most significant bits
            # to determine the number of bytes in the UTF-8 character
            if byte >> 7 == 0:  # 1 byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:  # 2 byte character (110xxxxx)
                n_bytes = 1
            elif byte >> 4 == 0b1110:  # 3 byte character (1110xxxx)
                n_bytes = 2
            elif byte >> 3 == 0b11110:  # 4 byte character (11110xxx)
                n_bytes = 3
            else:  # Invalid UTF-8 start byte
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    # Check if we've processed all expected bytes
    return n_bytes == 0
