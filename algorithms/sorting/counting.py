def sort(array):
    """
    A sorting algorithm for integers
    Best Scenario: All elements are the same
    Good Scenario: Several repeated elements
    Worst Scenario: Varied elements in a wide range
    Time complexity: O(n+k), where k is the length of the counting list, or size of the list range.
                When the list to be sorted is defined between a big interval then k is big.
    Space complexity: O(n+k), some sources says that this complexity is O(k), but we need to copy the
                array to sort it in place
    Stable
    """
    smallest_number = min(array)
    count_array_length = max(array) - smallest_number + 1
    count = [0] * count_array_length
    # count occurrences
    for el in array:
        count[el - smallest_number] += 1
    # compute initial positions
    for i in range(1, len(count), 1):
        count[i] += count[i - 1]
    # assign positions
    array_copy = array.copy()
    for el in array_copy:
        array[count[el - smallest_number] - 1] = el
        count[el - smallest_number] -= 1
