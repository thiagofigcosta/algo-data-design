from algo_data_design.algorithms.sorting.intro import sort as intro_sort


def sort(array, amount_of_buckets=20):
    """
    A sorting algorithm for float numbers in the interval [0,1)
    Best Scenario: float numbers uniformly distributed
    Time complexity:
        Best: O(n+k), where k is the amount of buckets
        Average: O(n)
        Worst: O(n^2)
    Space complexity: O(n+k)
    Stable
    """
    # create buckets
    buckets = [[] for _ in range(amount_of_buckets)]

    # assign each element to its bucket
    for el in array:
        destination_bucket = int(el * amount_of_buckets)
        buckets[destination_bucket].append(el)

    # sort the buckets
    for i in range(amount_of_buckets):
        intro_sort(buckets[i])

    # combine the buckets
    i = 0
    for bucket in buckets:
        for el in bucket:
            array[i] = el
            i += 1
