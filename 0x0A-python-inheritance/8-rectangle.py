#!/usr/bin/python3
"""
Defines a subclass of  the class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle class"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
