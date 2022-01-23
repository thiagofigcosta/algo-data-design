import unittest

from algo_data_design.algorithms import hashing


class HashingTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        pass  # nothing to create

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_hashing(self, *args, **kwargs):
        for i in range(1, 10000, 102):
            self.assertNotEqual(i, hashing.hash_triple(i))
            self.assertNotEqual(i, hashing.hash_multiplication(i))
            self.assertNotEqual(i, hashing.hash_7_shifts(i))
            self.assertNotEqual(i, hashing.hash_6_shifts(i))
            self.assertNotEqual(i, hashing.hash_6_shifts_low_bits(i))
            self.assertNotEqual(i, hashing.hash_5_shifts(i))
            self.assertEqual(i, hashing.hash_python(i))

        self.assertEqual(0, hashing.hash_triple(0))
        self.assertEqual(346819217770, hashing.hash_multiplication(0))
        self.assertEqual(0, hashing.hash_7_shifts(0))
        self.assertEqual(475834520164647, hashing.hash_6_shifts(0))
        self.assertEqual(0, hashing.hash_6_shifts_low_bits(0))
        self.assertEqual(6423398149250361, hashing.hash_5_shifts(0))
        self.assertEqual(0, hashing.hash_python(0))


if __name__ == '__main__':
    unittest.main()
