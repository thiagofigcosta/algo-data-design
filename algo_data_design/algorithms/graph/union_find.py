class Subset(object):
    def __init__(self, parent, rank):
        # the rank serves to keep the subsets with a small depth,
        # the rank is analog to the tree height, but sometimes the actual height can be smaller
        self.parent = parent
        self.rank = rank

    @staticmethod
    def create_empty_subsets():
        subsets = {}
        return subsets

    @staticmethod
    def fill_subsets(subsets, iterable_nodes):
        for node in iterable_nodes:
            subsets[node] = Subset(node, 0)

    @staticmethod
    def create_subsets(iterable_nodes):
        subsets = Subset.create_empty_subsets()
        Subset.fill_subsets(subsets, iterable_nodes)
        return subsets


def find(subsets, node):
    # O(log(n)), where n is the number of elements
    # finds the node that represents its subset recursively (root)
    # if two nodes have the same root, they belong to same subset
    if subsets[node].parent != node:  # path compression, allows reducing tree heights
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


def union(subsets, node_1, node_2):
    # O(1) + find calls complexity, but the union itself is constant
    # union by rank, join two subsets or trees
    # find the roots
    root_of_node_1_subset = find(subsets, node_1)
    root_of_node_2_subset = find(subsets, node_2)
    if root_of_node_1_subset == root_of_node_2_subset:  # Already on the same subset, there is no need of uniting
        return False  # operation fails
    # put the smaller rank tree under the root of highest rank one
    if subsets[root_of_node_1_subset].rank > subsets[root_of_node_2_subset].rank:
        subsets[root_of_node_2_subset].parent = root_of_node_1_subset
    elif subsets[root_of_node_2_subset].rank > subsets[root_of_node_1_subset].rank:
        subsets[root_of_node_1_subset].parent = root_of_node_2_subset
    else:
        # when they have the same rank the order does not matter and we increase the rank of the root
        subsets[root_of_node_1_subset].parent = root_of_node_2_subset
        subsets[root_of_node_2_subset].rank += 1
    return True


def has_circle(graph):
    # O(v*log(e)), where e is the number of edges and v number of vertices
    subsets = Subset.create_subsets(graph.nodes)  # add all nodes in a separated group
    for node_1 in graph.nodes:
        for node_2, _ in node_1.get_connections():
            # construct the subsets based on the edges, if cannot unite (they are already on same set) there is a circle
            if not union(subsets, node_1, node_2):
                return True
    return False
