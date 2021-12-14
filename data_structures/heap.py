import utils.list as u_list


def build_min_max_heap(array, min_heap=False):
    """
    Builds a max heap, a binary three where every parent node is bigger than their children,
    or a min heap, a binary three where every parent node is smaller than their children
    Time complexity:
        Average: O(n*log(n))
    Space complexity: O(1)
    """
    for node in range(1, len(array), 1):
        father = get_node_father_index(node)
        # if the child is greater than the father we need to update it backwards
        backward_node = node
        while backward_node > 0 and ((array[backward_node] > array[father] and not min_heap) or (
                array[backward_node] < array[father] and min_heap)):
            u_list.swap_elements(array, backward_node, father)
            backward_node = get_node_father_index(backward_node)
            father = get_node_father_index(backward_node)


def rebuild_min_max_heap(array, starting_point, min_heap=False):
    """
    Rebuilds the min/max heap from a given point
    Time complexity:
        Average: O(n*log(n))
    Space complexity: O(1)
    """
    root = array[0]
    left, right = 1, 2
    while right <= starting_point:
        if right < starting_point and (
                (array[right - 1] < array[right] and not min_heap) or (array[right - 1] > array[right] and min_heap)):
            right += 1
        if (root >= array[right - 1] and not min_heap) or (root <= array[right - 1] and min_heap):
            break
        array[left - 1] = array[right - 1]
        left = right
        right = 2 * left
    array[left - 1] = root


def build_max_heap(array):
    build_min_max_heap(array, min_heap=False)


def rebuild_max_heap(array, starting_point):
    rebuild_min_max_heap(array, starting_point, min_heap=False)


def build_min_heap(array):
    build_min_max_heap(array, min_heap=True)


def rebuild_min_heap(array, starting_point):
    rebuild_min_max_heap(array, starting_point, min_heap=True)


def get_node_father_index(node):
    if node < 0:
        return None
    return (node - 1) // 2


def get_node_children_index(node, length=None):
    node_x2 = node * 2
    children = node_x2 + 1, node_x2 + 2
    if length is not None:
        return [child if child < length else None for child in children]
    return children
