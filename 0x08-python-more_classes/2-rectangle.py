#!/usr/bin/python3
""""Defines a Rectangle class"""


class Rectangle:
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation of the size of the Rectangle

        Args:
            width: the width of the Rectangle
            height: the height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the value of the width

        Returns:
            int the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width of the rectangle
        Args:
            value (int): value to be assigned to the width of the rectangle

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of the height

        Returns:
            int the value of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height of the rectangle
        Args:
            value (int): value to be assigned to the height of the rectangle

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function returning the area of a rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__weight * self.__height

    def perimeter(self):
        """Function returning the perimeter of a rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__weight == 0 or self.__height == 0:
            return 0
        return (self.__weight * 2) + (self.__height * 2)
