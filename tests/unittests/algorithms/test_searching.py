import unittest

from algorithms import searching


class SearchingTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
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


if __name__ == '__main__':
    unittest.main()
