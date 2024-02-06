# Object Lookup Function

## Description

This project contains a Python function called `lookup` which returns a list of available attributes and methods of an object.

## Usage

To use the `lookup` function, you can simply import it into your Python script and call it with an object as an argument. Here's an example:

```python
from object_lookup import lookup

class Example:
    def __init__(self):
        self.data = "example"
    def method(self):
        pass

obj = Example()
print(lookup(obj))

Function Documentation
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to look up attributes and methods for.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)

