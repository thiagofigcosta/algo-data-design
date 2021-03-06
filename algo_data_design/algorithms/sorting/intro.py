import math

import algo_data_design.utils.list as u_list
from algo_data_design.algorithms.sorting import QuickSortPivotMethod as PivotMethod
from algo_data_design.algorithms.sorting.heap import sort as heap_sort
from algo_data_design.algorithms.sorting.quick import _choose_pivot
from algo_data_design.algorithms.sorting.quick_insertion import _insertion_sort


def sort(array, pivot_method=PivotMethod.MEDIAN, insertion_threshold=50):
    """
    A hybrid sorting algorithm, used on C++
    Worst Scenario: When the array is already sorted
    Time complexity: O(n*log(n))
    Space complexity:
        Best/Average: O(n*log(n))
        Worst: O(n)
        Store the recursion stack
    Unstable, two equal keys are not guaranteed to be in the same order as the input on the output (does not consider the positions to perform swaps, just the pivot)
    """
    if len(array) > 1:
        depth = 2 * int(math.log2(len(array)))
        _sort_recursive(array, 0, len(array) - 1, depth, pivot_method, insertion_threshold)


def _sort_recursive(array, left, right, depth, pivot_method, insertion_threshold):
    if right - left < insertion_threshold:
        _insertion_sort(array, left, right)
    elif depth <= 0:
        to_sort = array[left:right + 1]
        heap_sort(to_sort)
        for i, el in enumerate(to_sort):
            array[left + i] = el
    else:
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
            _sort_recursive(array, left, j, depth - 1, pivot_method, insertion_threshold)
        if i < right:
            _sort_recursive(array, i, right, depth - 1, pivot_method, insertion_threshold)
