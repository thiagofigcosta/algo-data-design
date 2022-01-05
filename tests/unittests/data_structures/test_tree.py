import unittest

from algo_data_design.data_structures import Tree, TreeNode as Node


class TreeTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        self.tree_1 = Tree(
            Node(0, branches=[Node(1, branches=[Node(3), Node(4)]), Node(2, branches=[Node(5), Node(6)])]))
        self.tree_2 = Tree(
            Node(0, branches=[Node(1, branches=[Node(2), Node(3)]), Node(4, branches=[Node(5), Node(6)])]))
        root = Node(0)
        other_nodes = [Node(1, branches=[Node(3), Node(4), root]), Node(2, branches=[Node(5), Node(6), root])]
        root.branches = other_nodes
        self.this_is_not_a_tree_is_a_graph = Tree(root)

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_copy(self, *args, **kwargs):
        # using this circular graph to test the algorithm reliability
        tree = self.this_is_not_a_tree_is_a_graph.copy()
        tree_to_change = self.this_is_not_a_tree_is_a_graph.copy()
        self.assertEqual(tree.depth_first_search(string_output=True),
                         tree_to_change.depth_first_search(string_output=True))
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         tree_to_change.breadth_first_search(string_output=True))
        self.assertEqual(tree.depth_first_search(string_output=True),
                         self.this_is_not_a_tree_is_a_graph.depth_first_search(string_output=True))
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         self.this_is_not_a_tree_is_a_graph.breadth_first_search(string_output=True))
        reference_to_tree_to_change = tree_to_change
        self.assertEqual(reference_to_tree_to_change.root.data, tree_to_change.root.data)
        tree_to_change.root.data = 50
        self.assertEqual(50, tree_to_change.root.data)
        self.assertEqual(50, reference_to_tree_to_change.root.data)
        self.assertNotEqual(50, tree.root.data)

    def test_bfs(self, *args, **kwargs):
        expected = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        bfs_out = self.tree_1.breadth_first_search(string_output=True)
        self.assertEqual(expected, bfs_out)

        bfs_out = self.tree_1.breadth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, bfs_out)

    def test_bfs_empty(self, *args, **kwargs):
        expected = ''
        bfs_out = Tree().breadth_first_search(string_output=True)
        self.assertEqual(expected, bfs_out)
        bfs_out = Tree().breadth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, bfs_out)

    def test_dfs(self, *args, **kwargs):
        expected = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        dfs_out = self.tree_2.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)

        dfs_out = self.tree_2.depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

    def test_dfs_empty(self, *args, **kwargs):
        expected = ''
        dfs_out = Tree().depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)
        dfs_out = Tree().depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

    def test_forest(self, *args, **kwargs):
        forest = self.tree_1.to_forest()
        for i in range(len(forest)):
            self.assertEqual(Tree(self.tree_1.get_next_nodes()[i]).depth_first_search(), forest[i].depth_first_search())

    def test_height(self, *args, **kwargs):
        expected = 3
        actual = self.tree_1.get_height()
        self.assertEqual(expected, actual)

    def test_width(self, *args, **kwargs):
        expected = 4
        actual = self.tree_1.get_width()
        self.assertEqual(expected, actual)

    def test_count(self, *args, **kwargs):
        expected = 7
        actual = self.tree_1.count()
        self.assertEqual(expected, actual)
        actual = self.tree_2.count()
        self.assertEqual(expected, actual)
        self.assertEqual(0, Tree().count())

    def test_find(self, *args, **kwargs):
        to_find = 5
        found = self.tree_1.find_bfs(to_find)
        self.assertEqual(to_find, found.data)
        found = self.tree_1.find_bfs(5000)
        self.assertIsNone(found)

        found = self.tree_1.find_dfs(to_find)
        self.assertEqual(to_find, found.data)
        found = self.tree_1.find_dfs(5000)
        self.assertIsNone(found)

        found = self.tree_1.find(to_find)
        self.assertEqual(to_find, found.data)
        found = self.tree_1.find(5000)
        self.assertIsNone(found)


if __name__ == '__main__':
    unittest.main()
