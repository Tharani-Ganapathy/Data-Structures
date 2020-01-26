class Deque():

    default_capacity = 5

    def __init__(self):
        self._size = 0
        self._data = [None] * Deque.default_capacity
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        back = (self._front+self._size1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % Deque.default_capacity
        self._size -= 1
        return element

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        back = (self._front + self._size - 1) % len(self._data)
        element = self._data[back]
        self._data[back] = None
        self._size -= 1
        return element

    def add_first(self, e):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        if self._front == 0 and self._size == 0:
            avail = self._size
        elif self._front == 0:
            self._front = (self._front - 1) % len(self._data)
            avail = self._front
        else:
            self._front -= 1
            avail = self._front
        self._data[avail] = e
        self._size += 1

        print(self._data)


    def add_last(self, e):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        avail = (self._size+self._front) % len(self._data)
        self._data[avail] = e
        self._size += 1
        print(self._data)

    def resize(self, cap):
        old_list = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old_list[walk]
            walk = (walk+1) % len(old_list)
        self._front = 0

DQ = Deque()
DQ.add_first(10)
DQ.add_first(20)
print(DQ.first())
DQ.add_last(50)
DQ.add_last(40)
DQ.add_first(30)
print(DQ.first())