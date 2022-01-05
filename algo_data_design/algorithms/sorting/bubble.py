import algo_data_design.utils.list as u_list
from algo_data_design.algorithms.sorting import BubbleSortMethod as Method


def sort(array, method=Method.OPTIMUM):
    if method == Method.OPTIMUM:
        _optimum_sort(array)
    elif method == Method.REGULAR:
        _regular_sort(array)
    else:
        raise AttributeError(f'Unknown method {method}')


def _optimum_sort(array):
    """
    Best Scenario: Array already sorted
    Worst Scenario: Array is sorted descending
    Time complexity:
        Best: O(n)
        Average/Worst: O(n^2)
    Space complexity: O(1)
    Stable, two equal keys are guaranteed to be in the same order as the input on the output
    """
    for i in range(len(array)):
        swapped = False
        # compare following elements two by two
        for j in range(0, len(array) - i - 1, 1):
            next_j = j + 1
            if array[j] > array[next_j]:
                u_list.swap_elements(array, j, next_j)
                swapped = True
        # if the array is sorted we can exit
        if not swapped:
            break


def _regular_sort(array):
    """
    Worst Scenario: Array is sorted descending
    Time complexity: O(n^2)
    Space complexity: O(1)
    Stable, two equal keys are guaranteed to be in the same order as the input on the output
    """
    for i in range(len(array)):
        # compare following elements two by two
        for j in range(0, len(array) - i - 1, 1):
            next_j = j + 1
            if array[j] > array[next_j]:
                u_list.swap_elements(array, j, next_j)
