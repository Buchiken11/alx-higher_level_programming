#!/usr/bin/python3
"""This function that returns the list of available attributes and methods of an object"""
def lookup(obj):
    """
    Args:
    obj = class object
    Returns:
    list of object
    """
    return dir(obj)
