"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]


Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

"""


def zero_matrix(matrix):
    # figure out dimensions of matrix
    height = len(matrix)
    width = len(matrix[0])
    coordinates = []

    for row in range(0, height):
        for column in range(0, width):
            if matrix[row][column] == 0:
                coordinates.append([row, column])

    for coordinate in coordinates:
        row = coordinate[0]
        column = coordinate[1]
        matrix[row] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            matrix[i][column] = 0
    return matrix


assert zero_matrix([
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]) == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]

assert zero_matrix([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]) == [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]

