#!/usr/bin/python3

matrix = [

            [1, 2, 3, 4],

            [5, 6, 7, 8],

            [9, 10, 11, 12],

]
transpose_matrix = [[row[i] for row in matrix] for i in range(4)]
for row in transpose_matrix:
    print(*row)
