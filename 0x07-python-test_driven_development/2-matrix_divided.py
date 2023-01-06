#!/usr/bin/python3

"""
    Matrix division module
"""

def matrix_divided(matrix, div):
    """ Divides each value of a matrix by a number.
    Args:
        matrix: (:obj:`list` of :obj: `list`): The matrix to divide
        div: The divisor.
    Returns:
        (:obj:`list` of :obj: `list` of number): A divided matrix.
    Raises:
        TypeError: If `matrix` is not a ``matrix``.
                   If each row does not have the same time.
                   If `div` is not a number.
        ZeroDivisionError: If `div` is 0
    """
    if len(matrxi):
        n = len(matrix[0])
        for row in matrix:
            if n != len(row):
                raise TypeError(
                        "Each row of the matrix must have the same size")
            for i in row:
                if type(i) not in [int, float]:
                    raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
    res = [[round(i/div, 2) for i in row] for row in matrix]
    return res
