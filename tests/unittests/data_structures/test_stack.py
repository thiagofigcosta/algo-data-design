import unittest

from algo_data_design.data_structures import Stack


class StackTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_append_pop_len_unlimited_size(self, *args, **kwargs):
        s = Stack()
        self.assertEqual(0, len(s))
        s.append(10)
        self.assertEqual(1, len(s))
        s.append(20)
        s.append(30)
        self.assertEqual(3, len(s))
        self.assertEqual(30, s.pop())
        self.assertEqual(2, len(s))
        self.assertFalse(s.is_full())

    def test_append_pop_len_limited_size(self, *args, **kwargs):
        s = Stack(size_limit=2)
        self.assertEqual(0, len(s))
        s.append(10)
        self.assertEqual(1, len(s))
        s.append(20)
        s.append(30)  # will be ignored
        self.assertEqual(2, len(s))
        self.assertEqual(20, s.pop())
        self.assertEqual(1, len(s))
        self.assertFalse(s.is_full())
        s.append(30)
        self.assertTrue(s.is_full())


if __name__ == '__main__':
    unittest.main()
