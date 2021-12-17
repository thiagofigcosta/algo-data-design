import unittest

from algo_data_design.data_structures import RingBuffer


class RingBufferTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_ring_buffer_behavior(self, *args, **kwargs):
        rb = RingBuffer(3)
        self.assertEqual(0, len(rb))
        rb.append(0)
        self.assertEqual(1, len(rb))
        rb.append(1)
        rb.append(2)
        self.assertEqual(3, len(rb))
        self.assertEqual(0, rb.pop())
        self.assertEqual(2, len(rb))
        self.assertEqual(1, rb.pop())
        self.assertEqual(1, len(rb))
        self.assertEqual(2, rb.pop())
        self.assertEqual(0, len(rb))
        for el in range(6):
            rb.append(el)
        self.assertEqual(3, len(rb))
        for el in range(3, 6, 1):
            self.assertEqual(el, rb.pop())
        self.assertEqual(0, len(rb))

    def test_ring_read_before_insert(self, *args, **kwargs):
        rb = RingBuffer(3)
        self.assertRaises(Exception, rb.pop)

    def test_ring_no_override(self, *args, **kwargs):
        rb = RingBuffer(3)
        for el in range(6):
            rb.append(el, override=False)
        self.assertEqual(3, len(rb))
        for el in range(3):
            self.assertEqual(el, rb.pop())
        self.assertEqual(0, len(rb))


if __name__ == '__main__':
    unittest.main()
