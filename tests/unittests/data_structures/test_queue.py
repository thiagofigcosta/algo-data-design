import unittest

from algo_data_design.data_structures import Queue


class QueueTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_append_pop_len_unlimited_size(self, *args, **kwargs):
        q = Queue()
        self.assertEqual(0, len(q))
        q.append(10)
        self.assertEqual(1, len(q))
        q.append(20)
        q.append(30)
        self.assertEqual(3, len(q))
        self.assertEqual(10, q.pop())
        self.assertEqual(2, len(q))
        self.assertFalse(q.is_full())

    def test_append_pop_len_limited_size(self, *args, **kwargs):
        q = Queue(size_limit=2)
        self.assertEqual(0, len(q))
        q.append(10)
        self.assertEqual(1, len(q))
        q.append(20)
        q.append(30)  # will be ignored
        self.assertEqual(2, len(q))
        self.assertEqual(10, q.pop())
        self.assertEqual(1, len(q))
        self.assertFalse(q.is_full())
        q.append(30)
        self.assertTrue(q.is_full())


if __name__ == '__main__':
    unittest.main()
