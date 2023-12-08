#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            # Print non-letter characters as they are
            print("{}".format(char), end="")
    print()  # Print a newline after the loop
