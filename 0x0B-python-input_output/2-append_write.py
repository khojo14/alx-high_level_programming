#!/usr/bin/python3
"""
contains a function that appends a
string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends the text to the video"""
    with open(filname, "w", encoding="utf-8") as a_file:
        return a_file.append(text)
