import math


def sort(array):
    """
    A sorting algorithm for integers
    Best Scenario: Elements have a large interval, good for sorting data partially (dates, 13052021, sort by year only)
    Time complexity: O(nk), where k is the amount of digits in the greatest value
    Space complexity: O(n+k)
    Unstable, two equal keys are not guaranteed to be in the same order as the input on the output
    """
    module = True
    greatest_number = max(array)
    k = int(math.log10(abs(greatest_number))) + 2
    for i in range(k):
        signal_as_digit = (i + 1 == k)
        count = [0] * 10
        exp = 10 ** i
        to_sort = array.copy()
        for el in to_sort:
            digit = _compute_digit(el, exp, module, signal_as_digit)
            count[digit] += 1
        # compute initial positions
        for j in range(1, len(count), 1):
            count[j] += count[j - 1]
        for j in range(len(to_sort) - 1, -1, -1):
            digit = _compute_digit(to_sort[j], exp, module, signal_as_digit)
            array[count[digit] - 1] = to_sort[j]
            count[digit] -= 1


def _compute_digit(number, exp, module=False, signal_as_digit=False):
    if not signal_as_digit:
        if module and number < 0:
            return 9 - (int(abs(number) / exp) % 10)
        else:
            return int(number / exp) % 10
    else:
        if number < 0:
            return 0
        else:
            return 1


def sort_positive_only(array):
    """
    A sorting algorithm for integers
    Best Scenario: Elements have a large interval, good for sorting data partially (dates, 13052021, sort by year only)
    Time complexity: O(nk), where k is the amount of digits in the greatest value
    Space complexity: O(n+k)
    Stable, two equal keys are guaranteed to be in the same order as the input on the output
    """
    greatest_number = max(array)
    k = int(math.log10(abs(greatest_number))) + 1
    for i in range(k):
        count = [0] * 10
        exp = 10 ** i
        to_sort = array.copy()
        for el in to_sort:
            digit = _compute_digit(el, exp)
            count[digit] += 1
        # compute initial positions
        for j in range(1, len(count), 1):
            count[j] += count[j - 1]
        for j in range(len(to_sort) - 1, -1, -1):
            digit = _compute_digit(to_sort[j], exp)
            array[count[digit] - 1] = to_sort[j]
            count[digit] -= 1
