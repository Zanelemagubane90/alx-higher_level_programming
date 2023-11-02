#!/usr/bin/python3
# 2-matrix_divided.py
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(arow, list) for arow in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [anum for arow in matrix for anum in arow])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(arow) == len(matrix[0]) for arow in matrix):
        raise TypeError("Each arow of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda v: round(v / div, 2), arow)) for arow in matrix])
