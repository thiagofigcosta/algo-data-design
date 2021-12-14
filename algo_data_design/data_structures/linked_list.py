class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        return self.data == other.data

    def __lt__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        return self.data < other.data

    def __gt__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        return self.data > other.data

    def __copy__(self):
        return self.copy()

    def deepcopy(self):
        for copy_func in ('__deepcopy__', 'deepcopy', '__copy__', 'copy'):
            copy_func_func = getattr(self.data, copy_func, None)
            if callable(copy_func_func):
                return Node(copy_func_func(self.data), self.next)
        return self.copy()

    def copy(self):
        return Node(self.data, self.next)


class LinkedList(object):

    def __init__(self, head_node=None):
        self.head = head_node

    def __add__(self, node):
        self.add(node)

    def add(self, node):
        if self.head is None:
            self.head = node
            return
        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def pop_first(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def pop_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.pop_first()
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

    def __len__(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        count = 1
        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return count + 1

    def __reversed__(self):
        new_list = self.copy()
        new_list.reverse()
        return new_list

    def reverse(self):
        # a -> b -> c -> d -> e -> None
        # e -> d -> c -> b -> a -> None
        if self.head is None or self.head.next is None:
            return
        current_node = self.head
        next_node = current_node.next
        current_node.next = None
        previous_node = current_node
        while True:
            current_node = next_node
            next_node = next_node.next
            current_node.next = previous_node
            previous_node = current_node
            if next_node is None:
                self.head = current_node
                break

    def __iter__(self):
        return LinkedListIterator(self)

    def __copy__(self):
        return self.copy()

    def _ll_copy(self, deep=False):
        out = LinkedList()
        if self.head is None:
            return out
        for node in self:
            if deep:
                new_node = node.deepcopy()
            else:
                new_node = node.copy()
            new_node.next = None
            out.add(new_node)
        return out

    def deepcopy(self):
        return self._ll_copy(deep=True)

    def copy(self):
        return self._ll_copy(deep=False)

    def __eq__(self, other):
        if other is None or not isinstance(other, LinkedList):
            return False
        current_self = self.head
        current_other = other.head
        while True:
            if current_self != current_other:
                return False
            if current_self.next is None and current_other.next is None:
                return True
            if current_self.next is None or current_other.next is None:
                return False
            current_self = current_self.next
            current_other = current_other.next


class LinkedListIterator:
    def __init__(self, linked_list):
        self._current = linked_list.head

    def __next__(self):
        if self._current is not None:
            result = self._current
            self._current = self._current.next
            return result
        raise StopIteration
