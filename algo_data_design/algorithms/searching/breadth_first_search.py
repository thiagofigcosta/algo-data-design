from algo_data_design.algorithms.searching.depth_breadth_first_search import db_fs_iterative, list_of_visited_to_str, \
    db_fs_iterative_find
from algo_data_design.data_structures import Queue


def breadth_first_search_iterative(node_data_structure, string_output=False):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    visited_order = db_fs_iterative(node_data_structure, breadth=True)
    if string_output:
        return list_of_visited_to_str(visited_order)
    else:
        return visited_order


def breadth_first_search_recursive(node_data_structure, visited_order=None, queue=None, visited=None,
                                   string_output=False):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    if visited is None:
        visited = set()  # to avoid visiting the same twice
    if visited_order is None:
        visited_order = []
    if queue is None:  # create an auxiliary queue to make it breadth
        queue = Queue(first_el=node_data_structure.get_first_node())
    if not queue.is_empty():
        visiting = queue.pop()  # get node to visit
        visited.add(visiting)  # mark as visited
        visited_order.append(visiting)  # visit
        for to_visit in visiting.get_next_nodes():
            if to_visit not in visited:  # add to visit list not visited children
                queue.append(to_visit)
        breadth_first_search_recursive(node_data_structure, visited_order, queue, visited,
                                       string_output)  # continue visiting
    if string_output:
        return list_of_visited_to_str(visited_order)
    else:
        return visited_order


def breadth_first_search_iterative_find(node_data_structure, to_find):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    return db_fs_iterative_find(node_data_structure, to_find, breadth=True)
