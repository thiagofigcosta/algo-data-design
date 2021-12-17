import random as rd

import algo_data_design.utils.random as u_random


def swap_elements(array, i, j):
    holder = array[i]
    array[i] = array[j]
    array[j] = holder


def random_int_list(size, lower_limit=-65535, upper_limit=65535):
    return u_random.random_int_list(size, lower_limit=lower_limit, upper_limit=upper_limit)


def random_float_list(size):
    return u_random.random_float_list(size)


def sequential_int_list(size, start_with=0):
    size = int(size)
    start_with = int(start_with)
    return list(range(start_with, size + start_with))


def sequential_stepped_int_list(size, step, start_with=0):
    out = []
    for i in range(start_with, size + start_with, 1):
        out.append(i * step)
    return out


def shuffle_list(array):
    rd.shuffle(array)


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def conditional_reversed(array, reverse=False):
    if reverse:
        return reversed(array)
    else:
        return array
