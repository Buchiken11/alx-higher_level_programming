#!/usr/bin/python3
def remove_char_at(str, n):
    new_chr = ""
    i = 0
    for character in str:
        if i != n:
            new_chr += character
            i = i + 1
            return (new_chr)
