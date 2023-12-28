#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary[key].update()
    if key in a_dictionary:
        new_dict[key] = value
    else:
        a_dictionary[key] = value
    return new_dict

