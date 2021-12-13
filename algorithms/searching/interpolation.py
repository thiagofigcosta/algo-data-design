from algorithms import sorting


def search(array, to_find, already_sorted=True):
    """
    Fast search for uniformly distributed sorted arrays (trees)
    Time complexity:
        Best: O(1)
        Average/Worst: O(log(log(n)))
    Space complexity: O(1)
    """
    if not already_sorted:
        sorting.sort(array)
    low = 0
    high = len(array) - 1
    ret = None
    while low <= high and array[low] <= to_find <= array[high]:
        pos = low + ((to_find - array[low]) // (array[high] - array[low])) * (high - low)
        if to_find < array[pos]:
            high = pos - 1
        elif to_find > array[pos]:
            low = pos + 1
        else:
            ret = pos
            break
    return ret


def search_with_hits(array, to_find, already_sorted=True):
    """
    Fast search for uniformly distributed sorted arrays (trees)
    Time complexity:
        Best: O(1)
        Average/Worst: O(log(log(n)))
    Space complexity: O(1)
    """
    if not already_sorted:
        sorting.sort(array)
    hits = 0
    low = 0
    high = len(array) - 1
    ret = None
    while low <= high and array[low] <= to_find <= array[high]:
        hits += 1
        pos = low + ((to_find - array[low]) * (high - low)) // (array[high] - array[low])
        if to_find < array[pos]:
            high = pos - 1
        elif to_find > array[pos]:
            low = pos + 1
        else:
            ret = pos
            break
    return ret, hits
