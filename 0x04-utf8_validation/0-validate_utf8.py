#!/usr/bin/env python3
"""A script to validate utf-8"""


def validUTF8(data):
    """The function to validate utf-8"""
    num_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the integer
        num = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes required to represent the character
            if num >> 7 == 0b0:         # 1-byte character (0xxxxxxx)
                num_bytes = 0
            elif num >> 5 == 0b110:    # 2-byte character (110xxxxx)
                num_bytes = 1
            elif num >> 4 == 0b1110:   # 3-byte character (1110xxxx)
                num_bytes = 2
            elif num >> 3 == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte (10xxxxxx)
            if num >> 6 != 0b10:
                return False

            num_bytes -= 1

    # If num_bytes is zero at the end, it means all characters were complete
    return num_bytes == 0
