import algo_data_design.utils.random as u_random


class Connection(object):
    def __init__(self, node, weight=1):
        if not isinstance(node, Node):
            raise Exception('Provide a Node object')
        if weight <= 0:
            raise Exception('Weight must be a positive number')
        self.node = node
        self.weight = weight


class Node(object):
    def __init__(self, data=None, connections=None):
        if connections is None:
            connections = []
        else:
            for el in connections:
                if not isinstance(el, Connection):
                    raise Exception('Adjacency list must be an iterable containing Connections')
        self.data = data
        self._uuid = u_random.random_uuid()
        self.connections = connections  # adjacency_list

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
                node = Node(copy_func_func(self.data),
                            [connection.deepcopy() if nested_deep_copy else connection.copy() for connection in
                             self.connections])
                break
        if node is None:
            node = self.copy()
        node._uuid = self._uuid  # here I want to copy the uuid
        return node

    def copy_without_connection(self):
        # I don't want to copy the uuid here
        return Node(self.data, [])

    def copy(self):
        # I don't want to copy the uuid here
        return Node(self.data, self.connections.copy())

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        next_nodes = [node_and_weight.node for node_and_weight in self.connections]
        return next_nodes

    def wrap_into_structure(self):
        # mandatory to run bfs and dfs
        return Graph(nodes=[self])


class Graph(object):
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes
        if len(nodes) == 1:
            self._starting_node = nodes[0]
        else:
            self._starting_node = None

    @staticmethod
    def build_from_matrix(matrix, node_map=None):
        if node_map is None:
            node_map = list(range(len(matrix)))
        nodes = []
        for i in range(len(node_map)):
            nodes.append(Node(node_map[i]))
        graph = Graph(nodes=nodes)
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell > 0:
                    graph.add_connection(nodes[r], nodes[c], cell, bidirectional=False)
        return graph

    def get_node(self, data):
        for node in self.nodes:
            if node.data == data:
                return node
        return None

    def add_node(self, data_or_node):
        node = data_or_node
        if not isinstance(data_or_node, Node):
            node = Node(data_or_node)
        if node not in self.nodes:
            self.nodes.append(node)
        self._starting_node = None

    def add_connection(self, data_or_node_1, data_or_node_2, weight=1, bidirectional=True):
        node_1 = data_or_node_1
        if not isinstance(data_or_node_1, Node):
            node_1 = self.get_node(data_or_node_1)
        node_2 = data_or_node_2
        if not isinstance(data_or_node_2, Node):
            node_2 = self.get_node(data_or_node_2)
        if node_1 is None or node_2 is None or node_1 not in self.nodes or node_2 not in self.nodes:
            raise Exception('Please provides nodes contained in the graph')
        node_1.connections.append(Connection(node_2, weight))
        if bidirectional:
            node_2.connections.append(Connection(node_1, weight))

    def __str__(self):
        string = ''
        for node in self.nodes:
            string = f'{string}{node.data}:\n'
            for conn in node.connections:
                string = f'{string}\t--{conn.weight}--> {conn.node.data}\n'
        return string

    def count(self):
        return len(self.nodes)

    def __len__(self):
        return self.count()

    def get_first_node(self):
        # mandatory to run bfs and dfs
        return self._starting_node

    def get_next_nodes(self):
        # mandatory to run bfs and dfs
        return self._starting_node.get_next_nodes()

    def depth_first_search(self, starting_node_or_data, string_output=False, recursive=False):
        self._set_starting_node(starting_node_or_data)
        from algo_data_design.algorithms.searching import dfs_itr, dfs_rec
        if recursive:
            return dfs_rec(self, string_output=string_output)
        else:
            return dfs_itr(self, string_output=string_output)

    def breadth_first_search(self, starting_node_or_data, string_output=False, recursive=False):
        self._set_starting_node(starting_node_or_data)
        from algo_data_design.algorithms.searching import bfs_itr, bfs_rec
        if recursive:
            return bfs_rec(self, string_output=string_output)
        else:
            return bfs_itr(self, string_output=string_output)

    def _set_starting_node(self, starting_node_or_data):
        node = starting_node_or_data
        if not isinstance(starting_node_or_data, Node):
            node = self.get_node(starting_node_or_data)
        if node is None or node not in self.nodes:
            raise Exception('Please provides nodes contained in the graph')
        self._starting_node = node

    def __copy__(self):
        return self.copy()

    def copy(self):
        def __copy(_nodes, _equivalence):
            _new_nodes = []
            for node in _nodes:  # copy all node
                new_node = node.copy_without_connection()
                _equivalence[node] = new_node  # store it on equivalence table
                _new_nodes.append(new_node)
            for n, node in enumerate(_nodes):
                for conn in node.connections:
                    _new_nodes[n].connections.append(Connection(_equivalence[conn.node], conn.weight))
            return _new_nodes

        equivalence = {}  # create a dict to store the already cloned nodes
        nodes = __copy(self.nodes, equivalence)  # clone recursively
        return Graph(nodes=nodes)  # return new tree

    def to_matrix(self):
        amount_nodes = len(self)
        matrix = [[0] * amount_nodes for _ in range(amount_nodes)]
        node_data_map = []
        node_index_map = {}
        for n, node in enumerate(self.nodes):
            node_index_map[node] = n
            node_data_map.append(node.data)
        for node in self.nodes:
            for conn in node.connections:
                if matrix[node_index_map[node]][node_index_map[conn.node]] == 0:
                    matrix[node_index_map[node]][node_index_map[conn.node]] = conn.weight
                else:
                    raise Exception('This node cannot be represented with a 2D matrix')
        return matrix, node_data_map

    def __eq__(self, other):
        if not isinstance(other, Graph):
            return False
        return str(self) == str(other)
