import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Maximum Depth of Binary Tree")
    print("Return the maximum depth of a binary tree")
    print("Examples:")
    print('\t[3,9,20,null,null,15,7] -> 3')
    print('\t[1,null,2] -> 2')


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def run(root):
    # Time complexity: O(v+e)
    # Space complexity: O(v)
    def __get_next_nodes(_node):
        next_nodes = []
        if _node.left is not None:
            next_nodes.append(_node.left)
        if _node.right is not None:
            next_nodes.append(_node.right)
        return next_nodes

    def __pop_from_stack(_stack):
        el = _stack[-1]  # get the last element from the stack
        del _stack[-1]  # remove the last
        return el

    # run dfs
    if root is None:
        return 0
    depth = 0
    visited = set()
    to_visit = [[0, root]]  # the first element is the current depth
    while len(to_visit) > 0:
        cur_depth, visiting = __pop_from_stack(to_visit)
        cur_depth += 1  # increase current depth
        depth = max(cur_depth, depth)  # updates the maximum depth
        visited.add(id(visiting))  # mark as visited, I'm using the memory address since multiple nodes can have the
        # same value and the id will not change during the same execution
        for next_node in __get_next_nodes(visiting):
            if id(next_node) not in visited:  # if not visited yet
                to_visit.append([cur_depth, next_node])  # to mark the start of the path
    return depth


def main():
    info()
    b_tree1 = Node(3)
    b_tree1.left = Node(9)
    b_tree1.right = Node(20)
    b_tree1.right.left = Node(15)
    b_tree1.right.right = Node(7)
    b_tree2 = Node(0)
    b_tree2.right = Node(0)
    test.assertEqual(3, run(b_tree1))
    test.assertEqual(2, run(b_tree2))
    test.assertEqual(0, run(None))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
