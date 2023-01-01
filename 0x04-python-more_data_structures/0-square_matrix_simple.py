#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for line in matrix:
        square = map(lambda x: x * x, line)
        result.append(list(square))

    return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    new_matrix = square_matrix_simple(matrix)
    print(matrix)
    print(new_matrix)
