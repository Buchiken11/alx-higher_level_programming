#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print the sorted dictionary
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
