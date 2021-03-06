#!/usr/bin/python3
"""
Define Geometry class.
"""


class BaseGeometry:
    """
    create object BaseGeometry
    """

    def integer_validator(self, name, value):
        """
        Parameter valitors.
        Args:
            name (str): name
            value (int): integer number.
        Return:
            None.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        Raise a exception.
        """
        raise Exception("area() is not implemented")
