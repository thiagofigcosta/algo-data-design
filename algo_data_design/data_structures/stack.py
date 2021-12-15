class Stack(object):
    # LIFO (Last In, First Out) Data structure
    def __init__(self, size_limit=None):
        self._array = []
        self._limit = size_limit

    def append(self, el):
        if not self.is_full():
            self._array.append(el)
            return True
        return False

    def push(self, el):
        return self.append(el)

    def pop(self):
        el = self._array[-1]
        del self._array[-1]
        return el

    def __copy__(self):
        return self.copy()

    def is_full(self):
        return self._limit is not None and len(self._array) >= self._limit

    def copy(self):
        out = Stack()
        out._array = self._array.copy()
        out._limit = self._limit
        return out

    def __len__(self):
        return len(self._array)
