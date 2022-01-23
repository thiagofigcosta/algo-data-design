import unittest

import algo_data_design.problems
from algo_data_design.utils import input as u_input

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Design HashMap")
    print("Implement a HashMap for integer keys")
    print("Examples:")
    print("\t['HashMap', 'put', 'put', 'get', 'get', 'put', 'get', 'remove', 'get'][[], [1, 1], "
          "[2, 2], [1], [3], [2, 1], [2], [2], [2]] -> [null, null, null, 1, -1, null, 1, null, -1]")


class SimpleHashMap(object):
    # Store a lot of sparse values and data loss when collision

    MAP_SIZE = 100003  # prime number to avoid collision

    # other numbers: 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003

    def __init__(self):
        self.map = [[] for _ in range(SimpleHashMap.MAP_SIZE)]

    def _get_hash(self, key):
        # Time complexity: O(1)
        # Space complexity: O(1)
        return key % SimpleHashMap.MAP_SIZE

    def put(self, key, value):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        if len(self.map[key_hash]) == 0:  # using array instead of plain object to allow storing nulls
            self.map[key_hash].append(value)  # insert
        else:
            self.map[key_hash][0] = value  # update

    def get(self, key):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        if len(self.map[key_hash]) == 0:
            return -1  # key does not exists
        else:
            return self.map[key_hash][0]  # return the value

    def remove(self, key):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        self.map[key_hash].clear()  # or self.map[key_hash] = []


class ListHashMap(object):
    # Store less sparse values and don't have data loss when collision, just performance degradation

    MAP_SIZE = 113  # prime number to avoid collision

    # other numbers: 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003

    def __init__(self):
        self.map = [[] for _ in range(ListHashMap.MAP_SIZE)]

    def _get_hash(self, key):
        # Time complexity: O(1)
        # Space complexity: O(1)
        # This makes every bit on the number have higher impact on final hash, reducing collisions
        # hashing.hash_triple
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key % ListHashMap.MAP_SIZE

    def put(self, key, value):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        if key_index is None:  # using array to insert the values to avoid data loss on collision
            self.map[key_hash].append([key, value])  # insert
        else:
            self.map[key_hash][key_index][1] = value  # update

    def get(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        if key_index is None:
            return -1  # key does not exists
        else:
            return self.map[key_hash][key_index][1]  # return the value (position [1])

    def remove(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        if key_index is not None:
            del self.map[key_hash][key_index]

    def find_index(self, key, key_hash=None):
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        if key_hash is None:
            key_hash = self._get_hash(key)
        for index, (iter_key, _) in enumerate(self.map[key_hash]):
            if iter_key == key:
                return index
        return None


class LinkedHashMap(object):
    # Store few sparse values, the map grows when needed and don't have data loss when collision,
    # just performance degradation that might be solved when rehashing

    LOAD_FACTOR = 0.75  # determines when to increase the hashmap capacity

    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=113):
        self.size = 0
        self.capacity = capacity  # other prime numbers 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003
        self.map = [None for _ in range(self.capacity)]

    def _get_hash(self, key):
        # Time complexity: O(1)
        # Space complexity: O(1)
        # This makes every bit on the number have higher impact on final hash, reducing collisions
        # hashing.hash_multiplication
        key = (key ^ 61) ^ (key >> 16)
        key = key + (key << 3)
        key = key ^ (key >> 4)
        key = key * 0x27d4eb2d
        key = key ^ (key >> 15)
        return key % self.capacity

    def increase_map_and_rehash(self):
        # Time complexity: O(n)
        # Space complexity: O(n)
        # would be great if we had a cheap way to get prime numbers (maybe stored cache)
        new_map = LinkedHashMap(capacity=self.capacity * 2)

        for ll in self.map:  # add all items on the newer and bigger map
            current_node = ll
            while current_node is not None:
                new_map.put(current_node.key, current_node.value)
                current_node = current_node.next

        self.size = new_map.size
        self.capacity = new_map.capacity
        self.map = new_map.map

    def put(self, key, value):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)

        if (self.size + 1) / self.capacity >= LinkedHashMap.LOAD_FACTOR:
            self.increase_map_and_rehash()

        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        if key_node is None:  # using linked list to insert the values to avoid data loss on collision
            new_node = LinkedHashMap.Node(key, value)
            if parent_node is None:  # first item
                self.map[key_hash] = new_node  # insert
            else:
                parent_node.next = new_node  # insert
            self.size += 1
        else:
            key_node.value = value  # update

    def get(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        if key_node is None:
            return -1  # key does not exists
        else:
            return key_node.value  # return the value

    def remove(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        if key_node is not None:
            if parent_node is None:  # first element
                self.map[key_hash] = key_node.next
            else:
                parent_node.next = key_node.next
            self.size -= 1

    def find_pointers(self, key, key_hash=None):
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the map,
        # but very unlikely
        # Space complexity: O(1)
        if key_hash is None:
            key_hash = self._get_hash(key)
        parent = None
        current = self.map[key_hash]
        while current is not None:
            if current.key == key:
                return current, parent
            parent = current
            current = current.next
        return None, parent


def run(hash_map_class):
    obj = hash_map_class()
    obj.put(1, 1)
    obj.put(2, 2)
    test.assertEqual(1, obj.get(1))
    test.assertEqual(-1, obj.get(3))
    obj.put(2, 1)
    test.assertEqual(1, obj.get(2))
    obj.remove(2)
    test.assertEqual(-1, obj.get(2))


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Linked HashMap')
        print('\t2 - List HashMap')
        print('\t3 - Simple HashMap')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=3)
    if solution == 1:
        hash_map_class = LinkedHashMap
    elif solution == 2:
        hash_map_class = ListHashMap
    elif solution == 3:
        hash_map_class = SimpleHashMap
    else:
        raise AttributeError('Unknown solution')
    info()
    run(hash_map_class)
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
