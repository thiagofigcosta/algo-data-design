from algo_data_design.data_structures import LinkedList


def sort(array):
    """
    Good for external sorting (huge arrays that does not fit in memory)
    Time complexity:
        Average/Best/Worst: O(n*log(n))
    Space complexity: O(n)
    Stable, two equal keys are guaranteed to be in the same order as the input on the output
    """
    _sort_recursive(array)


def sort_linked_list(ll):
    """
    Good for external sorting (huge arrays that does not fit in memory)
    Time complexity:
        Average/Best/Worst: O(n*log(n))
    Space complexity: O(1)
    Stable, two equal keys are guaranteed to be in the same order as the input on the output
    """
    if ll.is_empty() or ll.is_one_sized():
        return
    mid = ll.get_middle_node()
    # divide an conquer
    mid_next = mid.next
    mid.next = None
    ll1 = LinkedList(ll.head)
    ll2 = LinkedList(mid_next)
    sort_linked_list(ll1)
    sort_linked_list(ll2)
    # merge
    ll.head = _merge_linked_list(ll1, ll2).head


def _sort_recursive(array):
    if len(array) > 1:
        mid = len(array) // 2
        # divide an conquer
        left_partition = array[:mid]
        right_partition = array[mid:]
        _sort_recursive(left_partition)
        _sort_recursive(right_partition)
        # merge
        _merge(array, left_partition, right_partition)


def _merge(array, left_partition, right_partition):
    left_itr = 0
    right_itr = 0
    dst_itr = 0
    # merging sorted arrays
    while left_itr < len(left_partition) and right_itr < len(right_partition):
        if left_partition[left_itr] < right_partition[right_itr]:
            array[dst_itr] = left_partition[left_itr]
            left_itr += 1
        else:
            array[dst_itr] = right_partition[right_itr]
            right_itr += 1
        dst_itr += 1
    # moving the remainders
    for i in range(left_itr, len(left_partition), 1):
        array[dst_itr] = left_partition[i]
        dst_itr += 1
    for i in range(right_itr, len(right_partition), 1):
        array[dst_itr] = right_partition[i]
        dst_itr += 1


def _add_to_ll_and_retrieve_last(ll, last_ll_node, node_to_add):
    if last_ll_node is None:
        ll.add(node_to_add)
        return node_to_add
    else:
        last_ll_node.next = node_to_add
        return node_to_add


def _merge_linked_list(ll1, ll2):
    ll = LinkedList()
    ll_last = None
    cur_1 = ll1.head
    cur_2 = ll2.head
    # merging sorted arrays
    while cur_1 is not None and cur_2 is not None:
        if cur_1 < cur_2:
            ll_last = _add_to_ll_and_retrieve_last(ll, ll_last, cur_1)
            cur_1 = cur_1.next
        else:
            ll_last = _add_to_ll_and_retrieve_last(ll, ll_last, cur_2)
            cur_2 = cur_2.next
    # moving the remainders
    while cur_1 is not None:
        ll_last = _add_to_ll_and_retrieve_last(ll, ll_last, cur_1)
        cur_1 = cur_1.next
    while cur_2 is not None:
        ll_last = _add_to_ll_and_retrieve_last(ll, ll_last, cur_2)
        cur_2 = cur_2.next
    return ll
