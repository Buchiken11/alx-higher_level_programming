#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""a class Square that inherits from Rectangle (9-rectangle.py)"""
class Square(Rectangle):
    """instantiation with size: def __init__(self, size)
    Attribute:
    size = size of square
    """
    def __init__(self, size):
        """This initializes the instance with the number of arguments in the base class Rectangle

        size: Size of the square

        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
