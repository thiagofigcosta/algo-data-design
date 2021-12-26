import unittest

import algo_data_design.problems


class ProblemsTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        algo_data_design.problems.NO_PROMPT = True

    def tearDown(self, *args, **kwargs):
        algo_data_design.problems.NO_PROMPT = False

    def test_all_problems(self, *args, **kwargs):
        algo_data_design.problems.run_problems()


if __name__ == '__main__':
    unittest.main()
