import unittest

import algo_data_design.problems
import algo_data_design.utils.input as u_input

test = unittest.TestCase()


def info():
    print("Clone Graph")
    print("Run a deep clone on the given graph")
    print(
        "Definition for a Node.\nclass Node(object):\ndef __init__(self, val = 0, neighbors = None):\nself.val = val\n"
        "self.neighbors = neighbors if neighbors is not None else []")
    print("The graph can be None")
    print("Examples:")
    print('\t[[2,4],[1,3],[2,4],[1,3]] -> [[2,4],[1,3],[2,4],[1,3]]')
    print('\tNone -> None')


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def run_approach_1(node):
    # Time complexity: O(n*m), where n is the amount of nodes/vertices, and m the amount of edges
    # Space complexity: O(n)
    def __clone_without_neighbors(_node):
        return Node(_node.val, [])

    def __clone_recursive(_node, _clones_cache):
        if _node.val not in _clones_cache:
            new_node = __clone_without_neighbors(_node)
            _clones_cache[_node.val] = new_node
            for neighbor in _node.neighbors:
                new_node.neighbors.append(__clone_recursive(neighbor, _clones_cache))
        else:
            new_node = _clones_cache[_node.val]
        return new_node

    if node is None:
        return None
    clones_cache = {}
    n_node = __clone_recursive(node, clones_cache)
    return n_node


def run_approach_2(node):
    # Time complexity: O(n*m), where n is the amount of nodes/vertices, and m the amount of edges
    # Space complexity: O(n)
    def __clone_without_neighbors(_node):
        return Node(_node.val, [])

    def __clone_recursive(_node, _clones_cache):
        _clones_cache[_node.val] = __clone_without_neighbors(_node)
        for neighbor in _node.neighbors:
            if neighbor.val not in _clones_cache:
                _clones_cache[_node.val].neighbors.append(__clone_recursive(neighbor, _clones_cache))
            else:
                _clones_cache[_node.val].neighbors.append(_clones_cache[neighbor.val])
        return _clones_cache[_node.val]

    if node is None:
        return None
    clones_cache = {}
    n_node = __clone_recursive(node, clones_cache)
    return n_node


def create_node():
    node_1 = Node(1)
    node_2 = Node(1)
    node_3 = Node(1)
    node_4 = Node(1)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]
    return node_1


def assert_equal_but_not_same(original, new_graph, checked=None):
    if checked is None:
        checked = set()
    if original.val not in checked:
        checked.add(original.val)
        test.assertEqual(original.val, new_graph.val)
        test.assertEqual(len(original.neighbors), len(new_graph.neighbors))
        test.assertFalse(original is new_graph)
        for i in range(len(original.neighbors)):
            assert_equal_but_not_same(original.neighbors[i], new_graph.neighbors[i], checked)


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Approach 1')
        print('\t2 - Approach 2')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=2)
    if solution == 1:
        run = run_approach_1
    elif solution == 2:
        run = run_approach_2
    else:
        raise Exception('Unknown solution')
    info()
    test.assertEqual(None, run(None))
    original = create_node()
    new_graph = run(original)
    assert_equal_but_not_same(original, new_graph)
    print('All tests passed')


if __name__ == "__main__":
    main()
