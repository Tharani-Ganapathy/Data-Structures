class _DoublyLinkedBase:
    class _Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, e, previous, next_node):
        # next_node = previous._next
        newest = self._Node(e, previous, next_node)
        previous._next = newest
        next_node._prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        previous = node._prev
        next_node = node._next
        previous._next = next_node
        next_node._prev = previous
        self._size -= 1
        result = node._element
        node._next = node._prev = node._element = None
        return result


dll = _DoublyLinkedBase()
p = dll._Node(None, None, None)
s = dll._Node(None, None, None)
# answer = dll._Node(None, None, None)
answer = dll.insert_between(2, p, s)
print(answer._element)












