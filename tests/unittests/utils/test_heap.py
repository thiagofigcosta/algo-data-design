import unittest

import utils.heap as u_heap
import utils.list as u_list


class HeapTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_heap_build(self, *args, **kwargs):
        array = u_list.random_int_list(500, 0, 1000)
        u_heap.build_max_heap(array)

        for p in range(len(array) // 2):
            l, r = u_heap.get_node_children_index(p, len(array))
            if l is not None:
                self.assertTrue(array[p] >= array[l], msg=f'Left child `{array[l]}` at position `{l}` is greater than '
                                                          f'its parent `{array[p]}` position `{p}`')
            if r is not None:
                self.assertTrue(array[p] >= array[r], msg=f'Right child `{array[r]}` at position `{r}` is greater than '
                                                          f'its parent `{array[p]}` position `{p}`')


if __name__ == '__main__':
    unittest.main()
