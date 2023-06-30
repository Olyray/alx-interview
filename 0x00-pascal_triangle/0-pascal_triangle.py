#!/usr/bin/python3
"""A function that returns the Pascal's triangle of a number"""


def pascal_triangle(n):
    if n <= 0:
        return []
    # Create the double array for the triangle with 1 already included
    triangle = [[1]]
    # For loop from 1 to n:
    for i in range(1, n):
        # Create an array with 1 already included
        new_array = [1]
        # Create another array that is the last array of the triangle array
        previous_array = triangle[-1]
        # For loop from 1 to i:
        for j in range(1, i):
            # Append temp array [j - 1] plus temp array [j]
            new_array.append(previous_array[j - 1] + previous_array[j])
        # Add 1 to the end of the temp array
        new_array.append(1)
        # Add the temp array to the triangle
        triangle.append(new_array)
    # Return the triangle
    return triangle
