from algo_data_design.algorithms import sorting


def search(array, to_find, already_sorted=True):
    """
    Fast search for sorted arrays (trees)
    Time complexity:
        Best: O(1)
        Average/Worst: O(log(n))
    Space complexity: O(1)
    """
    if not already_sorted:
        sorting.sort(array)
    low = 0
    high = len(array) - 1
    ret = None
    while low <= high:
        mid = (low + high) // 2  # dividing to conquer
        if to_find < array[mid]:
            high = mid - 1
        elif to_find > array[mid]:
            low = mid + 1
        else:
            ret = mid
            break
    return ret


def search_with_hits(array, to_find, already_sorted=True):
    """
    Fast search for sorted arrays (trees)
    Time complexity:
        Best: O(1)
        Average/Worst: O(log(n))
    Space complexity: O(1)
    """
    if not already_sorted:
        sorting.sort(array)
    hits = 0
    low = 0
    high = len(array) - 1
    ret = None
    while low <= high:
        hits += 1
        mid = (low + high) // 2  # dividing to conquer
        if to_find < array[mid]:
            high = mid - 1
        elif to_find > array[mid]:
            low = mid + 1
        else:
            ret = mid
            break
    return ret, hits
