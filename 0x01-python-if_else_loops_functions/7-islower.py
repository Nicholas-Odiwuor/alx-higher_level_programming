def islower(c):
    """
    Checks if the character c is lowercase.

    Args:
    - c: a character (string of length 1)

    Returns:
    - True if c is lowercase
    - False otherwise
    """
    # Check if the ASCII value of the character is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Test the function
print(islower('a'))  # True
print(islower('B'))  # False
print(islower('3'))  # False

