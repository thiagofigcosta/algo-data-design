import unittest

from data_structures import LinkedList, LinkedListNode


class LinkedListTest(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.linked_list_1 = LinkedList()
        self.linked_list_1_values = []
        for i in range(10):
            self.linked_list_1.add(LinkedListNode(i))
            self.linked_list_1_values.append(i)

    def test_iterator_and_add(self, *args, **kwargs):
        for i, node in enumerate(self.linked_list_1):
            self.assertEqual(self.linked_list_1_values[i], node.data)

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

    def test_reverse(self, *args, **kwargs):
        reversed_linked_list = self.linked_list_1.copy()
        reversed_values = self.linked_list_1_values.copy()
        reversed_linked_list.reverse()
        reversed_values.reverse()
        for i, node in enumerate(reversed_linked_list):
            self.assertEqual(reversed_values[i], node.data)


if __name__ == '__main__':
    unittest.main()
