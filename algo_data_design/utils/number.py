import random as rd


def random_int(lower_limit=-65535, upper_limit=65535):
    return rd.randint(lower_limit, upper_limit)


def random_float(lower_limit=0, upper_limit=1):
    if lower_limit == 0 and upper_limit == 1:
        return rd.random()
    return lower_limit + rd.random() * (upper_limit - lower_limit)
