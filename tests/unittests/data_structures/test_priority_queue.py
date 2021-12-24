import unittest

from algo_data_design.data_structures import PriorityQueue


class QueueTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def tearDown(self, *args, **kwargs):
        pass

    def test_append_pop_len_unlimited_size(self, *args, **kwargs):
        q = PriorityQueue()
        self.assertEqual(0, len(q))
        q.append(10)
        self.assertEqual(1, len(q))
        q.append(20)
        q.append(30)
        self.assertEqual(3, len(q))
        self.assertEqual(10, q.pop())
        self.assertEqual(2, len(q))
        self.assertFalse(q.is_full())

        q = PriorityQueue()
        self.assertEqual(0, len(q))
        q.append(10, 1)
        self.assertEqual(1, len(q))
        q.append(20, 1)
        q.append(30, 0)
        self.assertEqual(3, len(q))
        self.assertEqual(30, q.pop())
        self.assertEqual(2, len(q))
        self.assertFalse(q.is_full())
        self.assertEqual(10, q.pop())
        self.assertEqual(20, q.pop())


if __name__ == '__main__':
    unittest.main()
