#!/usr/bin/python3
"""Defines a class named square."""


class Square():
    """A class named Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with the size of the Square

        Args:
            size (int): the size of the Square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """"Gets the position

        Returns:
            tuple: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position

        Args:
            value (tuple): the position

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print('#', end='') for j in range(0, self.__size)]
                print()
