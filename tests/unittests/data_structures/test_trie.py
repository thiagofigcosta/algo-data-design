import unittest

from algo_data_design.data_structures import Trie


class TrieTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        text = 'english is weird, it can be understood through tough throughout thought, though'
        self.trie = Trie()
        for word in text.split():
            self.trie.insert(word)

    def tearDown(self, *args, **kwargs):
        pass  # nothing to flush or destroy

    def test_insert(self, *args, **kwargs):
        expected = "'*' | 't' 'i' 'n' | 'h' | 's' | 'i' | 'i' | 'c' | 'a' 's' | 'e' | 'g' | 'o'"
        trie = Trie()
        trie.insert('thiago')
        trie.insert('this')
        trie.insert('is')
        trie.insert('nice')
        self.assertEqual(expected, str(trie))
        self.assertEqual(4, trie.count_words())
        self.assertEqual(2, trie.root['t'].count)
        self.assertEqual(1, trie.root['i'].count)
        self.assertEqual(1, trie.root['n'].count)

        expected = "'*' | 'A' 'a' | 'A' | 'a' | 'A' | 'a'"
        trie = Trie(case_sensitive=True)
        trie.insert('AAA')
        trie.insert('aaa')
        self.assertEqual(expected, str(trie))

    def test_breadth_first_search(self, *args, **kwargs):
        expected = ['*', 'e', 'i', 'w', 'c', 'b', 'u', 't', 'n', 's', 't', 'e', 'a', 'e', 'n', 'h', 'o', 'g', 'i', 'n',
                    'd', 'r', 'o', 'u', 'l', 'r', 'e', 'o', 'u', 'g', 'i', 'd', 'r', 'u', 'g', 'h', 's', 's', 'g', 'h',
                    'h', 't', 'h', 't', 'o', 'o', 'o', 'u', 'd', 't']
        actual = self.trie.breadth_first_search(string_output=True)
        self.assertEqual(expected, actual)

    def test_copy(self, *args, **kwargs):
        tree = self.trie.copy()
        tree_to_change = self.trie.copy()
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         tree_to_change.breadth_first_search(string_output=True))
        self.assertEqual(tree.breadth_first_search(string_output=True),
                         self.trie.breadth_first_search(string_output=True))
        reference_to_tree_to_change = tree_to_change
        self.assertEqual(reference_to_tree_to_change.root.char, tree_to_change.root.char)
        tree_to_change.root.char = 'X'
        self.assertEqual('X', tree_to_change.root.char)
        self.assertEqual('X', reference_to_tree_to_change.root.char)
        self.assertNotEqual('X', tree.root.char)

    def test_height(self, *args, **kwargs):
        self.assertEqual(11, self.trie.get_height())

    def test_width(self, *args, **kwargs):
        self.assertEqual(10, self.trie.get_width())

    def test_count_words(self, *args, **kwargs):
        self.assertEqual(12, self.trie.count_words())

    def test_count_chars(self, *args, **kwargs):
        self.assertEqual(49, self.trie.count_chars())
        self.assertEqual(16, self.trie.count_chars(unique=True))

    def test_search(self, *args, **kwargs):
        self.assertTrue(self.trie.search("ENGLISH"))
        self.assertTrue(self.trie.search("throughout"))
        self.assertFalse(self.trie.search("ENGLIS"))
        self.assertFalse(self.trie.search("JOAQUIN"))
        self.assertFalse(self.trie.search(""))

    def test_starts_with(self, *args, **kwargs):
        self.assertTrue(self.trie.starts_with("ENGLISH"))
        self.assertTrue(self.trie.starts_with("throughout"))
        self.assertTrue(self.trie.starts_with("ENGLIS"))
        self.assertFalse(self.trie.starts_with("JOAQUIN"))
        self.assertTrue(self.trie.starts_with(""))


if __name__ == '__main__':
    unittest.main()
