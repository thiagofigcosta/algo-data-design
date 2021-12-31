from algo_data_design.algorithms.searching import AStarHeuristic, AStarMetadata
from algo_data_design.algorithms.searching.a_star import _compute_path_and_cost
from algo_data_design.data_structures import PriorityQueue


def shortest_path(graph, starting_node_or_data, destination_node_or_data, node_coordinates_map, traversal_mode=False,
                  heuristic=AStarHeuristic.Type.DIAGONAL_DISTANCE):
    """
    Algorithm to find the shortest path between two points in a grid / map or graph also can be used to traverse a graph
    It is similar to dijkstra, but it as a heuristic to guide it. It maps all possible movements and chose the cheapest
    one based on f(n), where f(n) = g(n) + h(n), g(n) is the cost to move to the next node (n) and h(n) is a heuristic
    that estimates the cost of moving to next node (n)
    Indicated for: path find in grid and graph traversal
    Time Complexity: O() ??
    Space Complexity: O(n^2), where n is the amount of points ??
    """
    starting_node = graph.get_node(starting_node_or_data)
    if not traversal_mode:
        destination_node = graph.get_node(destination_node_or_data)
    else:  # when traversing `destination_node_or_data` can be just a object with coordinates on `node_coordinates_map`
        is_this_node = graph.get_node(destination_node_or_data)
        if is_this_node is not None:
            destination_node = is_this_node
        else:
            destination_node = destination_node_or_data

    if not traversal_mode:
        _validate_inputs(graph, starting_node, destination_node, node_coordinates_map)
    else:
        # validating starting_node twice because when traversing the graph the destination point not necessarily must
        # be a graph node. So I'm validating just the start node because I don't want to write other validation function
        _validate_inputs(graph, starting_node, starting_node, node_coordinates_map)

    points_metadata = {}  # store the distances from the starting node, if a node is not here, the distance is infinite
    open_list = PriorityQueue()  # this list stores the points to explore, the neighbors, the priority is the cost
    closed_list = set()  # this list stores already explored points

    visit_order = []  # to traverse the graph

    points_metadata[starting_node] = AStarMetadata(starting_node)
    open_list.push(starting_node,
                   priority=points_metadata[starting_node].f)  # there is not cost of staying in the same place

    heuristic = AStarHeuristic(heuristic)  # instantiate the heuristic
    while not open_list.is_empty():  # while there is nodes to explore
        exploring_node = open_list.pop()  # get the first node
        closed_list.add(exploring_node)  # mark as visited
        if traversal_mode:  # if traverse, store the order
            visit_order.append(exploring_node)
        for neighbor, neighbor_dist in exploring_node.get_connections():
            if neighbor == destination_node and not traversal_mode:  # we want to finish only if we are not in traverse mode
                # found the path
                points_metadata[destination_node] = AStarMetadata(
                    exploring_node, neighbor_dist)  # add the goal on the metadata to compute path
                return _compute_path_and_cost(points_metadata, starting_node,
                                              destination_node)  # compute path and return
            elif neighbor not in closed_list:
                neighbor_g = points_metadata[
                                 exploring_node].g + neighbor_dist  # previous path g cost + neighbor distance
                # retrieve the coordinates of the nodes to compute heuristic
                neighbor_h = heuristic.calc(node_coordinates_map[neighbor], node_coordinates_map[destination_node])
                neighbor_f = neighbor_g + neighbor_h  # final neighbor cost

                # if is the first time that we compute this neighbor of this path for it is best than the previous
                # we put it on the open_list
                if neighbor not in points_metadata or neighbor_f < points_metadata[neighbor].f:
                    points_metadata[neighbor] = AStarMetadata(exploring_node, neighbor_dist, neighbor_g, neighbor_h,
                                                              neighbor_f)
                    open_list.append(neighbor, priority=neighbor_f)
    if not traversal_mode:
        return None, None  # No path found
    else:
        return visit_order


def _validate_inputs(graph, starting_node, destination_node, node_coordinates_map):
    for node in [starting_node, destination_node]:
        if node not in graph.nodes:
            raise Exception('Unreachable nodes')
    for node in graph.nodes:
        if node not in node_coordinates_map:
            raise Exception('All nodes must have related coordinates')


def traverse(graph, starting_node_or_data, destination_node_or_data, node_coordinates_map,
             heuristic=AStarHeuristic.Type.DIAGONAL_DISTANCE):
    return shortest_path(graph, starting_node_or_data, destination_node_or_data, node_coordinates_map,
                         traversal_mode=True, heuristic=heuristic)
