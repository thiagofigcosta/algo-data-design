import utils.list as u_list


# TODO implement other gap sequences for shell sort instead of the original (n/2, n/4, n/8...)
#  https://en.wikipedia.org/wiki/Shellsort#Gap_sequences


def sort(array):
    """
    Time complexity:
        Average/Best: O(n*log(n))
        Worst: O(n^2)
    Space complexity: O(1)
    Unstable
    """
    step = len(array) // 2
    while step > 0:
        for i in range(len(array)):
            i_stepped = i + step
            if i_stepped >= len(array):
                break
            if array[i] > array[i_stepped]:
                u_list.swap_elements(array, i, i_stepped)
                for j in range(i - 1, -1, -1):
                    j_stepped = j + step
                    if array[j] > array[j_stepped]:
                        u_list.swap_elements(array, j, j_stepped)
                    else:
                        break
        step //= 2
