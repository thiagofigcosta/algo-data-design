import algo_data_design.utils.list as u_list

MAXIMUM_FAST_SORTING_SIZE = 6


def sort(array):
    """
    One of the worsts
    Time complexity:
        Best: O(n) since we need to check if it is sorted
        Average: O((n-1)*n!)
    Space complexity: O(1)
    Unstable
    """
    # if not sorted shuffle until it is sorted
    while not u_list.is_sorted(array):
        u_list.shuffle_list(array)
