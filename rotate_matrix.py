"""
Given an NxN matrix, rotate it by 90 degrees. You should perform this operation in-place, using only constant memory.

Example:
starting matrix:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
once rotated by 90 degrees, the matrix becomes:
 [
  [7, 4, 1]
  [8, 5, 2]
  [9, 6, 3]
]
"""

def rotate_matrix(matrix):
    print('before:')
    for row in matrix:
        print(row)

    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            print(f'swap {matrix[row][col]} with {matrix[col][row]}')
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    print('after:')
    for row in matrix:
        row.reverse()
        print(row)

    return matrix

matrix = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]

matrix2 = [
    [1,1,1,1,1,1,1,11],
    [2,2,2,2,2,2,2,22],
    [3,3,3,3,3,3,3,33],
    [4,4,4,4,4,4,4,44],
    [5,5,5,5,5,5,5,55],
    [6,6,6,6,6,6,6,66],
    [7,7,7,7,7,7,7,77],
    [8,8,8,8,8,8,8,88]
]

rotate_matrix(matrix)
rotate_matrix(matrix2)