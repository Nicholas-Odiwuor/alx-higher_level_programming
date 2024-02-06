# Python Input/Output

## Description

This project contains a Python function called `read_file` that reads a text file (UTF-8 encoded) and prints its contents to stdout.

## Function Documentation

The `read_file` function has the following signature:

```python
def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoded) and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

