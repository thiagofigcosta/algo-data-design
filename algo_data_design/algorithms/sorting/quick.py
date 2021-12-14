import algo_data_design.utils.list as u_list
from algo_data_design.algorithms.sorting import QuickSortPivotMethod as PivotMethod


def sort(array, pivot_method=PivotMethod.MEDIAN):
    """
    A good sorting algorithm
    Worst Scenario: When the array is already sorted
    Time complexity:
        Best/Average: O(n*log(n))
        Worst: O(n^2)
    Space complexity:
        Best/Average: O(n*log(n))
        Worst: O(n)
        Store the recursion stack
    Unstable (does not consider the positions to perform swaps, just the pivot)
    """
    _sort_recursive(array, 0, len(array) - 1, pivot_method)


def _median_of_3(a, b, c):
    if (a < b < c) or (c < b < a):
        return b
    elif (a < c < b) or (b < c < a):
        return c
    return a


def _choose_pivot(array, left, right, method):
    if method == PivotMethod.MIDDLE:
        pivot_index = (left + right) // 2
        pivot = array[pivot_index]
        return pivot
    elif method == PivotMethod.FIRST:
        return array[left]
    elif method == PivotMethod.LAST:
        return array[right]
    elif method == PivotMethod.MEDIAN:
        a = array[left]
        b = _choose_pivot(array, left, right, PivotMethod.MIDDLE)
        c = array[right]
        return _median_of_3(a, b, c)
    else:
        raise Exception(f'Unknown pivot method {method}')


def _sort_recursive(array, left, right, pivot_method):
    pivot = _choose_pivot(array, left, right, method=pivot_method)

    # every element before the pivot must be lower than it
    # every element after the pivot must be greater than it
    i, j = left, right
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            u_list.swap_elements(array, i, j)
            i += 1
            j -= 1
    # divide and conquer
    if j > left:
        _sort_recursive(array, left, j, pivot_method)
    if i < right:
        _sort_recursive(array, i, right, pivot_method)
