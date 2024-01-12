def uppercase(s):
    for char in s:
        print(chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char, end="")
    print()

# Test the function
uppercase("Hello, World!")

