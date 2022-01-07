import algo_data_design.utils.random as u_random
import algo_data_design.utils.string as u_string
from algo_data_design.data_structures import Queue


class Node(object):
    WILDCARD = '*'

    def __init__(self, char, count=0, children=None, is_end=False):
        if children is None:
            children = {}
        self.is_end = is_end  # indicates if it is the end of the word
        self.children = children
        self.count = count
        self.char = char
        self._uuid = u_random.random_uuid()  # better to use uuid since it allows storage, for single run use id(self) or hex(id(self))

    def __str__(self):
        return self.char

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

    def __contains__(self, item):
        return self.children.__contains__(item)

    def __getitem__(self, item):
        return self.children[item]

    def __setitem__(self, key, value):
        self.children[key] = value

    def copy(self):
        # I don't want to copy the uuid here
        return Node(self.char, self.count, self.children.copy(), self.is_end)

    def get_degree(self):
        return len(self.children)


class Trie(object):
    # Data struct to store words, useful to search them later
    SEPARATOR = '|'

    def __init__(self, case_sensitive=False, sanitize_words=True, root=None):
        if root is None:
            root = Node(Node.WILDCARD)
        self.root = root
        self.case_sensitive = case_sensitive
        self.sanitize_words = sanitize_words

    def count_words(self):
        return self.root.count

    def insert(self, word):
        cur_node = self.root
        cur_node.count += 1  # count words
        if self.sanitize_words:  # remove accents and non letter/numbers
            word = u_string.strip_accents(word)
            word = u_string.strip_non_alpha(word)
        for char in word:
            if char not in cur_node:
                if not self.case_sensitive:
                    char = char.lower()  # to lower
                cur_node[char] = Node(char)  # create a new node
            cur_node = cur_node[char]
            cur_node.count += 1  # count amount of chars
        cur_node.is_end = True  # mark as word

    def _search_core(self, word_or_prefix, starts_with=False):
        cur_node = self.root
        if self.sanitize_words:  # remove accents and non letter/numbers
            word_or_prefix = u_string.strip_accents(word_or_prefix)
            word_or_prefix = u_string.strip_non_alpha(word_or_prefix)
        for char in word_or_prefix:
            if not self.case_sensitive:
                char = char.lower()  # to lower
            if char not in cur_node:
                return False
            cur_node = cur_node[char]
        return starts_with or cur_node.is_end

    def search(self, word):
        return self._search_core(word, False)

    def starts_with(self, prefix):
        return self._search_core(prefix, True)

    def breadth_first_search(self, add_separator=False, string_output=False):
        visited_order = []
        visited = set()  # to avoid visiting the same twice
        # use a queue to always retrieve the first added element, making it breadth
        to_visit = Queue(first_el=self.root)
        if add_separator:
            to_visit.push(Trie.SEPARATOR)  # just a separator for levels
        while len(to_visit) > 0:
            visiting = to_visit.pop()
            if type(visiting) is str:  # separator
                if type(visited_order[-1]) is not str:  # if there is not already a separator
                    visited_order.append(visiting)  # just a separator for levels
            else:
                if visiting not in visited:  # visit just if not visited
                    visited.add(visiting)  # mark as visited
                    visited_order.append(visiting)  # visit
                    for char in list(visiting.children.values()):
                        to_visit.push(char)  # add children to visit
                    if add_separator:
                        to_visit.push(Trie.SEPARATOR)  # just a separator for levels
        if add_separator and len(visited_order) > 0:
            del visited_order[-1]
        if string_output:
            visited_order = [el if type(el) is str else el.char for el in visited_order]
        return visited_order

    def get_depth(self):
        # run a depth first search to count the deepness
        def __dfs_recursive_counter(node, visited=None):
            if visited is None:
                # avoid infinite recursion in cyclic, trees are not cyclic though
                visited = set()
            visiting = node
            visited.add(visiting)
            depths = [0]  # base case of the recursion is 0
            for to_visit in list(visiting.children.values()):
                if to_visit not in visited:
                    depths.append(__dfs_recursive_counter(to_visit))  # get depth of each subtree
            depth = max(depths)  # select the maximum depth
            return depth + 1  # add one to it

        if self.root is None:
            return 0
        return __dfs_recursive_counter(self.root)

    def get_height(self):
        return self.get_depth()

    def get_width(self):
        # run a breadth first search to count the wideness
        def __bfs_count(node, queue=None, visited=None, results=None):
            if results is None:
                # create a dict to store the sum of the partial widths
                results = {}
            if visited is None:
                # avoid infinite recursion in cyclic, trees are not cyclic though
                visited = set()
            if queue is None:
                queue = Queue(first_el=node)
            if not queue.is_empty():
                visiting = queue.pop()
                visited.add(visiting)
                inverse_cur_level = Trie(root=visiting).get_depth()  # compute the depth of the current node
                if inverse_cur_level not in results:
                    results[inverse_cur_level] = 0
                results[inverse_cur_level] += len(
                    list(visiting.children.values()))  # sum every partial width of nodes on same depth
                for to_visit in list(visiting.children.values()):
                    if to_visit not in visited:
                        queue.append(to_visit)
                __bfs_count(node, queue, visited, results)
            return results

        if self.root is None:
            return 0
        dict_results = __bfs_count(self.root)
        depth = len(dict_results)
        array_results = [0] * depth
        max_width = 0
        for inverse_level, width in dict_results.items():
            level = depth - inverse_level
            array_results[level] = width
            max_width = max(max_width, width)
        return max_width

    def count_chars(self, unique=False):
        bfs = self.breadth_first_search(string_output=True)
        if unique:
            return len(set(bfs)) - 1  # minus root
        else:
            return len(bfs) - 1  # minus root

    def __len__(self):
        return self.count_chars()

    def __copy__(self):
        return self.copy()

    def copy(self):
        def __copy(src_node, _equivalence):
            if src_node not in _equivalence:
                # copy the node
                new_node = __copy_node_without_children(src_node)
                _equivalence[src_node] = new_node  # store it on equivalence table
                # to the same of its children
                for char, node in src_node.children.items():
                    new_node.children[char] = __copy(node, _equivalence)
            else:
                # if already cloned this node just return its reference
                new_node = _equivalence[src_node]
            return new_node

        def __copy_node_without_children(src_node):
            # just to copy with empty branches, those will be filled later
            dst_node = src_node.copy()
            dst_node.children = {}
            return dst_node

        equivalence = {}  # create a dict to store the already cloned nodes
        new_root = __copy(self.root, equivalence)  # clone recursively
        return Trie(case_sensitive=self.case_sensitive, sanitize_words=self.sanitize_words,
                    root=new_root)  # return new tree

    def __str__(self):
        bfs = self.breadth_first_search(add_separator=True, string_output=True)
        str_out = ''
        for el in bfs:
            if el == Trie.SEPARATOR:
                str_out += f' {Trie.SEPARATOR}'
            else:
                str_out += f' \'{el}\''
        return str_out.strip()
