class PriorityQueue(object):
    # FIFO (First In, First Out) for equal priorities Data structure
    # 0 - Standard priority
    # if min queue:
    #   inf - Lowest priority
    #   -inf - Highest priority
    # if max queue:
    #   -inf - Lowest priority
    #   inf - Highest priority
    DATA_INDEX = 0
    PRIORITY_INDEX = 1

    def __init__(self, size_limit=None, max_queue=False):
        self._array = []
        self._limit = size_limit
        self._min = not max_queue

    def append(self, el, priority=0):
        if not self.is_full():
            insert_at = 0
            for i in range(len(self._array) - 1, -1, -1):
                iter_priority = self._array[i][PriorityQueue.PRIORITY_INDEX]
                # insert in order to make popping easier
                # check the type first and then run the real comparison
                if (self._min and iter_priority <= priority) or (not self._min and iter_priority >= priority):
                    insert_at = i + 1
                    break
            self._array.insert(insert_at, (el, priority))
            return True
        return False

    def push(self, el, priority=0):
        return self.append(el, priority=priority)

    def pop(self, retrieve_priority=False):
        return self.pop_at(0, retrieve_priority=retrieve_priority)

    def pop_at(self, i, retrieve_priority=False):
        el = self._array[i]
        del self._array[i]
        if retrieve_priority:
            return el
        else:
            return el[PriorityQueue.DATA_INDEX]

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
        return out

    def __len__(self):
        return len(self._array)

    def __eq__(self, other):
        if not isinstance(other, PriorityQueue):
            return False
        return self._array == other._array and self._limit == other._limit and self._min == other._min
