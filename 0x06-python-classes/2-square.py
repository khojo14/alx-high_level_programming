#!/usr/bin/python3
"""Defines a class named square"""


class Square():
    """A class named Square"""
    def __init__(self, size=0):
        """Instantiation with the size of the Square

        Args:
            param1: the size of the Square

        Raises:
            TypeError: if size is not and int
            ValueError: is size < 0
        """
        try:
            self.__size = size
            if not size:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
