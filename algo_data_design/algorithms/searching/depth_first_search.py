from algo_data_design.algorithms.searching.depth_breadth_first_search import db_fs_iterative, list_of_visited_to_str, \
    db_fs_iterative_find


def depth_first_search_iterative(node_data_structure, string_output=False):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    visited_order = db_fs_iterative(node_data_structure, breadth=False)
    if string_output:
        return list_of_visited_to_str(visited_order)
    else:
        return visited_order


def depth_first_search_recursive(node_data_structure, visited_order=None, visited=None, string_output=False):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    if visited is None:
        visited = set()  # to avoid visiting the same twice
    if visited_order is None:
        visited_order = []
    visiting = node_data_structure.get_node()
    if visiting is not None:  # if the data structure is not empty
        visited.add(visiting)  # mark as visited
        visited_order.append(visiting)  # visit
        for to_visit in visiting.get_next_nodes():
            if to_visit not in visited:  # visit not visited children
                depth_first_search_recursive(to_visit.wrap_into_structure(), visited_order, visited, string_output)
    if string_output:
        return list_of_visited_to_str(visited_order)
    else:
        return visited_order


def depth_first_search_iterative_find(node_data_structure, to_find):
    """
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(e)
    """
    return db_fs_iterative_find(node_data_structure, to_find, breadth=False)
