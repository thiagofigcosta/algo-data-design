import unittest

from algo_data_design.algorithms import graph
from algo_data_design.data_structures import Graph


class GraphAlgorithmsTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.graph_1 = Graph()
        for i in range(8):
            self.graph_1.add_node(i)
        # node 7 is unreachable
        self.graph_1.add_connection(0, 1, 2)
        self.graph_1.add_connection(0, 2, 6)
        self.graph_1.add_connection(1, 3, 5)
        self.graph_1.add_connection(2, 3, 8)
        self.graph_1.add_connection(3, 5, 15)
        self.graph_1.add_connection(3, 4, 10)
        self.graph_1.add_connection(5, 4, 6)
        self.graph_1.add_connection(5, 6, 6)
        self.graph_1.add_connection(4, 6, 2)

        self.graph_2 = Graph()
        for i in range(8):
            self.graph_2.add_node(i)
        # node 7 is unreachable
        self.graph_2.add_connection(0, 1, 28)
        self.graph_2.add_connection(0, 5, 10)
        self.graph_2.add_connection(5, 4, 25)
        self.graph_2.add_connection(4, 3, 22)
        self.graph_2.add_connection(4, 6, 24)
        self.graph_2.add_connection(3, 6, 18)
        self.graph_2.add_connection(3, 2, 12)
        self.graph_2.add_connection(6, 1, 14)
        self.graph_2.add_connection(1, 2, 16)

        self.graph_linear = Graph()
        for i in range(4):
            self.graph_linear.add_node(i)
        self.graph_linear.add_connection(0, 1)
        self.graph_linear.add_connection(0, 3)
        self.graph_linear.add_connection(1, 3)
        self.graph_linear.add_connection(2, 0)

    def tearDown(self, *args, **kwargs):
        pass

    def test_dijkstra(self, *args, **kwargs):
        expected_distances = {0: 0, 1: 2, 2: 6, 3: 7, 4: 17, 5: 22, 6: 19}
        for method in graph.DijkstraMethod.get_all_methods():
            distances = graph.dijkstra_shortest_path(self.graph_1, 0, method=method)
            actual_distances = graph.replace_node_key_by_data_key(distances)
            self.assertEqual(expected_distances, actual_distances)

    def test_dijkstra_with_dst(self, *args, **kwargs):
        expected_distance = 22
        for method in graph.DijkstraMethod.get_all_methods():
            self.assertEqual(expected_distance, graph.dijkstra_shortest_path(self.graph_1, 0, 5, method=method))

    def test_union_find(self):
        self.assertEqual(self.graph_1.has_circle(), graph.has_circle_union_find(self.graph_1))
        self.assertEqual(self.graph_2.has_circle(), graph.has_circle_union_find(self.graph_2))
        self.assertEqual(self.graph_linear.has_circle(), graph.has_circle_union_find(self.graph_linear))

    def test_minimum_spanning_tree(self, *args, **kwargs):
        expected_cost = 99
        expected_tree = "0:\n\t--10--> 5\n1:\n\t--14--> 6\n\t--16--> 2\n2:\n\t--12--> 3\n\t--16--> 1\n3:\n\t" \
                        "--12--> 2\n\t--22--> 4\n4:\n\t--22--> 3\n\t--25--> 5\n5:\n\t--10--> 0\n\t--25--> 4\n" \
                        "6:\n\t--14--> 1\n7:\n"
        for method in graph.MinimumSpanningTreeMethod.get_all_methods():
            tree, cost = graph.minimum_spanning_tree(self.graph_2, get_cost=True, method=method)
            self.assertEqual(expected_cost, cost)
            self.assertEqual(expected_tree, str(tree))


if __name__ == '__main__':
    unittest.main()
