#!/usr/bin/python3

def uppercase(str):
    for char in str:
        char_val = ord(char)
        if char_val > 96 and char_val < 123:
            char_val = char_val - 32
        print("{:s}".format(chr(char_val)), end="")
    print()
