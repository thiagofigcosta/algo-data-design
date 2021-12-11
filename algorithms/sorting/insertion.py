def sort(array):
    """
    Best Scenario: Partially ordered arrays and perform ordered insertions
    Worst Scenario: Array sorted in reverse order
    Time complexity:
        Best: O(n)
        Average/Worst: O(n^2)
    Space complexity: O(1)
    Stable
    """
    for i, to_insert in enumerate(array):
        j = i - 1
        # find where the element is supposed to be and insert
        while j >= 0 and to_insert < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = to_insert


def insert(array, element, start=0):
    """
    Time complexity: O(n)
    """
    for i in range(start, len(array), 1):
        if array[i] >= element:
            array[i:i] = [element]
            return
    array.append(element)
