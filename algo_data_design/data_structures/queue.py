class Queue(object):
    # FIFO (First In, First Out) Data structure
    def __init__(self, first_el=None, size_limit=None):
        self._array = []
        self._limit = size_limit
        if first_el is not None:
            self.append(first_el)

    def append(self, el):
        if not self.is_full():
            self._array.append(el)
            return True
        return False

    def push(self, el):
        return self.append(el)

    def pop(self):
        el = self._array[0]
        del self._array[0]
        return el

    def __copy__(self):
        return self.copy()

    def is_full(self):
        return self._limit is not None and len(self) >= self._limit

    def is_empty(self):
        return len(self) == 0

    def copy(self):
        out = Queue()
        out._array = self._array.copy()
        out._limit = self._limit
        return out

    def __len__(self):
        return len(self._array)
