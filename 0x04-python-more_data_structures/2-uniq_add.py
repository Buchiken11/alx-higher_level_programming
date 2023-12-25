#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_add = set()
    for i in my_list:
        if i != my_list:
            new_add.add(i)
        else:
            print("all values are the same")
    return sum(new_add)
