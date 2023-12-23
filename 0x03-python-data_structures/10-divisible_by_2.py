#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        list_result = i % 2
        if list_result == 0:
            result.append(True)
        else:
            result.append(False)
    return result
