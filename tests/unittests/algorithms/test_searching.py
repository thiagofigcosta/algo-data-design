import unittest

from algo_data_design.algorithms import searching


class SearchingTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        pass

    def tearDown(self, *args, **kwargs):
        pass

    def test_linear_search_found(self, *args, **kwargs):
        array = [1, -2, 3, 4, -5, 6, 7, 8, -9, 0, 500, 2]
        to_find = -5
        expected_index = 4
        found_index = searching.linear_search(array, to_find)
        self.assertEqual(expected_index, found_index)

    def test_linear_search_not_found(self, *args, **kwargs):
        array = [1, -2, 3, 4, -5, 6, 7, 8, -9, 0, 500, 2]
        to_find = 666
        found_index = searching.linear_search(array, to_find)
        self.assertIsNone(found_index)

    def test_binary_search_found(self, *args, **kwargs):
        array = [-9, -5, -2, 0, 1, 2, 3, 4, 6, 7, 8, 500]
        to_find = -5
        expected_index = 1
        found_index = searching.binary_search(array, to_find)
        self.assertEqual(expected_index, found_index)

    def test_binary_search_not_found(self, *args, **kwargs):
        array = [-9, -5, -2, 0, 1, 2, 3, 4, 6, 7, 8, 500]
        to_find = 666
        found_index = searching.binary_search(array, to_find)
        self.assertIsNone(found_index)

    def test_ordered_search_found(self, *args, **kwargs):
        array = [-9, -5, -2, 0, 1, 2, 3, 4, 6, 7, 8, 500]
        to_find = -5
        expected_index = 1
        found_index = searching.ordered_search(array, to_find)
        self.assertEqual(expected_index, found_index)

    def test_ordered_search_not_found(self, *args, **kwargs):
        array = [-9, -5, -2, 0, 1, 2, 3, 4, 6, 7, 8, 500]
        to_find = 666
        found_index = searching.ordered_search(array, to_find)
        self.assertIsNone(found_index)

    def test_interpolation_search_found(self, *args, **kwargs):
        array = [-4, -3, -2, -1, 0, 1, 2, 6]
        to_find = -3
        expected_index = 1
        found_index = searching.interpolation_search(array, to_find)
        self.assertEqual(expected_index, found_index)

    def test_interpolation_search_not_found(self, *args, **kwargs):
        array = [-4, -3, -2, -1, 0, 1, 2, 6]
        to_find = 666
        found_index = searching.interpolation_search(array, to_find)
        self.assertIsNone(found_index)

    def test_jump_search_found(self, *args, **kwargs):
        array = [1, -2, 3, 4, -5, 6, 7, 8, -9, 0, 500, 2]
        to_find = -5
        expected_index = 4
        found_index = searching.jump_search(array, to_find)
        self.assertEqual(expected_index, found_index)

    def test_jump_search_not_found(self, *args, **kwargs):
        array = [1, -2, 3, 4, -5, 6, 7, 8, -9, 0, 500, 2]
        to_find = 666
        found_index = searching.jump_search(array, to_find)
        self.assertIsNone(found_index)

    def test_a_star_grid_search(self, *args, **kwargs):
        grid = []
        expected_matrix_str = '4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 0, 1\n1, 4, 1, 4, 0, 4, 4, 1, 1, 1, 1, 1\n1, 1, 4, 4, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path = [(0, 0), (1, 1), (2, 2), (2, 3), (1, 3), (0, 4), (1, 5), (1, 6), (2, 7), (3, 8), (4, 9),
                         (5, 10), (6, 11)]
        grid.append([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
        grid.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])
        grid.append([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1])
        grid.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1])
        grid.append([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
        grid.append([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        grid.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3])
        starting_point = (0, 0)
        goal_point = (len(grid) - 1, len(grid[0]) - 1)
        path = searching.a_star_grid_search(grid, starting_point, goal_point)
        for x, y in path[:-1]:  # writing the path on the matrix
            grid[x][y] = 4
        actual_matrix_str = ''
        for row in grid:  # matrix to string
            actual_matrix_str += ', '.join([str(c) for c in row]) + '\n'
        self.assertEqual(expected_matrix_str, actual_matrix_str)
        self.assertEqual(expected_path, path)


if __name__ == '__main__':
    unittest.main()
