#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = max(list(a_dictionary.values()))
        for index in a_dictionary:
            if a_dictionary[index] == best_score:
                return index
    return None
