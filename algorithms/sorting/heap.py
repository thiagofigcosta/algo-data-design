import utils.heap as u_heap
import utils.list as u_list


def sort(array):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(1)
    Unstable
    """
    # create a max heap
    u_heap.build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        # swap the root (greatest) with the end (a small one)
        u_list.swap_elements(array, 0, i)
        # rebuild the max heap structure
        root = array[0]
        left, right = 1, 2
        while right <= i:
            if right < i and array[right - 1] < array[right]:
                right += 1
            if root >= array[right - 1]:
                break
            array[left - 1] = array[right - 1]
            left = right
            right = 2 * left
        array[left - 1] = root
