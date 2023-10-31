#!/usr/bin/python3
# 100-matrix_mul.py
def matrix_mul(num_a, num_b):
    
    if num_a == [] or num_a == [[]]:
        raise ValueError("num_a can't be empty")
    if num_b == [] or num_b == [[]]:
        raise ValueError("num_b can't be empty")

    if not isinstance(num_a, list):
        raise TypeError("num_a must be a list")
    if not isinstance(num_b, list):
        raise TypeError("num_b must be a list")

    if not all(isinstance(row, list) for row in num_a):
        raise TypeError("num_a must be a list of lists")
    if not all(isinstance(row, list) for row in num_b):
        raise TypeError("num_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in num_a for num in row]):
        raise TypeError("num_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in num_b for num in row]):
        raise TypeError("num_b should contain only integers or floats")

    if not all(len(row) == len(num_a[0]) for row in num_a):
        raise TypeError("each row of num_a must should be of the same size")
    if not all(len(row) == len(num_b[0]) for row in num_b):
        raise TypeError("each row of num_b must should be of the same size")

    if len(num_a[0]) != len(num_b):
        raise ValueError("num_a and num_b can't be multiplied")

    inverted_b = []
    for r in range(len(num_b[0])):
        n_row = []
        for c in range(len(num_b)):
            n_row.append(num_b[c][r])
        inverted_b.append(n_row)

    new_matrix = []
    for row in num_a:
        n_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            n_row.append(prod)
        new_matrix.append(n_row)

    return new_matrix
