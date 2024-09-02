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
    
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a description"""
        return str([Rectangle] self.__width/self.__height)
