import utils.list as u_list


def build_max_heap(array):
    """
    Builds a heap, a binary three where every parent node is bigger than their children
    Time complexity:
        Average: O(n*log(n))
    Space complexity: O(1)
    """
    for node in range(1, len(array), 1):
        father = get_node_father_index(node)
        # if the child is greater than the father we need to update it backwards
        backward_node = node
        while backward_node > 0 and array[backward_node] > array[father]:
            u_list.swap_elements(array, backward_node, father)
            backward_node = get_node_father_index(backward_node)
            father = get_node_father_index(backward_node)


def get_node_father_index(node):
    if node < 0:
        return None
    return (node - 1) // 2


def get_node_children_index(node, lenght=None):
    node_x2 = node * 2
    children = node_x2 + 1, node_x2 + 2
    if lenght is not None:
        return [child if child < lenght else None for child in children]
    return children
