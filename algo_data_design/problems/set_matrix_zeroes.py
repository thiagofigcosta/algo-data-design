import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Set matrix zeros")
    print("Given a 2D matrix set inplace to zero the rows and columns of cells that has zero as value")
    print("Examples:")
    print('\t[[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]')
    print('\t[[0,1,2,0],[3,4,5,2],[1,3,1,5]] -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]')


def run(matrix):
    # Time complexity: O(n*m)
    # Space complexity: O(n+m)
    rows_set = set()
    cols_set = set()
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell == 0:
                rows_set.add(r)
                cols_set.add(c)
    for row in rows_set:
        for c in range(len(matrix[row])):
            matrix[row][c] = 0
    for col in cols_set:
        for r in range(len(matrix)):
            matrix[r][col] = 0
    return matrix  # Can return None since the mod is in place, I'm turning


def main():
    info()
    test.assertEqual([[1, 0, 1], [0, 0, 0], [1, 0, 1]], run([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    test.assertEqual([[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], run([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
