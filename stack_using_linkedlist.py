class LinkedList:
    # LIFO Stack implementation using a singly linked list for storage
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next1):
            self._element = element
            self._next = next1
# stack methods
    def __init__(self):
        # create an empty stack
        self._head = None
        self._size = 0

    def __len__(self):
        # return the number of elements in the stack
        return self._size

    def is_empty(self):
        # return true if the stack is empty
        return self._size == 0

    def print_stack(self):
        node_i = self._head
        stack_size = self._size
        while stack_size > 1:
            print(format(node_i._element), end="->")
            stack_size -= 1
            node_i = node_i._next
        print(node_i._element)

    def push(self, e):
        # add element to the top of the stack
        self._head = self._Node(e, self._head)
        self._size += 1
        self.print_stack()

    def top(self):
        # return element at the top of the stack
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._head._element

    def pop(self):
        # Remove and return the element from the top of the stack(i.e., LIFO).
        # Raise Empty exception if the stack is empty
        if self.is_empty():
            raise ValueError("Stack is empty")
        result = self._head._element
        self._head = self._head._next    # reassign the former top node
        self._size -= 1
        return result


tg = LinkedList()
tg.push(1)
tg.push(2)
tg.push(3)
tg.push(4)
tg.push(5)
# print("The element at the top of the stack is {0}".format(tg.top()))
# print("The element popped is {0}".format(tg.pop()))
print(tg.push(6))
# print(tg.is_empty())
# print("The length of the stack is {0}".format(tg.__len__()))
