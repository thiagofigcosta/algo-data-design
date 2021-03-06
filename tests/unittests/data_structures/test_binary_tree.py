import unittest

from algo_data_design.data_structures import BinaryTree, BinaryTreeNode as Node


class BinaryTreeTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        self.tree_1 = BinaryTree(
            Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))
        self.tree_2 = BinaryTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6))))
        self.tree_3 = BinaryTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5))))
        self.tree_4 = BinaryTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6, Node(2), Node(3)))))

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_copy(self, *args, **kwargs):
        # using this circular graph to test the algorithm reliability
        tree = self.tree_1.copy()
        tree_to_change = self.tree_1.copy()
        self.assertEqual(tree.depth_first_search(string_output=True),
                         tree_to_change.depth_first_search(string_output=True))
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         tree_to_change.breadth_first_search(string_output=True))
        self.assertEqual(tree.depth_first_search(string_output=True),
                         self.tree_1.depth_first_search(string_output=True))
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         self.tree_1.breadth_first_search(string_output=True))
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
        bfs_out = BinaryTree().breadth_first_search(string_output=True)
        self.assertEqual(expected, bfs_out)
        bfs_out = BinaryTree().breadth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, bfs_out)

    def test_dfs(self, *args, **kwargs):
        expected = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        dfs_out = self.tree_2.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)

        dfs_out = self.tree_2.depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

    def test_dfs_empty(self, *args, **kwargs):
        expected = ''
        dfs_out = BinaryTree().depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)
        dfs_out = BinaryTree().depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

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
        self.assertEqual(0, BinaryTree().count())
        expected = 9
        actual = self.tree_4.count()
        self.assertEqual(expected, actual)

    def test_invert(self, *args, **kwargs):
        tree = self.tree_2.copy()
        tree.invert()
        expected = '0 -> 4 -> 6 -> 5 -> 1 -> 3 -> 2'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)

    def test_full_binary_tree(self, *args, **kwargs):
        self.assertTrue(self.tree_1.is_full())
        self.assertTrue(self.tree_2.is_full())
        self.assertFalse(self.tree_3.is_full())
        self.assertTrue(self.tree_4.is_full())

    def test_perfect_binary_tree(self, *args, **kwargs):
        self.assertTrue(self.tree_1.is_perfect())
        self.assertTrue(self.tree_2.is_perfect())
        self.assertFalse(self.tree_3.is_perfect())
        self.assertFalse(self.tree_4.is_perfect())

    def test_push_back(self, *args, **kwargs):
        tree = self.tree_2.copy()
        tree.push_back(11)
        tree.push_back(13)
        expected = '0 -> 1 -> 2 -> 11 -> 13 -> 3 -> 4 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)

    def test_pop_back(self, *args, **kwargs):
        tree = self.tree_2.copy()
        tree.push_back(11)
        expected_el = 11
        actual_el = tree.pop_back()
        expected_tree = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected_el, actual_el)
        self.assertEqual(expected_tree, dfs_out)

        expected_el = 6
        actual_el = tree.pop_back()
        expected_tree = '0 -> 1 -> 2 -> 3 -> 4 -> 5'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected_el, actual_el)
        self.assertEqual(expected_tree, dfs_out)

    def test_complete_binary_tree(self, *args, **kwargs):
        self.assertTrue(self.tree_1.is_complete())
        self.assertTrue(self.tree_2.is_complete())
        self.assertTrue(self.tree_3.is_complete())
        self.assertFalse(self.tree_4.is_complete())

    def test_balanced_binary_tree(self, *args, **kwargs):
        self.assertTrue(self.tree_1.is_balanced())
        self.assertTrue(self.tree_2.is_balanced())
        self.assertTrue(self.tree_3.is_balanced())
        self.assertTrue(self.tree_4.is_balanced())

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
