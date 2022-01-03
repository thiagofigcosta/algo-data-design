import unittest
from unittest import mock

import algo_data_design.utils.time as u_time
from algo_data_design.utils.test import call as tc, set_global_mocked_kwargs, clear_global_mocked_kwargs


class MockedTime(object):
    # A class to store the mocked functions in an organized way
    @staticmethod
    def sleep(*args, **kwargs):
        sleep_time = args[0]
        assert_time = kwargs.pop('assert_time', False)
        if assert_time:
            expected_sleep_time = kwargs.pop('time_to_assert', None)
            test = unittest.TestCase()
            test.assertEqual(expected_sleep_time, sleep_time)


class MockedRandom(object):
    # A class to store the mocked functions in an organized way
    @staticmethod
    def random(*args, **kwargs):
        random_value = kwargs.pop('random_value', None)
        if random_value is None:
            return 0.5
        else:
            return random_value


class TimeTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def tearDown(self, *args, **kwargs):
        pass

    @mock.patch('time.sleep', side_effect=tc(MockedTime.sleep, assert_time=True))
    @mock.patch('random.random', side_effect=tc(MockedRandom.random))
    def test_exponential_backoff(self, *args, **kwargs):
        max_tries = 3
        backoff_time = 1
        set_global_mocked_kwargs(time_to_assert=1.5)
        u_time.exponential_backoff(0, max_tries, backoff_time)
        set_global_mocked_kwargs(time_to_assert=2.5)
        u_time.exponential_backoff(1, max_tries, backoff_time)
        set_global_mocked_kwargs(time_to_assert=4.5)
        u_time.exponential_backoff(2, max_tries, backoff_time)
        set_global_mocked_kwargs(time_to_assert=1.5)
        self.assertRaises(Exception, u_time.exponential_backoff, 3, max_tries, backoff_time)
        clear_global_mocked_kwargs()


if __name__ == '__main__':
    unittest.main()
