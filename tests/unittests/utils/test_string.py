import unittest

import algo_data_design.utils.string as u_string


class StringTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass  # nothing to create

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_strip_accents(self, *args, **kwargs):
        string = 'ìáé êãç'
        expected = 'iae eac'
        actual = u_string.strip_accents(string)
        self.assertEqual(expected, actual)
        string = 'iasjdiasjdaii'
        expected = 'iasjdiasjdaii'
        actual = u_string.strip_accents(string)
        self.assertEqual(expected, actual)

    def test_strip_non_alpha(self, *args, **kwargs):
        string = 'ìáé êãç!!!, doaskda 10'
        expected = 'ìáéêãçdoaskda10'
        actual = u_string.strip_non_alpha(string)
        self.assertEqual(expected, actual)

    def test_strip_non_alpha_non_space(self, *args, **kwargs):
        string = 'ìáé êãç!!!, doaskda 10'
        expected = 'ìáé êãç doaskda 10'
        actual = u_string.strip_non_alpha_or_non_space(string)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
