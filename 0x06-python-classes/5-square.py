#!/usr/bin/python3
"""Defines a class named square."""


class Square():
    """A class named Square."""

    def __init__(self, size=0):
        """Instantiation with the size of the Square

        Args:
            size (int): the size of the Square
        """
        self.size = size

    @property
    def size(self):
        """"Gets the value of the square

        Returns:
            int the value of the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square
        Args:
            value (int): value tobe assigned to the size of the square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function returning the area of a square

        Returns:
            int: the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
