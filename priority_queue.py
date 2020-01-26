from doublylinkedlist_positionallist import PositionalList

class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0

class Unsorted_Priorityqueue(PriorityQueueBase):

    def _find_min(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        small = self._data.first()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data._add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        minimum = p.element()
        return (minimum._key, minimum._value)

    def remove_min(self):
        p = self._find_min()
        minimum_node = self._data.delete(p)
        return (minimum_node._key, minimum_node._value)











