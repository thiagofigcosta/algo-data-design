import algo_data_design.utils.random as u_random
from algo_data_design.data_structures import Queue


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self._uuid = u_random.random_uuid()

    def __str__(self):
        return str(self.data)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        # this function must be implemented in order to dict and set to work, so it cannot compare only data values
        if not isinstance(other, Node):
            return False
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
                if nested_deep_copy:
                    node = Node(copy_func_func(self.data), self.left.deepcopy() if self.left is not None else None,
                                self.right.deepcopy() if self.right is not None else None)
                else:
                    node = Node(copy_func_func(self.data), self.left, self.right)
                break
        if node is None:
            node = self.copy()
        node._uuid = self._uuid  # here I want to copy the uuid
        return node

    def copy(self):
        # I don't want to copy the uuid here
        return Node(self.data, self.left.copy() if self.left is not None else None,
                    self.right.copy() if self.right is not None else None)

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        branches = []
        if self.left is not None:
            branches.append(self.left)
        if self.right is not None:
            branches.append(self.right)
        return branches

    def wrap_into_structure(self):
        # mandatory to run bfs and dfs
        return BinaryTree(root=self)

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_full(self):
        return self.left is not None and self.right is not None


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_first_node(self):
        # mandatory to run bfs and dfs
        return self.root

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        return self.root.get_next_nodes()

    def find_dfs(self, el_data):
        from algo_data_design.algorithms.searching import dfs_itr_find
        return dfs_itr_find(self, el_data)

    def find_bfs(self, el_data):
        return self.find(el_data)

    def find(self, el_data):
        """
        Time complexity:
            Best: O(1)
            Average: O(h), where h is height of the tree
            Worst: O(n), search in all nodes
        Space complexity: O(n)
        """
        from algo_data_design.algorithms.searching import bfs_itr_find
        return bfs_itr_find(self, el_data)

    def is_full(self):
        # run dfs to check
        # has only 0 or two branches in every node
        if self.root is None:  # empty tree
            return True
        if self.root.is_leaf():  # both branches are empty
            return True
        if not self.root.is_full():  # has one branch only
            return False
        return self.root.left.wrap_into_structure().is_full() and \
               self.root.right.wrap_into_structure().is_full()

    def is_perfect(self, depth=None, cur_level=0):
        # run dfs to check
        # has two branches in every internal node, every leave must be in same level
        if self.root is None:  # empty tree
            return True
        if depth is None:
            depth = self.get_depth()
        if self.root.is_leaf():  # both branches are empty, so they are leaf nodes
            return depth == (cur_level + 1)  # check if leaves are at the end
        if not self.root.is_full():  # has one branch only
            return False
        return self.root.left.wrap_into_structure().is_perfect(depth, cur_level + 1) and \
               self.root.right.wrap_into_structure().is_perfect(
                   depth, cur_level + 1)

    def is_complete(self, count=None, cur_index=0):
        # run dfs to check, the positions/indexes of the tree must be organizable in a heap structure
        # has only 0 or two branches in every node, the leaves must be filled from left to right,
        #       the last element is allowed to not have the right element
        if self.root is None:  # empty tree
            return True
        if count is None:
            count = self.count()
        if cur_index >= count:  # constraint violated
            return False
        left_result = self.root.left is None or \
                      self.root.left.wrap_into_structure().is_complete(count, 2 * cur_index + 1)
        right_result = self.root.right is None or \
                       self.root.right.wrap_into_structure().is_complete(count, 2 * cur_index + 2)
        return left_result and right_result

    def is_balanced(self):
        # run dfs to check
        if self.root is None:
            return True
        left_height = 0
        if self.root.left is not None:
            left_height = self.root.left.wrap_into_structure().get_height()

        right_height = 0
        if self.root.right is not None:
            right_height = self.root.right.wrap_into_structure().get_height()

        if abs(left_height - right_height) <= 1:
            left_result = self.root.left is None or \
                          self.root.left.wrap_into_structure().is_balanced()
            right_result = self.root.right is None or \
                           self.root.right.wrap_into_structure().is_balanced()
            return left_result and right_result
        return False

    def get_depth(self):
        # run a depth first search to count the deepness
        def __dfs_recursive_counter(node_data_structure, visited=None):
            if visited is None:
                # avoid infinite recursion in cyclic, trees are not cyclic though
                visited = set()
            visiting = node_data_structure.get_first_node()
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

    def invert(self):
        # run BFS to swap all elements
        visited = set()  # to avoid visiting the same twice
        to_visit = Queue(first_el=self.get_first_node())
        while len(to_visit) > 0:
            visiting = to_visit.pop()
            if visiting not in visited:  # visit just if not visited
                visited.add(visiting)  # mark as visited
                tmp_node = visiting.left  # visiting / inverting
                visiting.left = visiting.right
                visiting.right = tmp_node
                for branch in visiting.get_next_nodes():
                    to_visit.push(branch)  # add children to visit

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
                queue = Queue(first_el=node_data_structure.get_first_node())
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

    def first_non_full_node(self):
        # run BFS search for the first node with available space
        visited = set()  # to avoid visiting the same twice
        to_visit = Queue(first_el=self.get_first_node())
        while len(to_visit) > 0:
            visiting = to_visit.pop()
            if visiting not in visited:  # visit just if not visited
                visited.add(visiting)  # mark as visited
                if not visiting.is_full():  # visiting / checking
                    return visiting
                for branch in visiting.get_next_nodes():
                    to_visit.push(branch)  # add children to visit
        return None

    def push_back(self, el_or_node):
        # run bfs to insert
        node_to_insert = el_or_node
        if not isinstance(node_to_insert, Node):
            node_to_insert = Node(el_or_node)
        parent_node = self.first_non_full_node()
        if parent_node.left is None:
            parent_node.left = node_to_insert
        elif parent_node.right is None:
            parent_node.right = node_to_insert

    def last_node_and_parent(self):
        # run bfs to find
        visited = set()  # to avoid visiting the same twice
        the_last = (self.get_first_node(), None)
        to_visit = Queue(first_el=the_last)
        while len(to_visit) > 0:
            visiting, parent = to_visit.pop()
            if visiting not in visited:  # visit just if not visited
                visited.add(visiting)  # mark as visited
                the_last = (visiting, parent)  # visiting / updating to_remove
                for branch in visiting.get_next_nodes():
                    to_visit.push((branch, visiting))  # add children to visit
        return the_last

    def pop_back(self):
        # run bfs to pop
        node_to_remove, parent_node = self.last_node_and_parent()
        if parent_node is None:
            self.root = None
        else:
            # the last node never has children
            if parent_node.left == node_to_remove:
                parent_node.left = None
            else:
                parent_node.right = None
        return node_to_remove.data

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
                if src_node.left is not None:
                    new_node.left = __copy(src_node.left, _equivalence)
                if src_node.right is not None:
                    new_node.right = __copy(src_node.right, _equivalence)
            else:
                # if already cloned this node just return its reference
                new_node = _equivalence[src_node]
            return new_node

        def __copy_node_without_branches(src_node):
            # just to copy with empty branches, those will be filled later
            dst_node = src_node.copy()
            dst_node.left = None
            dst_node.right = None
            return dst_node

        equivalence = {}  # create a dict to store the already cloned nodes
        new_root = __copy(self.root, equivalence)  # clone recursively
        return BinaryTree(root=new_root)  # return new tree

    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return False
        return self.breadth_first_search(string_output=True) == other.breadth_first_search(string_output=True)
