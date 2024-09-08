#!/usr/bin/python3
"""
contains a function that appends a
string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends the text to the file"""
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
