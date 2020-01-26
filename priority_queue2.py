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

class Sorted_Priorityqueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        new_element = self._Item(key, value)
        walk = self._data.last()

        while new_element < walk and walk is not None:
            walk = self._data.before(walk)
        if walk is None:
            self._data._add_first(self._Item(key, value))
        else:
            self._data._add_after(new_element, walk)

    def min(self):
        minimum = self._data.first()
        item = minimum.element()
        return (item._key, item._value)

    def remove_min(self):
        minimum_node = self._data.delete(self._data.first())
        return (minimum_node._key, minimum_node._value)











