import utils.list as u_list


def sort(array):
    """
    A bad sorting algorithm
    Time complexity: O(n^2)
    Space complexity: O(1)
    Stable
    """
    for i in range(len(array)):
        for j in range(i + 1, len(array), 1):
            if array[i] > array[j]:
                u_list.swap_elements(array, i, j)
