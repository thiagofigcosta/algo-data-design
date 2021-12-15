import sys

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
    D = int(timestamp_ms / 1000 / 60 / 60 / 24)
    H = int(timestamp_ms / 1000 / 60 / 60 % 24)
    M = int(timestamp_ms / 1000 / 60 % 60)
    S = int(timestamp_ms / 1000 % 60)
    MS = int(timestamp_ms % 1000)
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
