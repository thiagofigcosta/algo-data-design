import unittest

import algo_data_design.problems
from algo_data_design.utils import input as u_input

test = unittest.TestCase()


def info():
    if algo_data_design.problems.NO_INFO:
        return
    print("Merge k Sorted Lists")
    print("Given a list of sorted linked lists merge them all in a sorted linked list.")
    print("Examples:")
    print('\t[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]')
    print('\t[] -> []')
    print('\t[[]] -> []')


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


def find_middle_node(node):
    tortoise = node  # the tortoise starts on the start point
    hare = node.next  # the hare always starts first
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next  # tortoise move one step at the time
        hare = hare.next.next  # hare jumps two steps at the time
    return tortoise


def append_to_linked_list_and_retrieve_last_node(last_node_of_linked_list, node_to_append):
    if last_node_of_linked_list is None:
        return node_to_append
    else:
        last_node_of_linked_list.next = node_to_append
        return last_node_of_linked_list.next


def merge(ll1, ll2):
    merged_list = None
    merged_list_last_node = None
    cur_node_1 = ll1
    cur_node_2 = ll2
    # merging sorted arrays
    while cur_node_1 is not None and cur_node_2 is not None:
        if cur_node_1.val < cur_node_2.val:  # appending the smaller element to the final list
            merged_list_last_node = append_to_linked_list_and_retrieve_last_node(merged_list_last_node, cur_node_1)
            cur_node_1 = cur_node_1.next
        else:
            merged_list_last_node = append_to_linked_list_and_retrieve_last_node(merged_list_last_node, cur_node_2)
            cur_node_2 = cur_node_2.next
        if merged_list is None:  # store the head of linked list
            merged_list = merged_list_last_node
    # moving the remainders, appending the left elements
    while cur_node_1 is not None:
        merged_list_last_node = append_to_linked_list_and_retrieve_last_node(merged_list_last_node, cur_node_1)
        cur_node_1 = cur_node_1.next
        if merged_list is None:  # store the head of linked list
            merged_list = merged_list_last_node
    while cur_node_2 is not None:
        merged_list_last_node = append_to_linked_list_and_retrieve_last_node(merged_list_last_node, cur_node_2)
        cur_node_2 = cur_node_2.next
        if merged_list is None:  # store the head of linked list
            merged_list = merged_list_last_node
    return merged_list


def merge_sort(linked_list):
    # must split a linked_list only if its size is bigger than one
    if linked_list is None or linked_list.next is None:
        # if the linked list size is zero or one
        return linked_list
    # split in half
    middle_node = find_middle_node(linked_list)
    second_linked_list = middle_node.next
    middle_node.next = None
    # divide and conquer
    linked_list = merge_sort(linked_list)  # continue dividing the linked list
    second_linked_list = merge_sort(second_linked_list)  # continue dividing the linked list
    merged_list = merge(linked_list, second_linked_list)
    return merged_list


def run_appending_one_by_one(linked_lists):
    # Time complexity: O(k*t), where k is the amount of lists and t is the total size of all inner linked lists
    # Space complexity: O(t)
    merged_list_current = None
    merged_list_head = None
    while len(linked_lists) > 0:  # while True, but only if there are elements on the list
        min_value = None
        min_index = None
        done = True
        for l, linked_list in enumerate(linked_lists):  # get the smallest element
            if linked_list is not None:
                done = False # if there is a single list that wasn't fully iterated we continue
                if min_value is None or linked_list.val < min_value:
                    min_value = linked_list.val
                    min_index = l
        if min_index is not None: # insert the smallest on final linked list
            if merged_list_current is None:
                merged_list_current = Node(min_value)
                merged_list_head = merged_list_current
            else:
                merged_list_current.next = Node(min_value)
                merged_list_current = merged_list_current.next
            linked_lists[min_index] = linked_lists[min_index].next

        if done:
            return merged_list_head


def run_merging_linked_lists(linked_lists):
    # Time complexity: O(t), where t is the total size of all inner linked lists
    # Space complexity: O(1)
    if len(linked_lists) == 0:
        return None
    merged_linked_list = linked_lists[0]
    for linked_list in linked_lists[1:]:
        # since the linked lists are already sorted I don't need to divide them, just the merge function is enough
        merged_linked_list = merge(merged_linked_list, linked_list)  # merge lists one by one
    return merged_linked_list


def run_merging_linked_lists_two_by_two(linked_lists):  # accepted
    # Time complexity: O(t), where t is the total size of all inner linked lists
    # Space complexity: O(log(k))
    if len(linked_lists) == 0:  # base case, if len is zero return None
        return None
    if len(linked_lists) == 1:  # base case, if the len is none, return the only linked list
        return linked_lists[0]
    if len(linked_lists) == 2:  # base case, if there are two linked lists return them merged
        return merge(linked_lists[0], linked_lists[1])
    new_linked_lists = []  # to store merged lists
    for i in range(0, len(linked_lists), 2):  # iterate two by two
        two_lists = linked_lists[i:i + 2]
        if len(two_lists) == 2:
            new_linked_lists.append(merge(two_lists[0], two_lists[1]))  # combine the lists and store the result
        else:
            new_linked_lists.append(two_lists[0])  # if odd number, store the remaining list
    return run_merging_linked_lists_two_by_two(new_linked_lists)  # recursive call with partial results


def run_sorting_list(linked_lists):  # accepted
    # Time complexity: O(t+t*log(t)), where t is the total size of all inner linked lists
    # Space complexity: O(t)
    to_sort = []
    for node in linked_lists:
        while node is not None:
            to_sort.append(node.val)  # add all elements to an array
            node = node.next
    to_sort.sort()  # sort the array
    if len(to_sort) == 0:
        return None
    # reconstruct the linked list (we could be reusing the already instantiated nodes)
    head = Node(to_sort[0])
    current_node = head
    for el in to_sort[1:]:
        node = Node(el)
        current_node.next = node
        current_node = current_node.next
    return head


def run_merge_sort(linked_lists):  # accepted
    # Time complexity: O(t+t*log(t)), where t is the total size of all inner linked lists
    # Space complexity: O(1)
    merged_list = None
    cur_merged_list = None
    for node in linked_lists:  # append the linked lists together
        while node is not None:
            if merged_list is None:
                cur_merged_list = node
                merged_list = cur_merged_list
            else:
                cur_merged_list.next = node
                cur_merged_list = cur_merged_list.next
            node = node.next
    return merge_sort(merged_list)  # run merge sort


def main():
    if algo_data_design.problems.NO_PROMPT:
        solution = 1
    else:
        print('Choose a solution to run:')
        print('\t1 - Merging linked lists two by two - Accepted')
        print('\t2 - Merge sort on combined list - Accepted')
        print('\t3 - Sorting array and reconstructing linked list - Accepted - why?')
        print('\t4 - Merging linked lists - Rejected - why?')
        print('\t5 - Insertion sort - Rejected')
        solution = u_input.input_number(greater_or_eq=1, lower_or_eq=5)
    if solution == 1:
        run = run_merging_linked_lists_two_by_two
    elif solution == 2:
        run = run_merge_sort
    elif solution == 3:
        run = run_sorting_list
    elif solution == 4:
        run = run_merging_linked_lists
    elif solution == 5:
        run = run_appending_one_by_one
    else:
        raise AttributeError('Unknown solution')
    info()
    linked_lists_1 = [Node.from_list([1, 4, 5]), Node.from_list([1, 3, 4]), Node.from_list([2, 6])]
    test.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], run(linked_lists_1).to_list())
    linked_lists_2 = [None, Node.from_list([1])]
    test.assertEqual([1], run(linked_lists_2).to_list())
    test.assertEqual(None, run([]))
    test.assertEqual(None, run([None]))
    if not algo_data_design.problems.NO_INFO:
        print('All tests passed')


if __name__ == "__main__":
    main()
