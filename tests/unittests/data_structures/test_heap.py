import unittest

import algo_data_design.utils.list as u_list
from algo_data_design.data_structures import heap


class HeapTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass  # nothing to create

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_max_heap_build(self, *args, **kwargs):
        array = u_list.random_int_list(500, 0, 1000)
        heap.build_max_heap(array)

        for p in range(len(array) // 2):
            l, r = heap.get_node_children_index(p, len(array))
            if l is not None:
                self.assertTrue(array[p] >= array[l], msg=f'Left child `{array[l]}` at position `{l}` is greater than '
                                                          f'its parent `{array[p]}` position `{p}`')
            if r is not None:
                self.assertTrue(array[p] >= array[r], msg=f'Right child `{array[r]}` at position `{r}` is greater than '
                                                          f'its parent `{array[p]}` position `{p}`')

    def test_min_heap_build(self, *args, **kwargs):
        array = u_list.random_int_list(500, 0, 1000)
        heap.build_min_heap(array)

        for p in range(len(array) // 2):
            l, r = heap.get_node_children_index(p, len(array))
            if l is not None:
                self.assertTrue(array[p] <= array[l], msg=f'Left child `{array[l]}` at position `{l}` is lower than '
                                                          f'its parent `{array[p]}` position `{p}`')
            if r is not None:
                self.assertTrue(array[p] <= array[r], msg=f'Right child `{array[r]}` at position `{r}` is lower than '
                                                          f'its parent `{array[p]}` position `{p}`')


if __name__ == '__main__':
    unittest.main()
