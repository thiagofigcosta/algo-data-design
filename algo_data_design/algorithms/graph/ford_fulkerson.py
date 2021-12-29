from algo_data_design.data_structures import Queue


def maximum_flow(graph, starting_node_or_data, destination_node_or_data, preserve_graph=True):
    """
    Algorithm to compute the maximum flow between two points of graph
    Time Complexity: O(e*f), where f=maximum flow and e=edges
    Space Complexity: O(v), where v=vertices
    """
    if preserve_graph:  # the residual graph will change, so we might want to copy the original
        # (preserving the uuid, because if we receive a node as argument, we must find it on the new residual)
        residual_graph = graph.copy_preserving_node_uuid()
    else:
        residual_graph = graph
    # on the residual graph, the weights are interpreted as the maximum capacity, or flux, or flow
    start_node = residual_graph.get_node(starting_node_or_data)  # get the source node
    end_node = residual_graph.get_node(destination_node_or_data)  # get the destination node
    parent = {}  # stores a parent of a node, with means that we have a path of nodes, also stores the edge flux
    max_flow = 0  # result
    while _breadth_first_search_path_find(start_node, end_node, parent):  # while there is a path between src and dst
        # get the lowest available flow in between the edges of the path, with means the maximum flow/flux that
        # can go through it
        path_flow = _compute_path_max_flow(start_node, end_node, parent)
        max_flow += path_flow  # add the path flow to solution
        # subtract the path flow from the residual graph on each edge of the chosen path
        # add the path flow to the residual graph on each reversed edges of the chosen path
        _update_residual_graph(path_flow, start_node, end_node, parent)

    return max_flow


def _breadth_first_search_path_find(source, destination, parent):
    # standard BFS that returns true when there is available path between src and dst
    # also fills parent with the current path and available flux
    visited = set()  # to avoid visiting the same twice
    # use a queue to always retrieve the first added element, making it breadth
    to_visit = Queue(first_el=source)
    while len(to_visit) > 0:
        visiting = to_visit.pop()
        visited.add(visiting)  # mark as visited
        for node, available_flux in visiting.get_connections():
            # different from my other bfs implementations I'm checking if the node was visited inside the loop
            # this is because I need to also check if there is available flux
            if node not in visited and available_flux > 0:  # visit if not visited and if there is flow available
                parent[node] = (visiting, available_flux)
                if node == destination:
                    return True  # found the destination
                to_visit.push(node)  # add children to visit
    return False  # No way between the nodes


def _compute_path_max_flow(source, destination, parent):
    # compute the max flow of the given path, basically iterates through it and get the lowest flux
    pointer = destination  # points to destination and move the source
    max_path_flow = None
    while pointer != source:
        pointer, flux = parent[pointer]
        if max_path_flow is None or flux < max_path_flow:
            max_path_flow = flux
    return max_path_flow


def _update_residual_graph(path_flow, source, destination, parent):
    # subtract from the residual graph the flow of the path
    to_pointer = destination  # points to destination and move until the source, this stores the dst of the edge
    while to_pointer != source:
        from_pointer, _ = parent[to_pointer]  # from_pointer stores the src of the edge
        edge = from_pointer.get_connection_to(to_pointer)
        edge.weight -= path_flow  # subtract the path cost from the edge
        reverse_edge = to_pointer.get_connection_to(from_pointer)
        if reverse_edge is None:
            to_pointer.add_connection(from_pointer, path_flow)  # if the reverse edge does not exists, create it
        else:
            reverse_edge.weight += path_flow
        to_pointer = from_pointer  # the previous source is now the destination
