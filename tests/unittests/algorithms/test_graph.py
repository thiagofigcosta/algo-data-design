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

        self.graph_3 = Graph()
        for i in range(6):
            self.graph_3.add_node(i)
        self.graph_3.add_connection(0, 1, 10, bidirectional=False)
        self.graph_3.add_connection(0, 2, 10, bidirectional=False)
        self.graph_3.add_connection(1, 2, 2, bidirectional=False)
        self.graph_3.add_connection(1, 3, 4, bidirectional=False)
        self.graph_3.add_connection(1, 4, 8, bidirectional=False)
        self.graph_3.add_connection(2, 4, 9, bidirectional=False)
        self.graph_3.add_connection(3, 5, 10, bidirectional=False)
        self.graph_3.add_connection(4, 3, 6, bidirectional=False)
        self.graph_3.add_connection(4, 5, 10, bidirectional=False)

        self.graph_linear = Graph()
        for i in range(4):
            self.graph_linear.add_node(i)
        self.graph_linear.add_connection(0, 1)
        self.graph_linear.add_connection(0, 3)
        self.graph_linear.add_connection(1, 3)
        self.graph_linear.add_connection(2, 0)

        # The grid with geolocations of the geo_referenced_graph
        # X = blocked path
        #  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | - coordinates
        # -|--------------------------------
        # 0| 6 |   | X |   |   | X | 4 |   |
        # -|--------------------------------
        # 1|   |   | 1 |   |   | 2 |   |   |
        # -|--------------------------------
        # 2|   | X | X | 3 |   |   |   | 5 |
        # -|--------------------------------
        # 3| 0 |   | X |   |   | X |   |   |
        # ----------------------------------
        self.geo_referenced_graph = Graph()
        self.nodes_coordinates = {}
        for i in range(7):
            self.geo_referenced_graph.add_node(i)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(6)] = (0, 0)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(4)] = (0, 6)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(1)] = (1, 2)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(2)] = (1, 5)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(3)] = (2, 3)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(5)] = (2, 7)
        self.nodes_coordinates[self.geo_referenced_graph.get_node(0)] = (3, 0)
        self.geo_referenced_graph.add_connection(6, 1, 3)
        self.geo_referenced_graph.add_connection(6, 0, 3)
        self.geo_referenced_graph.add_connection(0, 1, 4)
        self.geo_referenced_graph.add_connection(1, 3, 2)
        self.geo_referenced_graph.add_connection(1, 2, 3)
        self.geo_referenced_graph.add_connection(3, 5, 4)
        self.geo_referenced_graph.add_connection(3, 2, 3)
        self.geo_referenced_graph.add_connection(2, 4, 2)
        self.geo_referenced_graph.add_connection(4, 5, 3)

    def tearDown(self, *args, **kwargs):
        pass

    def test_dijkstra(self, *args, **kwargs):
        expected_distances = {0: 0, 1: 2, 2: 6, 3: 7, 4: 17, 5: 22, 6: 19}
        for method in graph.DijkstraMethod.get_all_methods():
            distances = graph.shortest_paths_cost(self.graph_1, 0, method=method)
            actual_distances = graph.replace_node_key_by_data_key(distances)
            self.assertEqual(expected_distances, actual_distances)

    def test_dijkstra_with_dst(self, *args, **kwargs):
        expected_distance = 22
        for method in graph.DijkstraMethod.get_all_methods():
            self.assertEqual(expected_distance, graph.shortest_paths_cost(self.graph_1, 0, 5, method=method))

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

    def test_maximum_flow(self, *args, **kwargs):
        graph_copy = self.graph_3.copy()
        expected_flux = 19
        self.assertEqual(expected_flux, graph.maximum_flow(self.graph_3, 0, 5))
        self.assertEqual(graph_copy, self.graph_3)  # make sure that this is not the residual

    def test_a_star(self, *args, **kwargs):
        expected_cost = 10
        expected_path = [0, 1, 3, 5]
        start_node = self.geo_referenced_graph.get_node(0)
        end_node = self.geo_referenced_graph.get_node(5)

        path, cost = graph.shortest_path(self.geo_referenced_graph, start_node, end_node, self.nodes_coordinates)
        path = [node.data for node in path]
        cost_dijkstra = graph.shortest_paths_cost(self.geo_referenced_graph, start_node, end_node)
        self.assertEqual(expected_cost, cost)
        self.assertEqual(expected_path, path)
        self.assertEqual(expected_cost, cost_dijkstra)

    def test_a_star_traverse(self, *args, **kwargs):
        start_node = self.geo_referenced_graph.get_node(6)
        end_coordinates = (3, 7)
        node_coordinates_with_end_point = self.nodes_coordinates.copy()
        node_coordinates_with_end_point[end_coordinates] = end_coordinates
        expected_order = [6, 1, 2, 3, 0, 5, 4]
        visiting_order = graph.a_star_traverse(self.geo_referenced_graph, start_node, end_coordinates,
                                               node_coordinates_with_end_point)
        visiting_order = [node.data for node in visiting_order]
        self.assertEqual(expected_order, visiting_order)


if __name__ == '__main__':
    unittest.main()
