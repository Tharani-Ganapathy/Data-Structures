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

    def _insert_between(self, e, previous, next_node):
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

class PositionalList(_DoublyLinkedBase):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):

        if not isinstance(p, self.Position):
            raise TypeError("p must be of position type")

        if p._container is not self:
            raise ValueError("p does not belong to this container")

        if p._node._next is None:
            raise ValueError("p is no longer valid")

        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        position_node = self._validate(p)
        return self._make_position(position_node._prev)

    def after(self, p):
        position_node = self._validate(p)
        return self._make_position(position_node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = cursor.after()


    def _insert_between(self,e, previous, next_node):
        node = super()._insert_between(e, previous, next_node)
        return self._make_position(node)

    def _add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def _add_last(self, e):
        return self._insert_between(e,self._trailer._prev, self._trailer)

    def _add_before(self, e, p):
        x = self._validate(p)
        return self._insert_between(e, x._prev, x)

    def _add_after(self, e, p):
        x = self._validate(p)
        return self._insert_between(e, x, x._next)

    def delete(self, p):
        x = self._validate(p)
        return self.delete_node(x)

    def replace(self, e, p):
        x = self._validate(p)
        previous_node = x._element
        x._element = e
        return previous_node


pL = PositionalList()
p = (pL._add_first(5))
# print((pL._add_first(5))._node._element)
print(pL.first().element())
q = ((pL._add_after(6,p)))
print(pL.before(q).element())
r = ((pL._add_before(7,p)))
print(pL.last().element())
print(pL.delete(pL.last()))
nodeeeeeeeeeeeeeeeeeeeeeee = pL.replace(17, r)
print(nodeeeeeeeeeeeeeeeeeeeeeee)
