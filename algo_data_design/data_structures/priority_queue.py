import heapq
from enum import Enum, auto as enum_auto


class PriorityQueueMethod(Enum):
    LIST = enum_auto() # Push = O(n) | Pop (1)
    SORT = enum_auto() # Push = O(1) | Pop (n*log(n)) | Pop without new elements O(1)
    HEAP = enum_auto() # Push = O(log(n)) | Pop (log(n))
    # the order of equal priorities is not guaranteed in heapq

    @staticmethod
    def get_all_methods():
        return list(map(lambda c: c, PriorityQueueMethod))

    def __str__(self):
        return self.name

    def __eq__(self, other):
        # https://bugs.python.org/issue30545
        if not isinstance(other, Enum):
            return False
        self_dict = self.__dict__
        other_dict = other.__dict__
        return self_dict['_value_'] == other_dict['_value_'] and str(self_dict['__objclass__']) == str(
            other_dict['__objclass__'])

class PriorityQueueNode(object):
    # created to avoid using tuples on heapq since a given value of custom class might not implement the __lt__ function

    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority

    def get_pair(self):
        return self.value, self.priority


class PriorityQueue(object):
    # FIFO (First In, First Out) for equal priorities Data structure
    # 0 - Standard priority
    # if min queue:
    #   inf - Lowest priority
    #   -inf - Highest priority
    # if max queue:
    #   -inf - Lowest priority
    #   inf - Highest priority
    def __init__(self, size_limit=None, max_queue=False, method=PriorityQueueMethod.HEAP):
        self._array = []
        self._limit = size_limit
        self._min = not max_queue
        self._method = method
        self._sorted = False

    def append(self, el, priority=0):
        if not self.is_full():
            if self._method == PriorityQueueMethod.LIST:
                insert_at = 0
                for i in range(len(self._array) - 1, -1, -1):
                    iter_priority = self._array[i].priority
                    # insert in order to make popping easier
                    # check the type first and then run the real comparison
                    if (self._min and iter_priority <= priority) or (not self._min and iter_priority >= priority):
                        insert_at = i + 1
                        break
                self._array.insert(insert_at, PriorityQueueNode(priority, el))
            elif self._method == PriorityQueueMethod.SORT:
                self._array.append(PriorityQueueNode(priority, el))
                self._sorted = False
            elif self._method == PriorityQueueMethod.HEAP:
                if self._min:
                    item = PriorityQueueNode(priority, el)
                else:
                    item = PriorityQueueNode(-priority, el)
                heapq.heappush(self._array, item)
            else:
                raise AttributeError(f'Unknown pivot method {self._method}')
            return True
        return False

    def push(self, el, priority=0):
        return self.append(el, priority=priority)

    def pop(self, retrieve_priority=False):
        return self.pop_at(0, retrieve_priority=retrieve_priority)

    def pop_at(self, i, retrieve_priority=False):
        if self._method == PriorityQueueMethod.LIST:
            el = self._array[i]
            del self._array[i]
        elif self._method == PriorityQueueMethod.SORT:
            if not self._sorted:
                self.sort()
            el = self._array[i]
            del self._array[i]
        elif self._method == PriorityQueueMethod.HEAP:
            el = heapq.heappop(self._array)
            if not self._min:
                el.priority *= -1
        else:
            raise AttributeError(f'Unknown pivot method {self._method}')
        if retrieve_priority:
            return el.get_pair()
        else:
            return el.value

    def __copy__(self):
        return self.copy()

    def is_full(self):
        return self._limit is not None and len(self) >= self._limit

    def is_empty(self):
        return len(self) == 0

    def copy(self):
        out = PriorityQueue()
        out._array = self._array.copy()
        out._limit = self._limit
        out._min = self._min
        out._method = self._method
        out._sorted = self._sorted
        return out

    def __len__(self):
        return len(self._array)

    def __eq__(self, other):
        if not isinstance(other, PriorityQueue):
            return False
        # don't need to check neither sorted nor method
        return self._array == other._array and self._limit == other._limit and self._min == other._min

    def sort(self):
        self._array.sort(reverse=not self._min)
        self._sorted = True
