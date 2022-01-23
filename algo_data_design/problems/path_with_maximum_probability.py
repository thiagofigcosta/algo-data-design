import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Path with Maximum Probability")
    print("Given an undirected weighted graph, represented by an edge list with a probability of success of traversing")
    print("and edge represented by succ_prob.")
    print("Given two nodes, return the biggest path probability, if there is no path, return 0.")
    print("Examples:")
    print('\tnodes=3, edges = [[0,1],[1,2],[0,2]], succ_prob = [0.5,0.5,0.2], start = 0, end = 2 -> 0.25')
    print('\tnodes=3, edges = [[0,1],[1,2],[0,2]], succ_prob = [0.5,0.5,0.3], start = 0, end = 2 -> 0.3')
    print('\tnodes=3, edges = [[0,1]], succ_prob = [0.5], start = 0, end = 2 -> 0')


import heapq


class PriorityMaxQueue(object):

    def __init__(self):
        self.array = []

    def push(self, value, priority=0):
        heapq.heappush(self.array, (-priority, value))  # minus to act like a max queue

    def pop(self, retrieve_priority=False):
        priority, value = heapq.heappop(self.array)
        if retrieve_priority:
            return value, -priority  # minus to act like a max queue
        return value

    def __len__(self):
        return len(self.array)


def dijkstra_max(node_conns, starting_node):
    # Time complexity: O((v+e)*log(v)), where v is vertices and e is edges
    # Space complexity: O(v)
    open_list = PriorityMaxQueue()  # store locations to explore, min queue when distance
    probabilities = {}  # store the distances, in this case the probabilities

    open_list.push(starting_node, 1)  # start with the first node, and its probability, would be 0 is distance
    probabilities[starting_node] = 1  # the distance to the first node from itself is 0, and the prob is 1
    while len(open_list) > 0:  # while there is nodes to explore
        closest_node, path_probability = open_list.pop(retrieve_priority=True)

        # for with get_neighbors_and_probabilities(closest_node, edges, succ_prob) is slower
        for neighbor, neighbor_probability in node_conns[closest_node]:
            # check the distances between the neighbor and the origin
            neighbor_probability_from_origin = path_probability * neighbor_probability  # would be sum for distances,
            # but is times for probability

            # if I don't know this path or if this path is better than the one we knew update it on distances table,
            # it would be < for distances, but we are looking for the max
            if neighbor not in probabilities or neighbor_probability_from_origin > probabilities[neighbor]:
                probabilities[neighbor] = neighbor_probability_from_origin  # updating the distance
                open_list.push(neighbor, neighbor_probability_from_origin)  # add neighbor on priority queue
    return probabilities


# def get_neighbors_and_probabilities(source, edges, succ_prob):
#     # could preprocess before
#     neighbors_and_probabilities = []
#     for i, (node_a, node_b) in enumerate(edges):
#         probability = succ_prob[i]
#         if source == node_a:
#             neighbors_and_probabilities.append([node_b, probability])
#         elif source == node_b:
#             neighbors_and_probabilities.append([node_a, probability])
#     return neighbors_and_probabilities

def run(amount_nodes, edges, succ_prob, start, end):
    # Time complexity: O((v+e)*(log(v)+1)), where v is vertices and e is edges
    # Space complexity: O(v)
    # preprocess the connections
    node_conns = [[] for _ in range(amount_nodes)]
    for i, (node_a, node_b) in enumerate(edges):
        prob = succ_prob[i]
        node_conns[node_a].append([node_b, prob])
        node_conns[node_b].append([node_a, prob])
    # solve the problem
    probabilities = dijkstra_max(node_conns, start)
    # get answer
    if end not in probabilities:
        return 0
    return probabilities[end]


def main():
    info()
    test.assertEqual(.25, run(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))
    test.assertEqual(.3, run(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))
    test.assertEqual(0, run(3, [[0, 1]], [0.5], 0, 2))

    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
