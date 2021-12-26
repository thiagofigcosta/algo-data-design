import algo_data_design.utils.list as u_list
from algo_data_design.data_structures import heap


def sort(array):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(1)
    Unstable, two equal keys are not guaranteed to be in the same order as the input on the output
    """
    # create a max heap
    heap.build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        # swap the root (greatest) with the end (a small one)
        u_list.swap_elements(array, 0, i)
        # rebuild the max heap structure
        heap.rebuild_max_heap(array, i)
