#!/usr/bin/python3

"""A class module"""

class BaseGeometry:

    """Public instance method the message area() is not implemented"""
    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")
        """Public instance method:that validates"""
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        """The if condition"""
        if type(value) != int:

            """raise TypeError"""
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            """Raise ValueError"""
            raise ValueError("{} must be greater than 0".format(value))
