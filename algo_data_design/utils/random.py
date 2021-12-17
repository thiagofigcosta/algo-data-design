import random as rd
import uuid


def random_uuid():
    return uuid.uuid4().hex


def random_int(lower_limit=-65535, upper_limit=65535):
    return rd.randint(lower_limit, upper_limit)


def random_float(lower_limit=0, upper_limit=1):
    if lower_limit == 0 and upper_limit == 1:
        return rd.random()
    return lower_limit + rd.random() * (upper_limit - lower_limit)


def random_int_list(size, lower_limit=-65535, upper_limit=65535):
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
