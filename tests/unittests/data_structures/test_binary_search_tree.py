import unittest

from algo_data_design.data_structures import BinarySearchTree, BinaryTree, BinaryTreeNode as Node


class BinarySearchTreeTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        self.tree_1 = BinarySearchTree(
            Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6))))
        self.tree_2 = BinarySearchTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6))))
        self.tree_3 = BinarySearchTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5))))
        self.tree_4 = BinarySearchTree(
            Node(0, Node(1, Node(2), Node(3)), Node(4, Node(5), Node(6, Node(2), Node(3)))))
        self.tree_5 = BinarySearchTree(  # balanced
            Node(3, Node(1, Node(0), Node(2)), Node(5, Node(4), Node(6))))

    def tearDown(self, *args, **kwargs):
        pass

    def test_init_validate(self, *args, **kwargs):
        expected_1 = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        expected_2 = '0 -> 1 -> 4 -> 2 -> 5 -> 3 -> 6'
        expected_3 = '0 -> 1 -> 4 -> 2 -> 5 -> 3'
        expected_4 = '0 -> 1 -> 4 -> 2 -> 5 -> 3 -> 6 -> 2 -> 3'
        expected_5 = '3 -> 1 -> 5 -> 0 -> 2 -> 4 -> 6'
        bfs_out = self.tree_1.breadth_first_search(string_output=True)
        self.assertEqual(expected_1, bfs_out)
        bfs_out = self.tree_2.breadth_first_search(string_output=True)
        self.assertEqual(expected_2, bfs_out)
        bfs_out = self.tree_3.breadth_first_search(string_output=True)
        self.assertEqual(expected_3, bfs_out)
        bfs_out = self.tree_4.breadth_first_search(string_output=True)
        self.assertEqual(expected_4, bfs_out)
        bfs_out = self.tree_5.breadth_first_search(string_output=True)
        self.assertEqual(expected_5, bfs_out)

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
        bfs_out = BinarySearchTree().breadth_first_search(string_output=True)
        self.assertEqual(expected, bfs_out)
        bfs_out = BinarySearchTree().breadth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, bfs_out)

    def test_dfs(self, *args, **kwargs):
        expected = '0 -> 1 -> 4 -> 2 -> 3 -> 5 -> 6'
        dfs_out = self.tree_2.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)

        dfs_out = self.tree_2.depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

    def test_dfs_empty(self, *args, **kwargs):
        expected = ''
        dfs_out = BinarySearchTree().depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)
        dfs_out = BinarySearchTree().depth_first_search(string_output=True, recursive=True)
        self.assertEqual(expected, dfs_out)

    def test_height(self, *args, **kwargs):
        expected = 7
        actual = self.tree_1.get_height()
        self.assertEqual(expected, actual)

    def test_width(self, *args, **kwargs):
        expected = 1
        actual = self.tree_1.get_width()
        self.assertEqual(expected, actual)

    def test_count(self, *args, **kwargs):
        expected = 7
        actual = self.tree_1.count()
        self.assertEqual(expected, actual)
        actual = self.tree_2.count()
        self.assertEqual(expected, actual)
        self.assertEqual(0, BinarySearchTree().count())
        expected = 9
        actual = self.tree_4.count()
        self.assertEqual(expected, actual)

    def test_invert(self, *args, **kwargs):
        tree = self.tree_2.copy()
        self.assertRaises(Exception, tree.invert)

    def test_full_binary_tree(self, *args, **kwargs):
        self.assertFalse(self.tree_1.is_full())
        self.assertFalse(self.tree_2.is_full())
        self.assertFalse(self.tree_3.is_full())
        self.assertFalse(self.tree_4.is_full())
        self.assertTrue(self.tree_5.is_full())

    def test_perfect_binary_tree(self, *args, **kwargs):
        self.assertFalse(self.tree_1.is_perfect())
        self.assertFalse(self.tree_2.is_perfect())
        self.assertFalse(self.tree_3.is_perfect())
        self.assertFalse(self.tree_4.is_perfect())
        self.assertTrue(self.tree_5.is_full())

    def test_push_back(self, *args, **kwargs):
        tree = self.tree_2.copy()
        tree.push_back(11)
        tree.push_back(13)
        tree.push_back(-1)
        tree.push_back(-2)
        tree.push_back(-3)
        tree.push_back(-4)
        tree.push_back(-5)
        tree.push_back(-6)
        expected = '0 -> -1 -> -2 -> -3 -> -4 -> -5 -> -6 -> 1 -> 4 -> 2 -> 3 -> 5 -> 6 -> 11 -> 13'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected, dfs_out)
        self.assertTrue(tree.is_valid())

    def test_pop_back(self, *args, **kwargs):
        tree = self.tree_2.copy()
        tree.push_back(11)
        expected_el = 11
        actual_el = tree.pop_back()
        expected_tree = '0 -> 1 -> 4 -> 2 -> 3 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected_el, actual_el)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

        expected_el = 6
        actual_el = tree.pop_back()
        expected_tree = '0 -> 1 -> 4 -> 2 -> 3 -> 5'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(expected_el, actual_el)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

    def test_complete_binary_tree(self, *args, **kwargs):
        self.assertFalse(self.tree_1.is_complete())
        self.assertFalse(self.tree_2.is_complete())
        self.assertFalse(self.tree_3.is_complete())
        self.assertFalse(self.tree_4.is_complete())
        self.assertTrue(self.tree_5.is_complete())

    def test_balanced_binary_tree(self, *args, **kwargs):
        self.assertFalse(self.tree_1.is_balanced())
        self.assertFalse(self.tree_2.is_balanced())
        self.assertFalse(self.tree_3.is_balanced())
        self.assertFalse(self.tree_4.is_balanced())
        self.assertTrue(self.tree_5.is_balanced())

    def test_find(self, *args, **kwargs):
        to_find = 5
        found = self.tree_1.find(to_find)
        self.assertEqual(to_find, found.data)
        found = self.tree_1.find(5000)
        self.assertIsNone(found)

    def test_min_max(self, *args, **kwargs):
        self.assertEqual(0, self.tree_1.min().data)
        self.assertEqual(6, self.tree_1.max().data)

        self.assertEqual(0, self.tree_2.min().data)
        self.assertEqual(6, self.tree_2.max().data)

        self.assertEqual(0, self.tree_3.min().data)
        self.assertEqual(5, self.tree_3.max().data)

        self.assertEqual(0, self.tree_4.min().data)
        self.assertEqual(6, self.tree_4.max().data)

        self.assertEqual(0, self.tree_5.min().data)
        self.assertEqual(6, self.tree_5.max().data)

    def test_pop(self, *args, **kwargs):
        tree = self.tree_2.copy()
        to_pop = 3
        actual_el = tree.pop(to_pop)
        expected_tree = '0 -> 1 -> 4 -> 2 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(to_pop, actual_el.data)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

        to_pop = 0
        actual_el = tree.pop(to_pop)
        expected_tree = '1 -> 4 -> 2 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(to_pop, actual_el.data)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

        to_pop = 2
        actual_el = tree.pop(to_pop)
        expected_tree = '1 -> 4 -> 5 -> 6'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(to_pop, actual_el.data)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

        to_pop = 6
        actual_el = tree.pop(to_pop)
        expected_tree = '1 -> 4 -> 5'
        dfs_out = tree.depth_first_search(string_output=True)
        self.assertEqual(to_pop, actual_el.data)
        self.assertEqual(expected_tree, dfs_out)
        self.assertTrue(tree.is_valid())

    def test_strong_cast(self, *args, **kwargs):
        tree_1 = BinarySearchTree.strong_cast_from_binary_tree(BinaryTree(
            Node(0, Node(1, Node(3), Node(4)), Node(2, Node(5), Node(6)))))
        expected_1 = '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
        bfs_out = tree_1.breadth_first_search(string_output=True)
        self.assertEqual(expected_1, bfs_out)


if __name__ == '__main__':
    unittest.main()
