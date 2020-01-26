class LinkedQueue:
    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        # return the number of elements in the stack
        return self._size

    def is_empty(self):
        # return true if the stack is empty
        return self._size == 0

    def first(self):
        # return element at the top of the stack
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

tg = LinkedQueue()
tg.enqueue(1)
tg.enqueue(2)
print(tg.dequeue())