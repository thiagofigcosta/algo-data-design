from algo_data_design.algorithms.graph import union, UnionFindSubset
from algo_data_design.data_structures.graph import Graph


def minimum_spanning_tree(graph, get_cost=False, get_tree=True):
    """
    Algorithm to create a tree from a graph containing all its nodes, the sum of the edges of this tree
    is also the minimum possible
    Useful for:
        - Traveling Salesman Problem approximation
        - Circuit / Network design
        - Cluster Analysis
    Indicated for: Sparse graphs
    Time Complexity: O(v*log(v)), where v=vertices and e=edges
    Space Complexity: O(e+v)
    """
    forest = UnionFindSubset.create_subsets(graph.nodes)  # auxiliary structure to detect circles, using union-find
    tree_connections = []  # to store the tree | src - weight - dst
    graph_connections = graph.export_connections()  # src - weight - dst
    graph_connections.sort(key=lambda k: k[1])  # sort by weight
    graph_connections_index = 0  # pointer to next best edge available
    tree_cost = 0
    # the amount of edges on a minimum spanning tree is equal to amount of nodes -1
    while len(tree_connections) < len(graph) - 1:  # while the tree is not ready
        if graph_connections_index >= len(graph_connections):
            break  # this protects the algorithm from raising exception when there is unreachable nodes
        src_node, weight, dst_node = graph_connections[graph_connections_index]
        graph_connections_index += 1  # increase the pointer
        if union(forest, src_node, dst_node):  # if adding this edges does not cause a circle, we use it on MST
            tree_connections.append([src_node, weight, dst_node])
            tree_cost += weight

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
