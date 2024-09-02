#!/usr/bin/python3
"""
Defines a class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Retangle(BaseGeometry):
    """A Rectangle class - subclass of BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of Rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
