from binary_tree import BinaryTree

class Linked_BinaryTree(BinaryTree):

    class _Node():
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("P must be of position type")
        if p._container is not self:
            raise ValueError("P doesnot belong to this container")
        if p._node is p._node._parent:
            raise ValueError("P is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self): # creates an binary tree
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size # returns the total number of elements in the tree

    def root(self):
        # returns the root position of the tree
        return self._make_position(self._root)

    def parent(self, p):
        # return the position of p's parent
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        # returns the position of p's left child
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        # returns the position of p's right child
        node = self._validate(p)
        return self._make_position(node._right)

    def number_children(self, p):
        node = self._validate(p)
        numberofchildren = 0
        if node._left is not None:
            numberofchildren += 1
        elif node._right is not None:
            numberofchildren += 1

        return numberofchildren

    def _add_root(self, e):
        # places element e at the root of an empty tree and returns new position
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        # creates a new left child for position p
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return  self._make_position(node._left)

    def _add_right(self, p, e):
        # creates a new right child for position p
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def replace(self, p, e):
        # replaces the element at position p with element e and returns old element
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        # deletes the node at position p and replace that with it's child
        node = self._validate(p)
        if self.number_children(p) == 2:
            raise ValueError("p has 2 children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            elif node is parent._right:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p , t1, t2):
        # attach trees t1 and t2 as left and right subtrees of external p
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("given position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("given tree types must match")
        self._size = self._size + len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0





















