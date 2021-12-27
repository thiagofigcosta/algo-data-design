class RingBuffer(object):
    # Infinite buffer data structure (delete old elements when the limit is reached)
    def __init__(self, size):
        self._array = [None] * size
        self._size = size
        self._write_pointer = 0
        self._read_pointer = 0
        self._cur_size = 0

    def _circular_sum(self, base, to_add=1):
        return (base + to_add) % self._size

    def append(self, el, override=True):
        if override or len(self) < self._size:
            self._array[self._write_pointer] = el
            self._write_pointer = self._circular_sum(self._write_pointer)
            self._cur_size = min(self._cur_size + 1, self._size)
            return True
        return False

    def push(self, el, override=False):
        return self.append(el, override=override)

    def pop(self):
        if len(self) > 0:
            el = self.get()
            self._read_pointer = self._circular_sum(self._read_pointer)
            self._cur_size = max(self._cur_size - 1, 0)
            return el
        raise Exception('Empty buffer')

    def get(self, i=0):
        if self._read_pointer != -1 and len(self) > 0 and i < len(self):
            i = self._circular_sum(self._read_pointer, i)
            return self._array[i]
        raise Exception(f'Invalid position `{i}`')

    def __getitem__(self, item):
        return self.get(item)

    def __copy__(self):
        return self.copy()

    def copy(self):
        out = RingBuffer(self._size)
        out._array = self._array.copy()
        out._write_pointer = self._write_pointer
        out._read_pointer = self._read_pointer
        out._cur_size = self._cur_size
        return out

    def __len__(self):
        return self._cur_size

    def __eq__(self, other):
        if not isinstance(other, RingBuffer):
            return False
        equal = self._size == other._size and self._cur_size == other._cur_size
        if not equal:
            return False
        for i in range(self._cur_size):
            if self.get(i) != other.get(i):
                return False
        return True
