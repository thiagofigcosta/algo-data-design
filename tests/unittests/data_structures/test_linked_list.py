import unittest

import algo_data_design.utils.list as u_list
from algo_data_design.data_structures import LinkedList, LinkedListNode


class LinkedListTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.linked_list_1 = LinkedList()
        self.linked_list_1_values = []
        for i in range(10):
            self.linked_list_1.add(LinkedListNode(i))
            self.linked_list_1_values.append(i)

    def test_iterator_and_add_and_get(self, *args, **kwargs):
        for i, node in enumerate(self.linked_list_1):
            self.assertEqual(self.linked_list_1_values[i], node.data)
        linked_list = self.linked_list_1.copy()
        linked_list_values = self.linked_list_1_values.copy()
        linked_list_values.insert(3, 8888)
        linked_list.add_at(3, LinkedListNode(8888))
        for i, node in enumerate(linked_list):
            self.assertEqual(linked_list_values[i], node.data)
        for i in range(len(linked_list_values)):
            self.assertEqual(linked_list_values[i], linked_list.get_at(i))

    def test_copy(self, *args, **kwargs):
        linked_list = self.linked_list_1.copy()
        linked_list_to_change = self.linked_list_1.copy()
        self.assertEqual(linked_list, linked_list_to_change)
        reference_to_linked_list_to_change = linked_list_to_change
        self.assertEqual(linked_list.head, linked_list_to_change.head)
        linked_list_to_change.head.data = 50
        self.assertEqual(50, linked_list_to_change.head.data)
        self.assertEqual(50, reference_to_linked_list_to_change.head.data)
        linked_list_to_change.head.data = 50
        self.assertNotEqual(50, linked_list.head.data)

    def test_len(self, *args, **kwargs):
        self.assertEqual(len(self.linked_list_1_values), len(self.linked_list_1))
        self.assertEqual(0, len(LinkedList()))
        self.assertEqual(1, len(LinkedList(LinkedListNode(10))))

    def test_pop(self, *args, **kwargs):
        linked_list = self.linked_list_1.copy()
        self.assertEqual(self.linked_list_1_values[0], linked_list.pop_first())
        self.assertEqual(len(self.linked_list_1_values) - 1, len(linked_list))
        self.assertEqual(self.linked_list_1_values[-1], linked_list.pop_last())
        self.assertEqual(len(self.linked_list_1_values) - 2, len(linked_list))
        self.assertEqual(3, linked_list.pop_at(2))
        self.assertEqual(4, linked_list.pop_at(2))
        self.assertEqual(len(self.linked_list_1_values) - 4, len(linked_list))
        self.assertEqual(8, linked_list.pop_at(5))
        self.assertRaises(Exception, linked_list.pop_at, 5)

    def test_reverse(self, *args, **kwargs):
        reversed_linked_list = self.linked_list_1.copy()
        reversed_values = self.linked_list_1_values.copy()
        reversed_linked_list.reverse()
        reversed_values.reverse()
        for i, node in enumerate(reversed_linked_list):
            self.assertEqual(reversed_values[i], node.data)

    def test_circle(self, *args, **kwargs):
        linked_list = self.linked_list_1.copy()
        self.assertFalse(linked_list.has_circle())
        last_node = linked_list.get_at(len(linked_list) - 1, get_node=True)
        last_node.next = linked_list.get_at(4, get_node=True)
        self.assertTrue(linked_list.has_circle())

    def test_sort(self, *args, **kwargs):
        linked_list_values = u_list.random_int_list(300)
        linked_list = LinkedList()
        for el in linked_list_values:
            linked_list.add(LinkedListNode(el))
        linked_list_values.sort()
        linked_list.sort()
        for i, node in enumerate(linked_list):
            self.assertEqual(linked_list_values[i], node.data)


if __name__ == '__main__':
    unittest.main()
