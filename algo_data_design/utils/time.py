import sys
import time as time_lib

from algo_data_design.utils import random as u_random

try:  # if Python >= 3.3 uses the new high-res counter and keep running even when thread sleeps
    from time import perf_counter as _time_time
except ImportError:  # else select highest available resolution counter
    if sys.platform[:3] == 'win':
        from time import clock as _time_time
    else:
        from time import time as _time_time


def time():
    return _time_time()


def delta(previous_time):
    return _time_time() - previous_time


def timestamp_to_human_readable_str(timestamp, seconds=True):
    if seconds:
        timestamp_ms = timestamp * 1000
    else:
        timestamp_ms = timestamp
    timestamp_ms = int(timestamp_ms)
    tmp1 = timestamp_ms // 1000
    tmp2 = tmp1 // 60
    tmp3 = tmp2 // 60
    D = tmp3 // 24
    H = tmp3 % 24
    M = tmp2 % 60
    S = tmp1 % 60
    MS = timestamp_ms % 1000
    out = '' if timestamp_ms > 0 else 'FINISHED'
    if D > 0:
        out += '{} days '.format(D)
    if D > 0 and MS == 0 and S == 0 and M == 0 and H > 0:
        out += 'and '
    if H > 0:
        out += '{} hours '.format(H)
    if (D > 0 or H > 0) and MS == 0 and S == 0 and M > 0:
        out += 'and '
    if M > 0:
        out += '{} minutes '.format(M)
    if (D > 0 or H > 0 or M > 0) and MS == 0 and S > 0:
        out += 'and '
    if S > 0:
        out += '{} seconds '.format(S)
    if (D > 0 or H > 0 or M > 0 or S > 0) and MS > 0:
        out += 'and '
    if MS > 0:
        out += '{} milliseconds '.format(MS)
    return out


def exponential_backoff(cur_retry, max_attempts, backoff_in_secs):
    # cur_retry starts with zero
    if cur_retry < max_attempts:
        exponential_delay = (2 ** cur_retry) * backoff_in_secs
        random_delay = u_random.random_float()
        time_lib.sleep(exponential_delay + random_delay)
    else:
        raise Exception(f'Too many retries (`{max_attempts}`)')
    cur_retry += 1
    return cur_retry
