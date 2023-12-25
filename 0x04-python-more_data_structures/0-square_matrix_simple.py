#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Step 1: Initialize an empty result matrix
    result_matrix = []

    # Step 2: Iterate over each row in the input matrix
    for i in matrix:
        # Step 3: Initialize an empty list for the current row in the result matrix
        squared_row = []

        # Step 4: Iterate over each element in the current row
        for element in i:
            # Step 5: Square each element and append to the current row
            squared_element = element ** 2
            squared_row.append(squared_element)

        # Step 6: Append the current row to the result matrix
        result_matrix.append(squared_row)

    # Step 8: Return the result matrix
    return result_matrix
