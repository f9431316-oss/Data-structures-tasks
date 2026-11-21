class SlowQueue:
    def init(self):
        self._items = []

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if len(self._items) == 0:
            raise IndexError("Dequeue from empty queue")

        return self._items.pop(0)

    def len(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def repr(self):
        return str(self._items)


class CircularQueue:
    def init(self, capacity=5, grow_on_full=False):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self._items = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.size = 0
        self.grow_on_full = grow_on_full

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            if self.grow_on_full:
                self._grow()
            else:
                raise OverflowError("Queue is full")

        tail = (self.head + self.size) % self.capacity
        self._items[tail] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        value = self._items[self.head]
        self._items[self.head] = None

        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return value

    def _grow(self):
        new_capacity = self.capacity * 2
        new_items = [None] * new_capacity

        for i in range(self.size):
            index = (self.head + i) % self.capacity
            new_items[i] = self._items[index]

        self._items = new_items
        self.capacity = new_capacity
        self.head = 0

    def repr(self):
        result = []

        for i in range(self.size):
            index = (self.head + i) % self.capacity
            result.append(self._items[index])

        return str(result)


print("SLOW QUEUE TEST")

q1 = SlowQueue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print("Queue:", q1)
print("Dequeue:", q1.dequeue())
print("Queue after dequeue:", q1)
print("Length:", len(q1))
print("Is empty:", q1.is_empty())

print("CIRCULAR QUEUE TEST")

q2 = CircularQueue(5)

q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)

print("Queue:", q2)
print("Dequeue:", q2.dequeue())
print("Queue after dequeue:", q2)

q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(60)

print("Queue after wrap around:", q2)
print("Length:", len(q2))
print("Is full:", q2.is_full())

print("CIRCULAR QUEUE GROW TEST")

q3 = CircularQueue(2, grow_on_full=True)

q3.enqueue(1)
q3.enqueue(2)
q3.enqueue(3)

print("Queue:", q3)
print("New capacity:", q3.capacity)

print("Dequeue:", q3.dequeue())
print("Queue after dequeue:", q3)

print("EMPTY QUEUE TEST")

q4 = CircularQueue(5)

print("Is empty:", q4.is_empty())

try:
    q4.dequeue()
except IndexError as error:
    print("Error:", error)
