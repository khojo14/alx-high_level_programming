#!/usr/bin/python3
"""Defines a class named square."""


class Square():
    """A class named Square."""


    def __init__(self, size=0):
        """Instantiation with the size of the Square

        Args:
            size (int): the size of the Square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isintance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
