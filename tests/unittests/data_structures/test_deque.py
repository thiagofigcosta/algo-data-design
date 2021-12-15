import unittest

from algo_data_design.data_structures import Deque


class DequeTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_push_pop_len_unlimited_size(self, *args, **kwargs):
        d = Deque()
        self.assertEqual(0, len(d))
        d.push_back(10)
        self.assertEqual(1, len(d))
        d.push_back(20)
        d.push_back(30)
        self.assertEqual(3, len(d))
        self.assertEqual(10, d.pop_front())
        self.assertEqual(2, len(d))
        self.assertFalse(d.is_full())
        self.assertEqual(30, d.pop_back())

        d = Deque()
        self.assertEqual(0, len(d))
        d.push_front(10)
        self.assertEqual(1, len(d))
        d.push_front(20)
        d.push_front(30)
        self.assertEqual(3, len(d))
        self.assertEqual(30, d.pop_front())
        self.assertEqual(2, len(d))
        self.assertFalse(d.is_full())
        self.assertEqual(10, d.pop_back())

    def test_push_pop_len_limited_size(self, *args, **kwargs):
        d = Deque(2)
        self.assertEqual(0, len(d))
        d.push_back(10)
        self.assertEqual(1, len(d))
        d.push_back(20)
        d.push_back(30)  # will be ignored
        self.assertEqual(2, len(d))
        self.assertEqual(10, d.pop_front())
        self.assertEqual(1, len(d))
        self.assertFalse(d.is_full())
        self.assertEqual(20, d.pop_back())
        d.push_front(30)
        d.push_front(30)
        self.assertTrue(d.is_full())

        d = Deque(2)
        self.assertEqual(0, len(d))
        d.push_front(10)
        self.assertEqual(1, len(d))
        d.push_front(20)
        d.push_front(30)  # will be ignored
        self.assertEqual(2, len(d))
        self.assertEqual(20, d.pop_front())
        self.assertEqual(1, len(d))
        self.assertFalse(d.is_full())
        self.assertEqual(10, d.pop_back())
        d.push_front(30)
        d.push_front(30)
        self.assertTrue(d.is_full())


if __name__ == '__main__':
    unittest.main()
