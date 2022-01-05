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

    def deepcopy(self, nested_deep_copy=False):
        for copy_func in ('__deepcopy__', 'deepcopy', '__copy__', 'copy'):
            copy_func_func = getattr(self.data, copy_func, None)
            if callable(copy_func_func):
                return Node(copy_func_func(self.data), self.next.deepcopy() if nested_deep_copy else self.next)
        return self.copy()

    def copy(self):
        return Node(self.data, self.next)


class LinkedList(object):

    def __init__(self, head_node=None):
        self.head = head_node

    def sort(self):
        from algo_data_design.algorithms.sorting import merge_sort_linked_list
        merge_sort_linked_list(self)

    def _hare_and_tortoise(self, detect_circle=True):
        if self.is_empty():
            if detect_circle:
                return False
            else:
                return None
        if self.is_one_sized():
            if detect_circle:
                return False
            else:
                return self.head
        tortoise = self.head  # the tortoise starts on the start point
        hare = self.head.next  # the hare always starts first
        while hare is not None and hare.next is not None:
            if detect_circle and hare is tortoise:
                return True
            tortoise = tortoise.next  # tortoise move one step at the time
            hare = hare.next.next  # hare jumps two steps at the time
        if detect_circle:
            return False
        else:
            return tortoise

    def has_circle(self):
        return self._hare_and_tortoise(True)

    def get_middle_node(self):
        return self._hare_and_tortoise(False)

    def is_empty(self):
        return self.head is None

    def is_one_sized(self):
        return self.head.next is None

    def add_at(self, at, node):
        if self.is_empty():
            if at != 0:
                raise KeyError(f'Invalid position `{at}`')
            self.head = node
            return
        previous = None
        current = self.head
        j = 0
        while j < at and current.next is not None:
            previous = current
            current = current.next
            j += 1
        if at != j:
            raise KeyError(f'Invalid position `{at}`')
        previous.next = node
        node.next = current

    def add(self, node):
        if self.is_empty():
            self.head = node
            return
        if self.is_one_sized():
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

    def _get_or_pop_at(self, i, pop=False, get_node=False):
        if self.is_empty():
            raise KeyError(f'Invalid position `{i}`')
        if i == 0:
            if pop:
                return self.pop_first(get_node=get_node)
            else:
                return self.head.data
        previous = None
        current = self.head
        j = 0
        while j < i and current.next is not None:
            previous = current
            current = current.next
            j += 1
        if i != j:
            raise KeyError(f'Invalid position `{i}`')
        if pop:
            previous.next = current.next
        if get_node:
            return current
        else:
            return current.data

    def pop_at(self, i, get_node=False):
        return self._get_or_pop_at(i, True, get_node=get_node)

    def get_at(self, i, get_node=False):
        return self._get_or_pop_at(i, False, get_node=get_node)

    def __getitem__(self, item):
        return self.get_at(item, get_node=True)

    def pop_first(self, get_node=False):
        if self.is_empty():
            raise KeyError('There is nothing to pop')
        value = self.head.data
        self.head = self.head.next
        if get_node:
            return self.head
        else:
            return value

    def _get_or_pop_last(self, pop=False, get_node=False):
        if self.is_empty():
            raise KeyError('There is nothing to pop')
        if self.is_one_sized():
            if pop:
                return self.pop_first(get_node=get_node)
            else:
                return self.get_at(0, get_node=get_node)
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        if pop:
            previous_node.next = None
        if get_node:
            return current_node
        else:
            return current_node.data

    def get_last(self, get_node=False):
        return self._get_or_pop_last(False, get_node=get_node)

    def pop_last(self, get_node=False):
        return self._get_or_pop_last(True, get_node=get_node)

    def __len__(self):
        if self.is_empty():
            return 0
        if self.is_one_sized():
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
        if self.is_empty() or self.is_one_sized():
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
        if self.is_empty():
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

    def __str__(self):
        string = ''
        size = len(self)
        for i, node in enumerate(self):
            string += str(node)
            if i + 1 < size:
                string += ' -> '
        return string


class LinkedListIterator:
    def __init__(self, linked_list):
        self._current = linked_list.head

    def __next__(self):
        if self._current is not None:
            result = self._current
            self._current = self._current.next
            return result
        raise StopIteration
