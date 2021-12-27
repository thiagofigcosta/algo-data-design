from algo_data_design.data_structures import Queue, Stack
from algo_data_design.utils import list as u_list


def db_fs_iterative(node_data_structure, breadth=False):
    visited_order = []
    visited = set()  # to avoid visiting the same twice
    if breadth:
        # use a queue to always retrieve the first added element, making it breadth
        to_visit = Queue(first_el=node_data_structure.get_first_node())
    else:
        # use a stack to always retrieve the last added element, making it depth
        to_visit = Stack(first_el=node_data_structure.get_first_node())
    while len(to_visit) > 0:
        visiting = to_visit.pop()
        if visiting not in visited:  # visit just if not visited
            visited.add(visiting)  # mark as visited
            visited_order.append(visiting)  # visit
            for branch in u_list.conditional_reversed(visiting.get_next_nodes(), reverse=not breadth):
                to_visit.push(branch)  # add children to visit
    return visited_order


def list_of_visited_to_str(visited_order):
    return ' -> '.join([str(node) for node in visited_order])


def db_fs_iterative_find(node_data_structure, to_find, breadth=False):
    visited = set()  # to avoid visiting the same twice
    if breadth:
        # use a queue to always retrieve the first added element, making it breadth
        to_visit = Queue(first_el=node_data_structure.get_first_node())
    else:
        # use a stack to always retrieve the last added element, making it depth
        to_visit = Stack(first_el=node_data_structure.get_first_node())
    while len(to_visit) > 0:
        visiting = to_visit.pop()
        if visiting not in visited:  # visit just if not visited
            visited.add(visiting)  # mark as visited
            if visiting.data == to_find:  # visit
                return visiting
            for branch in u_list.conditional_reversed(visiting.get_next_nodes(), reverse=not breadth):
                to_visit.push(branch)  # add children to visit
    return None
