from algo_data_design.data_structures import BinaryTreeNode as Node, BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root)
        if not self.is_valid():
            self.validate()

    def find(self, el_data):
        """
        Time complexity:
            Best/Average: O(n*log(n)), tree must be balanced to achieve this, this tree does not balance itself automatically
            Worst: O(n), search in all nodes
        Space complexity: O(n)
        """
        if self.root is None:
            return None
        if self.root.data == el_data:
            return self.root
        if self.root.data > el_data and self.root.left is not None:
            return BinarySearchTree.weak_cast_from_binary_tree(self.root.left.wrap_into_structure()).find(el_data)
        if self.root.data < el_data and self.root.right is not None:
            return BinarySearchTree.weak_cast_from_binary_tree(self.root.right.wrap_into_structure()).find(el_data)
        return None

    def push_back(self, el_or_node):
        def __push_back(parent, to_insert):
            if parent is None:
                return to_insert
            if to_insert.data < parent.data:
                parent.left = __push_back(parent.left, to_insert)
            else:
                parent.right = __push_back(parent.right, to_insert)
            return parent

        node_to_insert = el_or_node
        if not isinstance(node_to_insert, Node):
            node_to_insert = Node(el_or_node)
        # run dfs to insert in order
        self.root = __push_back(self.root, node_to_insert)

    def min(self):
        if self.root.left is not None:
            return BinarySearchTree.weak_cast_from_binary_tree(self.root.left.wrap_into_structure()).min()
        return self.root

    def max(self):
        if self.root.right is not None:
            return BinarySearchTree.weak_cast_from_binary_tree(self.root.right.wrap_into_structure()).max()
        return self.root

    def pop(self, el):
        """
        Time complexity:
            Best/Average: O(n*log(n))
            Worst: O(n), search in all nodes
        Space complexity: O(n)
        """

        def __pop(checking_node, el_data):
            if checking_node is None:
                return None, None

            if checking_node.data > el_data and checking_node.left is not None:
                checking_node.left, removed_node = __pop(checking_node.left, el_data)
            elif checking_node.data < el_data and checking_node.right is not None:
                checking_node.right, removed_node = __pop(checking_node.right, el_data)
            else:
                removed_node = checking_node
                if checking_node.left is None:  # has no left child, then return right child or None
                    return checking_node.right, removed_node
                elif checking_node.right is None:  # has no right child, then return right child or None
                    return checking_node.left, removed_node
                else:  # has both children
                    # put the smallest value of the right side on the node to be deleted
                    smallest_node = BinarySearchTree.weak_cast_from_binary_tree(
                        checking_node.right.wrap_into_structure()).min()
                    checking_node.data = smallest_node.data

                    # delete the duplicated node
                    checking_node.right = __pop(checking_node.right, smallest_node.data)

            return checking_node, removed_node

        self.root, node = __pop(self.root, el)
        return node

    def pop_back(self):
        #  # run bfs to find the last, and them, dfs to pop
        # node,_=self.last_node_and_parent()
        # return self.pop(node.data)
        # since the last node is always the greatest we don't need the above stuff, we can safely remove it
        return super().pop_back()

    def is_valid(self):
        if self.root is None:
            return True
        results = [True]
        if self.root.left is not None:
            if self.root.left.data <= self.root.data:
                results.append(
                    BinarySearchTree.weak_cast_from_binary_tree(self.root.left.wrap_into_structure()).is_valid())
            else:
                return False

        if self.root.right is not None:
            if self.root.right.data >= self.root.data:
                results.append(
                    BinarySearchTree.weak_cast_from_binary_tree(self.root.right.wrap_into_structure()).is_valid())
            else:
                return False

        if self.root.left is not None and self.root.right is not None:
            results.append(self.root.left.data <= self.root.right.data)

        return all(results)

    def validate(self):
        nodes = self.breadth_first_search()
        self.root = Node(nodes[0].data)
        for node in nodes[1:]:
            self.push_back(node.data)

    def invert(self):
        raise Exception('Unsupported operation!')

    def copy(self):
        copied = super().copy()
        return BinarySearchTree.weak_cast_from_binary_tree(copied)

    def __copy__(self):
        return self.copy()

    def __eq__(self, other):
        if not isinstance(other, BinarySearchTree):
            return False
        return self.breadth_first_search(string_output=True) == other.breadth_first_search(string_output=True)

    @staticmethod
    def weak_cast_from_binary_tree(binary_tree):
        # I'm just lazy to override fully the copy functions and also to code an exclusive node for this tree
        casted = BinarySearchTree()
        casted.root = binary_tree.root
        return casted

    @staticmethod
    def strong_cast_from_binary_tree(binary_tree):
        casted = BinarySearchTree(root=binary_tree.root)
        return casted
