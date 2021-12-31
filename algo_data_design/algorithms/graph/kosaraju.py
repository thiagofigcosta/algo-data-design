from algo_data_design.data_structures import Stack


def strongly_connected_components(graph, first_dfs_recursive=False):
    """
    Algorithm that receives a directed graph and returns the clusters of strongly connected elements.
    Strongly connected elements are a group of nodes in which every node can reach each other, this can be used
    to simplify the graph, since the group can be considered as a single node that contains all others fom the graph
    perspective
    Time Complexity: O(v+e), where v=vertices and e=edges
    Space Complexity: O(v)
    """
    graph_to_run = graph.copy()  # copy the graph to preserve the original
    if first_dfs_recursive:
        tree_of_potential_scc = _dfs_find_potential_scc_in_order_rec(graph_to_run)  # find potential SCC
    else:
        tree_of_potential_scc = _dfs_find_potential_scc_in_order_iter(graph_to_run)  # find potential SCC
    # revert the graph connections (transpose), to check which nodes are reachable from each other
    graph_to_run.transpose()  # transpose the graph
    # run DFS again on reversed graph, all reachable nodes from a given one belong to the same group
    scc_clusters = []
    visited = set()  # to avoid visiting the same twice/duplicating, we use the same set to every following dfs
    while not tree_of_potential_scc.is_empty():
        node = tree_of_potential_scc.pop()
        if node not in visited:  # to avoid visiting the same twice/duplicating
            # standard DFS
            scc = []  # to store reachable nodes from the starting one
            to_visit = Stack(first_el=node)
            while len(to_visit) > 0:
                visiting = to_visit.pop()
                if visiting not in visited:  # visit just if not visited
                    visited.add(visiting)  # mark as visited
                    scc.append(visiting)  # visit
                    for branch in reversed(visiting.get_next_nodes()):
                        to_visit.push(branch)  # add children to visit
            scc_clusters.append(scc)  # append the scc to the group
    return scc_clusters


def _dfs_find_potential_scc_in_order_iter(graph):
    visited = set()  # to avoid visiting the same twice
    # the line is the string of nodes in depth until the last reachable one
    to_visit = Stack(first_el=(False, graph.nodes[0]))  # False means we will visit this node, not finish the line
    forest_of_potential_scc = Stack()  # this stack stores the reachable nodes from the root, in their finish order
    while len(to_visit) > 0:
        finish_line, visiting = to_visit.pop()
        if finish_line:
            forest_of_potential_scc.push(visiting)  # reached the end of the line
        elif visiting not in visited:  # visit just if not visited
            to_visit.push((True, visiting))  # mark to remove from line, this is need to avoid recursion if we
            # were using recursion we would just remove the element from the line after finishing all
            # neighbors' recursion calls
            visited.add(visiting)  # mark as visited
            for branch in reversed(visiting.get_next_nodes()):
                to_visit.push((False, branch))  # add children to visit
    return forest_of_potential_scc


def _dfs_find_potential_scc_in_order_rec(graph):
    def __dfs_rec(_node, _visited, _forest_of_potential_scc):
        _visited.add(_node)  # mark as visited
        for to_visit in _node.get_next_nodes():
            if to_visit not in _visited:  # visit not visited children
                __dfs_rec(to_visit, _visited, _forest_of_potential_scc)
        _forest_of_potential_scc.push(_node)  # reached the end of the line

    visited = set()  # to avoid visiting the same twice
    forest_of_potential_scc = Stack()  # this stack stores the reachable nodes from the root, in their finish order
    for visiting in graph.nodes:  # need to iterate because not every node might be reachable from the start point
        if visiting not in visited:  # if the data structure is not empty
            __dfs_rec(visiting, visited, forest_of_potential_scc)

    return forest_of_potential_scc
