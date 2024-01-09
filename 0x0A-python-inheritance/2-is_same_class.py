#!/usr/bin/python3
"""This function returns True if the object is exactly an instance of the specified class"""
def is_same_class(obj, a_class):
    """If condition block"""
    if type(obj) == a_class:
        """
        Returns:
        True if the object is exactly an instance of the specified class
        otherwise: False
        """
        return True
    else:
        return False
