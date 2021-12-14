def search(array, to_find, start=0):
    """
    Regular search
    Time complexity:
        Best: O(1)
        Average/Worst: O(n)
    Space complexity: O(1)
    """
    for i in range(start, len(array), 1):
        el = array[i]
        if el == to_find:
            return i
    return None


def search_with_hits(array, to_find, start=0, hits=0):
    """
    Regular search
    Time complexity:
        Best: O(1)
        Average/Worst: O(n)
    Space complexity: O(1)
    """
    for i in range(start, len(array), 1):
        hits += 1
        el = array[i]
        if el == to_find:
            return i, hits
    return None, hits
