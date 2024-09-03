#!/usr/bin/python3
"""
Defines a subclass of  the class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square class"""
    def __init__(self, size):
        """instantiation of the square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
