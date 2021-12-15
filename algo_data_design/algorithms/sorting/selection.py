import algo_data_design.utils.list as u_list


def sort(array):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    Stable
    """
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array), 1):
            if array[min] > array[j]:
                min = j
        u_list.swap_elements(array, i, min)