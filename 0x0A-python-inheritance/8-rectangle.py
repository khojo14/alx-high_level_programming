#!/usr/bin/python3
"""
Defines a class
"""


class Retangle(BaseGeometry):
    """A Rectangle class - subclass of BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator(width)
        self.__width = width
        super().integer_validator(height)
        self.__height = height
