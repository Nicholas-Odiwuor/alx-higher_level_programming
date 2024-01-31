#!/usr/bin/python3
"""
Module for max_integer
"""


def max_integer(list=[]):
    """
    Finds the maximum integer in a list of integers.

    Args:
        list (list): The list of integers.

    Returns:
        int: The maximum integer.

    """
    if not list:
        return None
    max_int = list[0]
    for num in list:
        if num > max_int:
            max_int = num
    return max_int

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/6-max_integer_test.txt")

