import unittest

import algo_data_design.utils.list as u_list


class ListTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass  # nothing to create

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_swap_elements(self, *args, **kwargs):
        a_list = [1, 2, 3]
        a_list_2 = a_list.copy()
        u_list.swap_elements(a_list, 0, len(a_list) - 1)
        self.assertEqual(a_list[0], a_list_2[-1])
        self.assertEqual(a_list[-1], a_list_2[0])


if __name__ == '__main__':
    unittest.main()
