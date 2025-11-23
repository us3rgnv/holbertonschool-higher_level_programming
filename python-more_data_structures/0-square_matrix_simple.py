#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers of a 2D matrix.

    Args:
        matrix (list of list of int): 2D matrix of integers

    Returns:
        list of list of int: new matrix with squared values
    """
    return [[x ** 2 for x in row] for row in matrix]
