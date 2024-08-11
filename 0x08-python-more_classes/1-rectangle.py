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
            value (int): value to be assigned to the width of the square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an integer")

    @property
    def height(self):
        """Gets the value of the height

        Returns:
            int the value of the height
        """
        return self.__width

    @height.setter
    def height(self, value):
        """Sets the value of the height of the rectangle
        Args:
            value (int): value to be assigned to the height of the square

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
