import unittest

import algorithms.sorting as sorting
import utils.list as u_list


class SortingTest(unittest.TestCase):
    TEST_SIZE = 800

    def setUp(self, *args, **kwargs):
        pass

    def test_intro_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE)
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_insertion_quick_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE)
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.quick_insertion_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_quick_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE)
        to_sort = expected.copy()
        for method in sorting.quick.PivotMethod.get_all_methods():
            u_list.shuffle_list(to_sort)
            sorting.quick_sort(to_sort, method)
            self.assertEqual(expected, to_sort)

    def test_bubble_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE)
        to_sort = expected.copy()
        for method in sorting.bubble.Method.get_all_methods():
            u_list.shuffle_list(to_sort)
            sorting.bubble_sort(to_sort, method)
            self.assertEqual(expected, to_sort)

    def test_swap_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE)
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.swap_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_counting_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.counting_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_heap_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.heap_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_insertion_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.insertion_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_shell_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.shell_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_merge_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.merge_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_radix_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.radix_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_selection_sort(self, *args, **kwargs):
        expected = u_list.sequential_int_list(SortingTest.TEST_SIZE, -(SortingTest.TEST_SIZE / 2))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.selection_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_bucket_sort(self, *args, **kwargs):
        expected = sorted(u_list.random_float_list(SortingTest.TEST_SIZE))
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.bucket_sort(to_sort)
        self.assertEqual(expected, to_sort)

    def test_bogo_sort(self, *args, **kwargs):
        patience_length = 6
        expected = u_list.sequential_int_list(patience_length)
        to_sort = expected.copy()
        u_list.shuffle_list(to_sort)
        sorting.stou_com_sort(to_sort)
        self.assertEqual(expected, to_sort)


if __name__ == '__main__':
    unittest.main()
