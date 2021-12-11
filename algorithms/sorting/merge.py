def sort(array):
    """
    Good for external sorting (huge arrays that does not fit in memory)
    Time complexity:
        Average/Best/Worst: O(n*log(n))
    Space complexity: O(n)
    Stable
    """
    _sort_recursive(array)


def _sort_recursive(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_partition = array[:mid]
        right_partition = array[mid:]
        _sort_recursive(left_partition)
        _sort_recursive(right_partition)
        _merge(array, left_partition, right_partition)


def _merge(array, left_partition, right_partition):
    left_itr = 0
    right_itr = 0
    dst_itr = 0
    # merging sorted arrays
    while left_itr < len(left_partition) and right_itr < len(right_partition):
        if left_partition[left_itr] < right_partition[right_itr]:
            array[dst_itr] = left_partition[left_itr]
            left_itr += 1
        else:
            array[dst_itr] = right_partition[right_itr]
            right_itr += 1
        dst_itr += 1
    # moving the remainders
    for i in range(left_itr, len(left_partition), 1):
        array[dst_itr] = left_partition[i]
        dst_itr += 1
    for i in range(right_itr, len(right_partition), 1):
        array[dst_itr] = right_partition[i]
        dst_itr += 1
