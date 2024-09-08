#!/usr/bin/python3
"""contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    writes the text to the file and 
    return the number of characters written
    """
    with open(filename, mode = "w", encoding="utf-8") as f:
        f.write(text)
