import math

from algo_data_design.algorithms.searching.linear import search as linear_search, \
    search_with_hits as linear_search_with_hits


def search(array, to_find, start=0):
    """
    Search that can be better than linear
    Time complexity:
        Best: O(1)
        Average: O(sqrt(n))
        Worst: O(n)
    Space complexity: O(1)
    """
    fixed_step = int(math.sqrt(len(array)))
    step = 0
    i = 0
    # advance as much as possible
    while array[min(step, len(array)) - 1] < to_find:
        step += fixed_step
        i = step
        if i >= len(array):
            return None

    if array[i] == to_find:
        return i
    else:
        return linear_search(array, to_find, start=i)


def search_with_hits(array, to_find, start=0):
    """
    Search that can be better than linear
    Time complexity:
        Best: O(1)
        Average: O(sqrt(n))
        Worst: O(n)
    Space complexity: O(1)
    """
    hits = 0
    fixed_step = int(math.sqrt(len(array)))
    step = 0
    i = 0
    # advance as much as possible
    while array[min(step, len(array)) - 1] < to_find:
        hits += 1
        step += fixed_step
        i = step
        if i >= len(array):
            return None

    if array[i] == to_find:
        return i
    else:
        return linear_search_with_hits(array, to_find, start=i, hits=hits)
