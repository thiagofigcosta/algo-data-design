import unittest

from algo_data_design.data_structures import Graph, GraphNode as Node, GraphConnection as Conn


class GraphTest(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        node_0 = Node(0)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        conn_0 = [Conn(node_1), Conn(node_3)]
        conn_1 = [Conn(node_2)]
        conn_2 = [Conn(node_0)]
        conn_3 = [Conn(node_0)]
        node_0.connections = conn_0
        node_1.connections = conn_1
        node_2.connections = conn_2
        node_3.connections = conn_3
        self.graph_circle = Graph(nodes=[node_0, node_1, node_2, node_3])
        node_0 = Node(0)
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        conn_0 = [Conn(node_1), Conn(node_3)]
        conn_1 = [Conn(node_3)]
        conn_2 = [Conn(node_0)]
        node_0.connections = conn_0
        node_1.connections = conn_1
        node_2.connections = conn_2
        self.graph_linear = Graph(nodes=[node_0, node_1, node_2, node_3])

    def tearDown(self, *args, **kwargs):
        pass

    def test_construction(self, *args, **kwargs):
        graph = Graph()
        for i in range(1, 6, 1):
            graph.add_node(i)
        graph.add_connection(1, 2)
        graph.add_connection(2, 3)
        graph.add_connection(3, 1)
        graph.add_connection(1, 4, bidirectional=False)
        graph.add_connection(4, 5)
        expected_graph = "1:\n\t--1--> 2\n\t--1--> 3\n\t--1--> 4\n2:\n\t--1--> 1\n\t--1--> 3\n3:\n\t--1--> 2\n\t" \
                         "--1--> 1\n4:\n\t--1--> 5\n5:\n\t--1--> 4\n"
        self.assertEqual(expected_graph, str(graph))

    def test_construction_conn_fail(self, *args, **kwargs):
        graph = Graph()
        self.assertRaises(Exception, graph.add_connection, 1, 2)

    def test_copy(self, *args, **kwargs):
        graph = self.graph_circle.copy()
        graph_to_change = self.graph_circle.copy()
        for i in range(len(graph.nodes)):
            self.assertNotEqual(graph.nodes[i], graph_to_change.nodes[i])
        self.assertEqual(graph, graph_to_change)
        self.assertEqual(graph, self.graph_circle)
        reference_graph_to_change = graph_to_change
        self.assertEqual(reference_graph_to_change.nodes[0].data, graph_to_change.nodes[0].data)
        graph_to_change.nodes[0].data = 50
        self.assertEqual(50, graph_to_change.nodes[0].data)
        self.assertEqual(50, reference_graph_to_change.nodes[0].data)
        self.assertNotEqual(50, graph.nodes[0].data)

    def test_copy_preserving_node_uuid(self, *args, **kwargs):
        graph = self.graph_circle.copy_preserving_node_uuid()
        graph_to_change = self.graph_circle.copy_preserving_node_uuid()
        for i in range(len(graph.nodes)):
            self.assertEqual(graph.nodes[i], graph_to_change.nodes[i])
        self.assertEqual(graph, graph_to_change)
        self.assertEqual(graph, self.graph_circle)
        reference_graph_to_change = graph_to_change
        self.assertEqual(reference_graph_to_change.nodes[0].data, graph_to_change.nodes[0].data)
        graph_to_change.nodes[0].data = 50
        self.assertEqual(50, graph_to_change.nodes[0].data)
        self.assertEqual(50, reference_graph_to_change.nodes[0].data)
        self.assertNotEqual(50, graph.nodes[0].data)

    def test_to_matrix(self, *args, **kwargs):
        expected_matrix = [[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
        expected_map = [0, 1, 2, 3]
        matrix, node_map = self.graph_circle.to_matrix()
        self.assertEqual(expected_matrix, matrix)
        self.assertEqual(expected_map, node_map)

    def test_from_matrix(self, *args, **kwargs):
        matrix = [[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
        self.assertEqual(self.graph_circle, Graph.build_from_matrix(matrix))

    def test_to_matrix_3d_fail(self, *args, **kwargs):
        graph = self.graph_circle.copy()
        graph.add_connection(1, 2, weight=3)
        self.assertRaises(Exception, graph.to_matrix)

    def test_dfs_and_bfs(self):
        self.assertEqual('0 -> 1 -> 3 -> 2', self.graph_circle.breadth_first_search(0, string_output=True))
        self.assertEqual('0 -> 1 -> 2 -> 3', self.graph_circle.depth_first_search(0, string_output=True))

    def test_remove_connection(self):
        graph = self.graph_circle.copy()
        expected_graph_0 = "0:\n\t--1--> 1\n\t--1--> 3\n1:\n\t--1--> 2\n2:\n\t--1--> 0\n3:\n\t--1--> 0\n"
        self.assertEqual(expected_graph_0, str(graph))
        graph.remove_connection(0, 3)
        expected_graph_1 = "0:\n\t--1--> 1\n1:\n\t--1--> 2\n2:\n\t--1--> 0\n3:\n"
        self.assertEqual(expected_graph_1, str(graph))
        graph = self.graph_circle.copy()
        graph.remove_connection(0, 3, bidirectional=False)
        expected_graph_2 = "0:\n\t--1--> 1\n1:\n\t--1--> 2\n2:\n\t--1--> 0\n3:\n\t--1--> 0\n"
        self.assertEqual(expected_graph_2, str(graph))

    def test_pop_node_and_contains(self):
        graph = self.graph_circle.copy()
        expected_graph_0 = "0:\n\t--1--> 1\n\t--1--> 3\n1:\n\t--1--> 2\n2:\n\t--1--> 0\n3:\n\t--1--> 0\n"
        self.assertEqual(expected_graph_0, str(graph))
        popped = graph.pop_node(0)
        self.assertEqual(0, popped.data)
        self.assertFalse(graph.contains(0))
        expected_graph_1 = "1:\n\t--1--> 2\n2:\n3:\n"
        self.assertEqual(expected_graph_1, str(graph))

    def test_has_circle(self):
        has_circle, circle = self.graph_circle.has_circle(get_circle=True, recursive=False)
        self.assertTrue(has_circle)
        self.assertEqual({0, 1, 2}, set([el.data for el in circle]))
        self.assertFalse(self.graph_linear.has_circle())

        has_circle, circle = self.graph_circle.has_circle(get_circle=True, recursive=True)
        self.assertTrue(has_circle)
        self.assertEqual({0, 1, 2}, set([el.data for el in circle]))
        self.assertFalse(self.graph_linear.has_circle(recursive=True))


if __name__ == '__main__':
    unittest.main()
