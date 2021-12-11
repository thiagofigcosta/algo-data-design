import random as rd


def swap_elements(array, i, j):
    holder = array[i]
    array[i] = array[j]
    array[j] = holder


def random_int_list(size, lower_limit, upper_limit):
    random_list = []
    for _ in range(size):
        n = rd.randint(lower_limit, upper_limit)
        random_list.append(n)
    return random_list


def random_float_list(size):
    return [rd.random() for _ in range(size)]


def sequential_int_list(size, start_with=0):
    size = int(size)
    start_with = int(start_with)
    return list(range(start_with, size + start_with))


def shuffle_list(array):
    rd.shuffle(array)


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True
