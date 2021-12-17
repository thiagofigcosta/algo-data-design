class Deque(object):
    # Data struct that allows to insert/pop on front and back
    def __init__(self, size_limit=None):
        self._array = []
        self._limit = size_limit

    def _push(self, el, back=False):
        if not self.is_full():
            if back:
                self._array.append(el)
            else:
                self._array.insert(0, el)
            return True
        return False

    def push_back(self, el):
        return self._push(el, back=True)

    def push_front(self, el):
        return self._push(el, back=False)

    def _pop(self, back=False):
        if back:
            pos = -1
        else:
            pos = 0
        el = self._array[pos]
        del self._array[pos]
        return el

    def pop_back(self):
        return self._pop(back=True)

    def pop_front(self):
        return self._pop(back=False)

    def __copy__(self):
        return self.copy()

    def is_full(self):
        return self._limit is not None and len(self) >= self._limit

    def is_empty(self):
        return len(self) == 0

    def copy(self):
        out = Deque()
        out._array = self._array.copy()
        out._limit = self._limit
        return out

    def __len__(self):
        return len(self._array)
