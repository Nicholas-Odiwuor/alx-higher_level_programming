Description
This project includes implementations in both Python and C for a function that prints all integers of a given list. The Python scripts are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5, and the C files are compiled on the same platform using gcc.

Files and Structure
Python Scripts
print_list_integer.py: Python script containing the function print_list_integer that prints all integers in the given list, one integer per line.
C Scripts
print_list_integer.c: C file with the function print_list_integer that performs the same task as its Python counterpart.
Additional Files
lists.h: Header file containing the prototypes of functions used in the C scripts.
Coding Standards
Python scripts adhere to the PEP 8 style guide, checked using pycodestyle (version 2.8.*).
C scripts follow the Betty style, checked using betty-style.pl and betty-doc.pl.
No global variables are used in the C scripts.
Each C file contains no more than 5 functions.
Header files are include guarded.
Execution and Testing
All files must end with a new line.
The first line of all files is #!/usr/bin/python3 for Python scripts.
The first line of C files adheres to the Betty style.
All files must be executable.
