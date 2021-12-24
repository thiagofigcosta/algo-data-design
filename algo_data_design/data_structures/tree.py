import algo_data_design.utils.random as u_random
from algo_data_design.data_structures import Queue


class Node(object):

    def __init__(self, data, branches=None):
        if branches is None:
            branches = []
        self.data = data
        self.branches = branches
        self._uuid = u_random.random_uuid()

    def __str__(self):
        return str(self.data)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        # this function must be implemented in order to dict and set to work, so it cannot compare only data values
        return self._uuid == other._uuid

    def __hash__(self):
        # this function must be implemented in order to dict and set to work
        return hash(self._uuid)

    def __copy__(self):
        return self.copy()

    def deepcopy(self, nested_deep_copy=False):
        node = None
        for copy_func in ('__deepcopy__', 'deepcopy', '__copy__', 'copy'):
            copy_func_func = getattr(self.data, copy_func, None)
            if callable(copy_func_func):
                node = Node(copy_func_func(self.data),
                            [branch.deepcopy() if nested_deep_copy else branch for branch in self.branches])
                break
        if node is None:
            node = self.copy()
        node._uuid = self._uuid  # here I want to copy the uuid
        return node

    def copy(self):
        # I don't want to copy the uuid here
        return Node(self.data, self.branches.copy())

    def get_degree(self):
        return len(self.branches)

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        return self.branches

    def wrap_into_structure(self):
        # mandatory to run bfs and dfs
        return Tree(root=self)

    def is_leaf(self):
        return len(self.branches) == 0


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def get_node(self):
        # mandatory to run bfs and dfs
        return self.root

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        return self.root.get_next_nodes()

    def to_forest(self):
        return Forest([Tree(root=new_root) for new_root in self.root.branches])

    def find(self, el_data, depth=False):
        from algo_data_design.algorithms.searching import dfs_itr_find, bfs_itr_find
        if depth:
            return dfs_itr_find(self, el_data)
        else:
            return bfs_itr_find(self, el_data)

    def get_depth(self):
        # run a depth first search to count the deepness
        def __dfs_recursive_counter(node_data_structure, visited=None):
            if visited is None:
                # avoid infinite recursion in cyclic, trees are not cyclic though
                visited = set()
            visiting = node_data_structure.get_node()
            visited.add(visiting)
            depths = [0]  # base case of the recursion is 0
            for to_visit in visiting.get_next_nodes():
                if to_visit not in visited:
                    depths.append(__dfs_recursive_counter(to_visit.wrap_into_structure()))  # get depth of each subtree
            depth = max(depths)  # select the maximum depth
            return depth + 1  # add one to it

        if self.root is None:
            return 0
        return __dfs_recursive_counter(self)

    def get_height(self):
        return self.get_depth()

    def get_width(self):
        # run a breadth first search to count the wideness
        def __bfs_count(node_data_structure, queue=None, visited=None, results=None):
            if results is None:
                # create a dict to store the sum of the partial widths
                results = {}
            if visited is None:
                # avoid infinite recursion in cyclic, trees are not cyclic though
                visited = set()
            if queue is None:
                queue = Queue(first_el=node_data_structure.get_node())
            if not queue.is_empty():
                visiting = queue.pop()
                visited.add(visiting)
                inverse_cur_level = visiting.wrap_into_structure().get_depth()  # compute the depth of the current node
                if inverse_cur_level not in results:
                    results[inverse_cur_level] = 0
                results[inverse_cur_level] += len(
                    visiting.get_next_nodes())  # sum every partial width of nodes on same depth
                for to_visit in visiting.get_next_nodes():
                    if to_visit not in visited:
                        queue.append(to_visit)
                __bfs_count(node_data_structure, queue, visited, results)
            return results

        if self.root is None:
            return 0
        dict_results = __bfs_count(self)
        depth = len(dict_results)
        array_results = [0] * depth
        max_width = 0
        for inverse_level, width in dict_results.items():
            level = depth - inverse_level
            array_results[level] = width
            max_width = max(max_width, width)
        return max_width

    def depth_first_search(self, string_output=False, recursive=False):
        from algo_data_design.algorithms.searching import dfs_itr, dfs_rec
        if recursive:
            return dfs_rec(self, string_output=string_output)
        else:
            return dfs_itr(self, string_output=string_output)

    def breadth_first_search(self, string_output=False, recursive=False):
        from algo_data_design.algorithms.searching import bfs_itr, bfs_rec
        if recursive:
            return bfs_rec(self, string_output=string_output)
        else:
            return bfs_itr(self, string_output=string_output)

    def count(self):
        return len(self.depth_first_search())

    def __len__(self):
        return self.count()

    def __copy__(self):
        return self.copy()

    def copy(self):
        def __copy(src_node, _equivalence):
            if src_node not in _equivalence:
                # copy the node
                new_node = __copy_node_without_branches(src_node)
                _equivalence[src_node] = new_node  # store it on equivalence table
                # to the same of its children
                for node in src_node.branches:
                    new_node.branches.append(__copy(node, _equivalence))
            else:
                # if already cloned this node just return its reference
                new_node = _equivalence[src_node]
            return new_node

        def __copy_node_without_branches(src_node):
            # just to copy with empty branches, those will be filled later
            dst_node = src_node.copy()
            dst_node.branches = []
            return dst_node

        equivalence = {}  # create a dict to store the already cloned nodes
        new_root = __copy(self.root, equivalence)  # clone recursively
        return Tree(root=new_root)  # return new tree


class Forest(object):
    def __init__(self, trees=None):
        if trees is None:
            trees = []
        self.trees = trees

    def __len__(self):
        return len(self.trees)

    def __getitem__(self, item):
        return self.trees[item]
