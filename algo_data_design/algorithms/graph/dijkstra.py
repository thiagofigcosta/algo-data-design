from algo_data_design.algorithms.graph import DijkstraMethod as Method
from algo_data_design.data_structures import PriorityQueue


def shortest_paths_cost(graph, starting_node_or_data, destination_node_or_data=None, method=Method.PRIORITY_QUEUE):
    if method == Method.PRIORITY_QUEUE:
        return _shortest_paths_cost_with_priority_queue(graph, starting_node_or_data, destination_node_or_data)
    elif method == Method.REGULAR:
        return _shortest_paths_cost_standard(graph, starting_node_or_data, destination_node_or_data)
    else:
        raise AttributeError(f'Unknown method {method}')


def _shortest_paths_cost_standard(graph, starting_node_or_data, destination_node_or_data=None):
    """
    Algorithm with hard spelling, that is used to find the shortest path between a node and all other
    Time Complexity: O(v^2), where v=vertices and e=edges
                - Using binary heap: O(e log v)
                - Using fibonacci heap: O(e + v log v)
                - Using priority queue: ??
                - If sparse: O(v^3)
    Space Complexity: O(v)
    """
    # instead of doing `not in distances` we could assign all distances to infinity at start
    starting_node = graph.get_node(starting_node_or_data)
    destination_node = None if destination_node_or_data is None else graph.get_node(destination_node_or_data)
    distances = {}  # store the distances from the starting node, if a node is not here, the distance is infinite
    visited = set()

    distances[starting_node] = 0  # there is not cost of staying in the same place
    for _ in range(len(graph)):
        closest_non_visited_node = _get_closest_non_visited(distances, visited)
        if closest_non_visited_node is not None:  # the closest non visited is None when there is a unreachable node
            visited.add(closest_non_visited_node)  # mark the node as visited

            for neighbor, neighbor_distance in closest_non_visited_node.get_connections():
                if neighbor not in visited:
                    # check the distances between the neighbor and the origin
                    neighbor_distance_from_origin = distances[closest_non_visited_node] + neighbor_distance
                    # if I don't know this path or if this path is better than the one we knew update it on distances
                    if neighbor not in distances or neighbor_distance_from_origin < distances[neighbor]:
                        distances[neighbor] = neighbor_distance_from_origin

    if destination_node is not None:
        return distances[destination_node]
    return distances


def _get_closest_non_visited(distances, visited):
    shortest_distance = None
    shortest_node = None
    # select the closest non visited node
    for node, distance in distances.items():
        if node not in visited and (shortest_distance is None or distance < shortest_distance):
            shortest_node = node
            shortest_distance = distance
    return shortest_node


def replace_node_key_by_data_key(distances):
    for k in list(distances):  # list forces a copy of dict keys to iter
        distances[k.data] = distances.pop(k)
    return distances


def _shortest_paths_cost_with_priority_queue(graph, starting_node_or_data, destination_node_or_data=None):
    """
    Algorithm with hard spelling, that is used to find the shortest path between a node and all other
    Time Complexity: O((e+v)*log(v)), where v=vertices and e=edges
    Space Complexity: O(v)
    """
    # instead of doing `not in distances` we could assign all distances to infinity at start
    starting_node = graph.get_node(starting_node_or_data)
    destination_node = None if destination_node_or_data is None else graph.get_node(destination_node_or_data)
    open_list = PriorityQueue(max_queue=False)  # this list stores the points to explore, the neighbors, the priority
    # is the cost
    distances = {}  # store the distances from the starting node, if a node is not here, the distance is infinite
    visited = set() # elements should be added on queue at most once
    
    open_list.push(starting_node)  # start with the first node
    distances[starting_node] = 0  # there is not cost of staying in the same place
    while not open_list.is_empty():  # while there is nodes to explore
        closest_node, path_distance = open_list.pop(retrieve_priority=True)
        for neighbor, neighbor_distance in closest_node.get_connections():
            if neighbor not in visited:
                visited.add(neighbor)  # mark the node as visited
                # check the distances between the neighbor and the origin
                neighbor_distance_from_origin = path_distance + neighbor_distance
                # if I don't know this path or if this path is better than the one we knew update it on distances table
                if neighbor not in distances or neighbor_distance_from_origin < distances[neighbor]:
                    distances[neighbor] = neighbor_distance_from_origin  # updating the distance
                    open_list.push(neighbor, neighbor_distance_from_origin)  # add neighbor on priority queue

    if destination_node is not None:
        return distances[destination_node]
    return distances
