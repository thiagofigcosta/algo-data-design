import unittest

import algo_data_design.problems

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Reverse Linked List")
    print("Reverse a linked list :)")
    print("Examples:")
    print('\t[1,2,3,4,5] -> [5,4,3,2,1]')


class Node(object):
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def to_list(self):
        current_node = self
        list_of_values = []
        while current_node is not None:
            list_of_values.append(current_node.val)
            current_node = current_node.next
        return list_of_values

    @staticmethod
    def from_list(array):
        if len(array) == 0:
            return None
        head = Node(array[0])
        current_node = head
        for el in array[1:]:
            node = Node(el)
            current_node.next = node
            current_node = current_node.next
        return head


def run(head):
    # Time complexity: O(n)
    # Space complexity: O(1)
    current_node = head
    previous_node = None
    while current_node is not None:
        next_current_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_current_node
    return previous_node


def main():
    info()
    input_linked_list = Node.from_list([1, 2, 3, 4, 5])
    output_linked_list = run(input_linked_list)
    test.assertEqual([5, 4, 3, 2, 1], output_linked_list.to_list())
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
