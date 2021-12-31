from enum import Enum, auto as enum_auto


class DijkstraMethod(Enum):
    PRIORITY_QUEUE = enum_auto()
    REGULAR = enum_auto()

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, DijkstraMethod))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        # https://bugs.python.org/issue30545
        if not isinstance(other, Enum):
            return False
        self_dict = self.__dict__
        other_dict = other.__dict__
        return self_dict['_value_'] == other_dict['_value_'] and str(self_dict['__objclass__']) == str(
            other_dict['__objclass__'])


class MinimumSpanningTreeMethod(Enum):
    KRUSKAL = enum_auto()
    PRIM = enum_auto()

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, MinimumSpanningTreeMethod))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        # https://bugs.python.org/issue30545
        if not isinstance(other, Enum):
            return False
        self_dict = self.__dict__
        other_dict = other.__dict__
        return self_dict['_value_'] == other_dict['_value_'] and str(self_dict['__objclass__']) == str(
            other_dict['__objclass__'])


from .dijkstra import shortest_paths_cost, replace_node_key_by_data_key
from .union_find import union, find, has_circle as has_circle_union_find, Subset as UnionFindSubset
from .prim import minimum_spanning_tree as prim_minimum_spanning_tree
from .kruskal import minimum_spanning_tree as kruskal_minimum_spanning_tree
from .ford_fulkerson import maximum_flow
from .a_star import shortest_path, traverse as a_star_traverse
from .kosaraju import strongly_connected_components


def minimum_spanning_tree(graph, method=MinimumSpanningTreeMethod.KRUSKAL, get_cost=False, get_tree=True):
    if method == MinimumSpanningTreeMethod.KRUSKAL:
        return kruskal_minimum_spanning_tree(graph, get_cost=get_cost, get_tree=get_tree)
    elif method == MinimumSpanningTreeMethod.PRIM:
        return prim_minimum_spanning_tree(graph, get_cost=get_cost, get_tree=get_tree)
    else:
        raise Exception(f'Unknown method {method}')
