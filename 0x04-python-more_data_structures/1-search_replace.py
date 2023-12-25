#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Initialize a new list
    new_list = []

    # Iterate over the elements in the input list
    for i in my_list:
        # Check for the element to be replaced
        if i == search:
            # Replace the element
            new_list.append(replace)
        else:
            # Keep the original element
            new_list.append(i)

    # Return the new list
    return new_list
