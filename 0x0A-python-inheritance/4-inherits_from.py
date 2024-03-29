#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class 
"""
def inherits_from(obj, a_class):

    """
    Args:

    obj = object of the class to check
    a_class = the specified class

    Returns:

    True if the object is an instance of a class
    otherwise:
    False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
