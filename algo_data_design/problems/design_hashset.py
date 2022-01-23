import unittest

import algo_data_design.problems
from algo_data_design.utils import input as u_input

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Design HashSet")
    print("Implement a HasSet for integer keys")
    print("Examples:")
    print("\t['MyHashSet', 'add', 'add', 'contains', 'contains', 'add', 'contains', 'remove', 'contains'] [[], [1], "
          "[2], [1], [3], [2], [2], [2], [2]] -> [null, null, null, true, false, null, true, null, false]")


class SimpleHashSet(object):
    # Store a lot of sparse values and data loss when collision

    SET_SIZE = 100003  # prime number to avoid collision

    # other numbers: 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003

    def __init__(self):
        self.set = [False for _ in range(SimpleHashSet.SET_SIZE)]

    def _get_hash(self, key):
        # Time complexity: O(1)
        # Space complexity: O(1)
        return key % SimpleHashSet.SET_SIZE

    def add(self, key):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        self.set[key_hash] = True  # insert

    def contains(self, key):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        return self.set[key_hash]

    def remove(self, key):  # int key
        # Time complexity: O(1)
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        self.set[key_hash] = False


class ListHashSet(object):
    # Store less sparse values and don't have data loss when collision, just performance degradation

    SET_SIZE = 113  # prime number to avoid collision

    # other numbers: 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003

    def __init__(self):
        self.set = [[] for _ in range(ListHashSet.SET_SIZE)]

    def _get_hash(self, key):
        # Time complexity: O(1)
        # Space complexity: O(1)
        # This makes every bit on the number have higher impact on final hash, reducing collisions
        # hashing.hash_triple
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key % ListHashSet.SET_SIZE

    def add(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        if key_index is None:  # using array to insert the values to avoid data loss on collision
            self.set[key_hash].append(key)  # insert

    def contains(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        return key_index is not None

    def remove(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_index = self.find_index(key, key_hash)
        if key_index is not None:
            del self.set[key_hash][key_index]

    def find_index(self, key, key_hash=None):
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        if key_hash is None:
            key_hash = self._get_hash(key)
        for index, iter_key in enumerate(self.set[key_hash]):
            if iter_key == key:
                return index
        return None


class LinkedHashSet(object):
    # Store few sparse values, the set grows when needed and don't have data loss when collision,
    # just performance degradation that might be solved when rehashing

    LOAD_FACTOR = 0.75  # determines when to increase the hashset capacity

    class Node(object):
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self, capacity=113):
        self.size = 0
        self.capacity = capacity  # other prime numbers 113, 503, 1013, 1553, 2003, 3023, 5003, 6661, 7013, 9013, 100003
        self.set = [None for _ in range(self.capacity)]

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

    def increase_set_and_rehash(self):
        # Time complexity: O(n)
        # Space complexity: O(n)
        # would be great if we had a cheap way to get prime numbers (maybe stored cache)
        new_set = LinkedHashSet(capacity=self.capacity * 2)

        for ll in self.set:  # add all items on the newer and bigger set
            current_node = ll
            while current_node is not None:
                new_set.add(current_node.key)
                current_node = current_node.next

        self.size = new_set.size
        self.capacity = new_set.capacity
        self.set = new_set.set

    def add(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)

        if (self.size + 1) / self.capacity >= LinkedHashSet.LOAD_FACTOR:
            self.increase_set_and_rehash()

        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        if key_node is None:  # using linked list to insert the values to avoid data loss on collision
            new_node = LinkedHashSet.Node(key)
            if parent_node is None:  # first item
                self.set[key_hash] = new_node  # insert
            else:
                parent_node.next = new_node  # insert
            self.size += 1

    def contains(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        return key_node is not None

    def remove(self, key):  # int key
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        key_hash = self._get_hash(key)
        key_node, parent_node = self.find_pointers(key, key_hash)
        if key_node is not None:
            if parent_node is None:  # first element
                self.set[key_hash] = key_node.next
            else:
                parent_node.next = key_node.next
            self.size -= 1

    def find_pointers(self, key, key_hash=None):
        # Time complexity: O(n), where n is the amount of elements on the list, worst case is every element of the set,
        # but very unlikely
        # Space complexity: O(1)
        if key_hash is None:
            key_hash = self._get_hash(key)
        parent = None
        current = self.set[key_hash]
        while current is not None:
            if current.key == key:
                return current, parent
            parent = current
            current = current.next
        return None, parent


def run(hash_set_class):
    obj = hash_set_class()
    obj.add(1)
    obj.add(2)
    test.assertTrue(obj.contains(1))
    test.assertFalse(obj.contains(3))
    obj.add(2)
    test.assertTrue(obj.contains(2))
    obj.remove(2)
    test.assertFalse(obj.contains(2))


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Linked HashSet')
        print('\t2 - List HashSet')
        print('\t3 - Simple HashSet')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=3)
    if solution == 1:
        hash_set_class = LinkedHashSet
    elif solution == 2:
        hash_set_class = ListHashSet
    elif solution == 3:
        hash_set_class = SimpleHashSet
    else:
        raise AttributeError('Unknown solution')
    info()
    run(hash_set_class)
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
