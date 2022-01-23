import unittest

from algo_data_design.data_structures import PriorityQueue, PriorityQueueMethod


class PriorityQueueTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass  # nothing to create

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_append_pop_len_unlimited_size(self, *args, **kwargs):
        for method in PriorityQueueMethod.get_all_methods():
            q = PriorityQueue(method=method)
            self.assertEqual(0, len(q))
            q.append(10)
            self.assertEqual(1, len(q))
            q.append(20)
            q.append(30)
            self.assertEqual(3, len(q))
            self.assertEqual(10, q.pop())
            self.assertEqual(2, len(q))
            self.assertFalse(q.is_full())

            q = PriorityQueue(method=method)
            self.assertEqual(0, len(q))
            q.append(10, 1)
            self.assertEqual(1, len(q))
            q.append(20, 1)
            q.append(30, 0)
            self.assertEqual(3, len(q))
            self.assertEqual(30, q.pop())
            self.assertEqual(2, len(q))
            self.assertFalse(q.is_full())
            if method != PriorityQueueMethod.HEAP:  # the order of equal priorities is not guaranteed in heapq
                self.assertEqual(10, q.pop())
                self.assertEqual(20, q.pop())

    def test_append_pop_len_unlimited_size_max_queue(self, *args, **kwargs):
        for method in PriorityQueueMethod.get_all_methods():
            q = PriorityQueue(max_queue=True, method=method)
            self.assertEqual(0, len(q))
            q.append(10)
            self.assertEqual(1, len(q))
            q.append(20)
            q.append(30)
            self.assertEqual(3, len(q))
            self.assertEqual(10, q.pop())
            self.assertEqual(2, len(q))
            self.assertFalse(q.is_full())

            q = PriorityQueue(max_queue=True, method=method)
            self.assertEqual(0, len(q))
            q.append(10, 1)
            self.assertEqual(1, len(q))
            q.append(20, 1)
            q.append(30, 0)
            self.assertEqual(3, len(q))
            self.assertEqual(10, q.pop())
            self.assertEqual(2, len(q))
            self.assertFalse(q.is_full())
            self.assertEqual(20, q.pop())
            self.assertEqual(30, q.pop())


if __name__ == '__main__':
    unittest.main()
