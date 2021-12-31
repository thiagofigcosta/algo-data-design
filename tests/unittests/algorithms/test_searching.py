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
        def __run_a_star(_original_grid, _expected_grid_str, _expected_path, _expected_path_cost, _heuristic):
            _grid = [x[:] for x in _original_grid]  # copy 2d matrix
            path, cost = searching.a_star_grid_search(_grid, starting_point, goal_point, heuristic=_heuristic)
            for y, x in path[1:-1]:  # writing the path on the matrix
                _grid[y][x] = 4
            actual_matrix_str = ''
            for row in _grid:  # matrix to string
                actual_matrix_str += ', '.join([str(c) for c in row]) + '\n'
            self.assertEqual(_expected_grid_str, actual_matrix_str)
            self.assertEqual(_expected_path, path)
            self.assertAlmostEqual(_expected_path_cost, cost, 4)
            pass

        original_grid = []  # 0 = obstacle, 1 = path, 2 = start, 3 = goal, 4 = a* path
        starting_point = (0, 0)
        original_grid.append([2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1])
        original_grid.append([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])
        original_grid.append([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1])
        original_grid.append([1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1])
        original_grid.append([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
        original_grid.append([1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        original_grid.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3])
        goal_point = (len(original_grid) - 1, len(original_grid[0]) - 1)
        # EUCLIDEAN_DISTANCE
        heuristic = searching.AStarHeuristic.Type.EUCLIDEAN_DISTANCE
        expected_matrix_str_euclidean = '2, 4, 4, 4, 4, 1, 1, 1, 1, 1, 0, 1\n1, 1, 1, 1, 0, 4, 4, 1, 1, 1, 1, 1\n' \
                                        '1, 1, 1, 1, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n' \
                                        '1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n' \
                                        '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path_euclidean = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (2, 7), (3, 8), (4, 9),
                                   (5, 10), (6, 11)]
        expected_path_cost_euclidean = 13.48528137422
        __run_a_star(original_grid, expected_matrix_str_euclidean, expected_path_euclidean,
                     expected_path_cost_euclidean, heuristic)

        # MANHATTAN_DISTANCE
        heuristic = searching.AStarHeuristic.Type.MANHATTAN_DISTANCE
        expected_matrix_str_manhattan = '2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1\n4, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1\n' \
                                        '4, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1\n4, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1\n' \
                                        '1, 4, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1\n1, 4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1\n' \
                                        '1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3\n'
        expected_path_manhattan = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 1), (5, 1), (6, 2), (6, 3), (6, 4), (6, 5),
                                   (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11)]
        expected_path_cost_manhattan = 15.82842712474
        __run_a_star(original_grid, expected_matrix_str_manhattan, expected_path_manhattan,
                     expected_path_cost_manhattan, heuristic)

        # CHEBYSHEV_DISTANCE
        heuristic = searching.AStarHeuristic.Type.CHEBYSHEV_DISTANCE
        expected_matrix_str_chebyshev = '2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 0, 1\n1, 1, 1, 1, 0, 1, 4, 1, 1, 1, 1, 1\n' \
                                        '1, 1, 1, 1, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n' \
                                        '1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n' \
                                        '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path_chebyshev = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
                                   (5, 10), (6, 11)]
        expected_path_cost_chebyshev = 13.48528137422
        __run_a_star(original_grid, expected_matrix_str_chebyshev, expected_path_chebyshev,
                     expected_path_cost_chebyshev, heuristic)

        # DIAGONAL_DISTANCE
        heuristic = searching.AStarHeuristic.Type.DIAGONAL_DISTANCE
        expected_matrix_str_diagonal = '2, 4, 4, 4, 4, 1, 1, 1, 1, 1, 0, 1\n1, 1, 1, 1, 0, 4, 4, 1, 1, 1, 1, 1\n' \
                                       '1, 1, 1, 1, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n' \
                                       '1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n' \
                                       '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path_diagonal = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6), (2, 7), (3, 8), (4, 9),
                                  (5, 10), (6, 11)]
        expected_path_cost_diagonal = 13.48528137422
        __run_a_star(original_grid, expected_matrix_str_diagonal, expected_path_diagonal,
                     expected_path_cost_diagonal, heuristic)

        # COSINE_DISTANCE
        heuristic = searching.AStarHeuristic.Type.COSINE_DISTANCE
        expected_matrix_str_cosine = '2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 0, 1\n1, 1, 1, 1, 0, 1, 4, 1, 1, 1, 1, 1\n' \
                                     '1, 1, 1, 1, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n' \
                                     '1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n' \
                                     '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path_cosine = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10),
                                (6, 11)]
        expected_path_cost_cosine = 13.48528137422
        __run_a_star(original_grid, expected_matrix_str_cosine, expected_path_cosine,
                     expected_path_cost_cosine, heuristic)

        # DIJKSTRA
        heuristic = searching.AStarHeuristic.Type.DIJKSTRA
        expected_matrix_str_dijkstra = '2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 0, 1\n1, 1, 1, 1, 0, 1, 4, 1, 1, 1, 1, 1\n' \
                                       '1, 1, 1, 1, 0, 1, 0, 4, 1, 1, 1, 1\n1, 0, 0, 0, 0, 1, 1, 1, 4, 0, 1, 1\n' \
                                       '1, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 1\n1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1\n' \
                                       '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3\n'
        expected_path_dijkstra = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
                                  (5, 10), (6, 11)]
        expected_path_cost_dijkstra = 13.48528137422
        __run_a_star(original_grid, expected_matrix_str_dijkstra, expected_path_dijkstra, expected_path_cost_dijkstra,
                     heuristic)


if __name__ == '__main__':
    unittest.main()
