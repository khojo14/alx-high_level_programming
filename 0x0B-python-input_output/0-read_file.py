#!/usr/bin/python3
"""Contains a function to read file"""


def read_file(filename=""):
    """Takes a file and reads out its content"""
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
