class PriorityQueue(object):
    # FIFO (First In, First Out) for equal priorities Data structure
    # 0 - Standard priority
    # inf - Lowest priority
    # -inf - Highest priority
    DATA_INDEX = 0
    PRIORITY_INDEX = 1

    def __init__(self, size_limit=None):
        self._array = []
        self._limit = size_limit

    def append(self, el, priority=0):
        if not self.is_full():
            insert_at = 0
            for i in range(len(self._array) - 1, -1, -1):
                iter_priority = self._array[i][PriorityQueue.PRIORITY_INDEX]
                if iter_priority <= priority:
                    insert_at = i + 1
                    break
            self._array.insert(insert_at, (el, priority))
            return True
        return False

    def push(self, el, priority=0):
        return self.append(el, priority=priority)

    def pop(self, retrieve_priority=False):
        el = self._array[0]
        del self._array[0]
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
        return out

    def __len__(self):
        return len(self._array)

    def __eq__(self, other):
        if not isinstance(other, PriorityQueue):
            return False
        return self._array == other._array and self._limit == other._limit
