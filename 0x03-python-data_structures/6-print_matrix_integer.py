#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    [[row[i] for row in matrix] for i in range(3)]
    print("{}".format(i))
=======
    for i in matrix:
        print(''.join('{:d}'.format(j)for j in i))
>>>>>>> origin/main
