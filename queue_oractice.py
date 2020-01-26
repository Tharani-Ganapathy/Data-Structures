class Array_Queue():

    default_capacity = 5

    def __init__(self):
        self._size = 0
        self._data = [None] * Array_Queue.default_capacity
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % Array_Queue.default_capacity
        self._size -= 1
        return element


    def enqueue(self, e):
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

AQ = Array_Queue()
AQ.enqueue(10)
AQ.enqueue(20)
AQ.enqueue(30)
AQ.enqueue(40)
AQ.enqueue(50)
AQ.enqueue(60)
# print(AQ.dequeue())
print(AQ.is_empty())
print(AQ.__len__())
print(AQ.first())




