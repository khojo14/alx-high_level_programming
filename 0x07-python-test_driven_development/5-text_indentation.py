#!/usr/bin/python3
"""
This is the 5-text-indentation module.
This module supplies on function, text_indentation()
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True

    for i in text:
        if i == ' ' and skip_space:
            continue
        elif i in ':?.':
            print(i)
            print()
            skip_space = True
        else:
            print(i, end="")
            skip_space = False
