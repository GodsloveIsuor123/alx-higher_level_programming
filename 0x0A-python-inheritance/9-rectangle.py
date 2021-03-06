#!/usr/bin/python3
"""
Define a rectagle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    init rectangle objects.
    """
    def __init__(self, width, height):
        """
        Init object attributes.

        Args:
            width (int): integer number greater than zero
            height (int): integer number greater than zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of a rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Printable object.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

