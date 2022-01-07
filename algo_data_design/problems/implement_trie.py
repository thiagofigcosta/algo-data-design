import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Implement Trie (Prefix Tree)")
    print("Implement a trie :)")
    print('\t["Trie", "insert", "search", "search", "startsWith", "insert", "search"]')
    print('\t\t[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]] ')
    print('\t\t-> [null, null, true, false, true, null, true]')


class Node(object):
    def __init__(self, char):
        children = {}
        self.is_end = False  # indicates if it is the end of the word
        self.children = children
        self.count = 0
        self.char = char

    def __contains__(self, item):
        return self.children.__contains__(item)

    def __getitem__(self, item):
        return self.children[item]

    def __setitem__(self, key, value):
        self.children[key] = value


class Trie(object):

    def __init__(self):
        root = Node('')
        self.root = root

    def insert(self, word):
        cur_node = self.root
        cur_node.count += 1  # count words
        for char in word:
            if char not in cur_node:
                cur_node[char] = Node(char)  # create a new node
            cur_node = cur_node[char]
            cur_node.count += 1  # count amount of chars
        cur_node.is_end = True  # mark as word

    def _search_core(self, word_or_prefix, starts_with=False):
        cur_node = self.root
        for char in word_or_prefix:
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        return starts_with or cur_node.is_end

    def search(self, word):
        return self._search_core(word, False)

    def startsWith(self, prefix):
        return self._search_core(prefix, True)


def run():
    obj = Trie()
    obj.insert("apple")
    test.assertTrue(obj.search("apple"))
    test.assertFalse(obj.search("app"))
    test.assertTrue(obj.startsWith("app"))
    obj.insert("app")
    test.assertTrue(obj.search("app"))


def main():
    info()
    run()
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
