#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for mul in a_dictionary:
        new_dict[mul] = a_dictionary[mul] * 2
    return new_dict
