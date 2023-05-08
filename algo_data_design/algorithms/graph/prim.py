from algo_data_design.data_structures.graph import Graph


def minimum_spanning_tree(graph, get_cost=False, get_tree=True):
    """
    Algorithm to create a tree from a graph containing all its nodes, the sum of the edges of this tree
    is also the minimum possible
    Useful for:
        - Traveling Salesman Problem approximation
        - Circuit / Network design
        - Cluster Analysis
    Indicated for: Dense graphs
    Time Complexity: O(vˆ2), where v=vertices and e=edges
             - Using binary heap: O(e log v)
             - Using fibonacci heap: O(e + v log v)
    Space Complexity: O(e+v)
    """
    nodes_in_the_tree = set()  # set of the nodes in the tree
    tree_connections = []  # to store the tree | src - weight - dst
    tree_cost = 0
    unreachable_elements = 0  # to avoid infinite loops when there are non connected nodes, but these kinds of graphs
    #                                should not be used to generate minimum spanning tree, this is just a precaution
    nodes_in_the_tree.add(graph.nodes[0])  # add the first node
    while len(nodes_in_the_tree) + unreachable_elements < len(graph):
        minimum_edge = []
        minimum_node = None
        for node in nodes_in_the_tree: # we want connections between nodes already in MST with nodes not yet on it
            for neighbor, weight in node.get_connections():
                if neighbor not in nodes_in_the_tree:  # we don't want circles
                    # if is the first or this edge is smaller pick it
                    if minimum_node is None or weight < minimum_edge[0]:
                        minimum_edge = [weight, neighbor]
                        minimum_node = node
        if minimum_node is None:
            unreachable_elements += 1
        else:
            nodes_in_the_tree.add(minimum_edge[1])  # add the new node on the tree
            tree_cost += minimum_edge[0]
            tree_connections.append(
                [minimum_node, minimum_edge[0], minimum_edge[1]])  # store the connection to construct the new tree
    if get_tree:
        # algorithm is done, we now construct the new tree
        mst = Graph()
        equivalence = {}
        for node in graph.get_nodes():
            new_node = node.copy_without_connection()
            mst.add_node(new_node)
            equivalence[node] = new_node
        for src_node, weight, dst_node in tree_connections:
            mst.add_connection(equivalence[src_node], equivalence[dst_node], weight)
        if get_cost:
            return mst, tree_cost
        else:
            return mst
    else:
        return tree_cost
