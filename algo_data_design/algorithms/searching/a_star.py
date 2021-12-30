import math
from enum import Enum, auto as enum_auto

from algo_data_design.data_structures import PriorityQueue

X_INDEX = 0
Y_INDEX = 1
LATERAL_COST = 1
DIAGONAL_COST = 1.41421356237  # diagonal of square, sqrt(2)
MAX_BLOCKED_GRID_VALUE = 0  # positive values are paths, negative or zero are blocked


class Metadata(object):
    def __init__(self, parent=None, g=0.0, h=0.0, f=0.0):
        self.parent = parent
        self.f = f  # final cost
        self.g = g  # graph cost
        self.h = h  # heuristic

    def compute_f(self):
        self.f = self.g + self.h


class Heuristic(object):
    class Type(Enum):
        DISTANCE = enum_auto()

        @staticmethod
        def get_all_methods():
            return list(map(lambda c: c, Heuristic.Type))

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

    def __init__(self, type=Type.DISTANCE):
        if not isinstance(type, Heuristic.Type):
            raise Exception('Invalid heuristic type')
        self.type = type

    def __eq__(self, other):
        if not isinstance(other, Heuristic):
            return False
        return self.type == other.type

    def calc(self, point_or_node, destination):
        is_point = type(point_or_node) in (tuple, list)
        if self.type == Heuristic.Type.DISTANCE:
            # distance between points
            if is_point:
                x_diff_squared = (point_or_node[X_INDEX] - destination[X_INDEX]) ** 2
                y_diff_squared = (point_or_node[Y_INDEX] - destination[Y_INDEX]) ** 2
                g = math.sqrt(x_diff_squared + y_diff_squared)
            else:
                raise Exception('Not implemented yet')
        else:
            raise Exception(f'Unknown method {self.type}')
        return g


def a_star_grid_search(grid_2d, start_point, goal_point, heuristic=Heuristic.Type.DISTANCE):
    """
    Algorithm to find the shortest path between two points in a grid / map or graph also can be used to traverse a graph
    It is similar to dijkstra, but it as a heuristic to guide it. It maps all possible movements and chose the cheapest
    one based on f(n), where f(n) = g(n) + h(n), g(n) is the cost to move to the next node (n) and h(n) is a heuristic
    that estimates the cost of moving to next node (n)
    Indicated for: path find in grid and graph traversal
    Time Complexity: O() ??
    Space Complexity: O(n^2), where n is the amount of points ??
    """
    _validate_inputs(grid_2d, start_point, goal_point)

    open_list = PriorityQueue()  # this list stores the points to explore, the neighbors, the priority is the cost
    points_metadata = {}  # to store the points metadata, if a point is not here it not entered the open_list yet
    closed_list = set()  # this list stores already explored points

    points_metadata[start_point] = Metadata(start_point)
    open_list.append(start_point, priority=points_metadata[start_point].f)

    heuristic = Heuristic(heuristic)  # instantiate the heuristic
    while not open_list.is_empty():  # while there are points to explore
        exploring = open_list.pop()  # get the first point
        closed_list.add(exploring)  # mark point as explored
        neighbors = _generate_valid_neighbors(exploring, grid_2d)
        for neighbor, neighbor_g in neighbors:
            if neighbor == goal_point:
                # found the path
                points_metadata[goal_point] = Metadata(exploring)  # add the goal on the metadata to compute path
                return _compute_path(points_metadata, start_point, goal_point)
            elif neighbor not in closed_list:  # if we not visited this neighbor yet
                neighbor_g += points_metadata[start_point].g  # previous path g cost + neighbor g cost
                neighbor_h = heuristic.calc(neighbor, goal_point)
                neighbor_f = neighbor_g + neighbor_h  # final neighbor cost

                # if is the first time that we compute this neighbor of this path for it is best than the previous
                # we put it on the open_list
                if neighbor not in points_metadata or neighbor_f < points_metadata[neighbor].f:
                    points_metadata[neighbor] = Metadata(exploring, neighbor_g, neighbor_h, neighbor_f)
                    open_list.append(neighbor, priority=neighbor_f)

    return None  # No path found


def _validate_inputs(grid_2d, start_point, goal_point):
    rows = len(grid_2d)
    columns = len(grid_2d[0])
    for row in grid_2d:
        if len(row) != columns:
            raise Exception('Every row of the grid must have the same size')
    if not _is_point_inside_grid(start_point, rows, columns):
        raise Exception('Invalid starting point coordinates')
    if not _is_point_inside_grid(goal_point, rows, columns):
        raise Exception('Invalid goal point coordinates')
    if _point_has_obstacle(start_point, grid_2d):
        raise Exception('Starting point inside obstacle')
    if _point_has_obstacle(goal_point, grid_2d):
        raise Exception('Goal point unreachable')


def _is_point_inside_grid(point, x_length, y_length):
    return 0 <= point[X_INDEX] < x_length and 0 <= point[Y_INDEX] < y_length


def _get_grid_value(point, grid_2d):
    return grid_2d[point[X_INDEX]][point[Y_INDEX]]


def _point_has_obstacle(point, grid_2d):
    return _get_grid_value(point, grid_2d) <= MAX_BLOCKED_GRID_VALUE


def _generate_valid_neighbors(point, grid_2d):
    # returns a list of all valid neighbors and their costs of a given point
    x_length = len(grid_2d)
    y_length = len(grid_2d[0])
    possible_neighbors = []
    valid_neighbors = []
    possible_neighbors.append(((point[X_INDEX] - 1, point[Y_INDEX] - 1), DIAGONAL_COST))
    possible_neighbors.append(((point[X_INDEX] - 1, point[Y_INDEX]), LATERAL_COST))
    possible_neighbors.append(((point[X_INDEX] - 1, point[Y_INDEX] + 1), DIAGONAL_COST))
    possible_neighbors.append(((point[X_INDEX], point[Y_INDEX] - 1), LATERAL_COST))
    possible_neighbors.append(((point[X_INDEX], point[Y_INDEX] + 1), LATERAL_COST))
    possible_neighbors.append(((point[X_INDEX] + 1, point[Y_INDEX] - 1), DIAGONAL_COST))
    possible_neighbors.append(((point[X_INDEX] + 1, point[Y_INDEX]), LATERAL_COST))
    possible_neighbors.append(((point[X_INDEX] + 1, point[Y_INDEX] + 1), DIAGONAL_COST))
    # test the validity of all possible neighbors
    for candidate_neighbor in possible_neighbors:
        neighbor_point = candidate_neighbor[0]
        if _is_point_inside_grid(neighbor_point, x_length, y_length) and \
                not _point_has_obstacle(neighbor_point, grid_2d):
            valid_neighbors.append(candidate_neighbor)

    return valid_neighbors


def _compute_path(metadata, start_point, goal_point):
    path = []
    cur_pointer = goal_point
    while cur_pointer != start_point:  # go reverse until find the start point
        path.append(cur_pointer)
        cur_pointer = metadata[cur_pointer].parent
    path.append(start_point)
    return path[::-1]  # reverse the list
