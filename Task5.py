class Node:
    def init(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def init(self):
        self.head = None
        self.tail = None
        self._size = 0

    def len(self):
        return self._size

    def iter(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def push_front(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def find(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def getitem(self, index):
        if index < 0:
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.push_front(value)
            return

        if index == self._size:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self._size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("Pop from empty list")

        value = self.head.value
        self.head = self.head.next

        self._size -= 1

        if self.head is None:
            self.tail = None

        return value

    def remove(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.pop_front()
            return True

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                self._size -= 1
                return True

            previous = current
            current = current.next

        return False

    def reverse(self):
        previous = None
        current = self.head

        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def repr(self):
        return str(list(self))


# Testing all methods

ll = LinkedList()

print("1. Append:")
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)

print("\n2. Push Front:")
ll.push_front(0)
print(ll)

print("\n3. Find:")
print("Index of 2:", ll.find(2))
print("Index of 10:", ll.find(10))

print("\n4. Get Item:")
print("Item at index 2:", ll[2])

print("\n5. Insert At:")
ll.insert_at(2, 10)
print(ll)

print("\n6. Pop Front:")
print("Removed:", ll.pop_front())
print(ll)

print("\n7. Remove:")
print("Removed 3:", ll.remove(3))
print(ll)

print("\n8. Reverse:")
ll.reverse()
print(ll)

print("\n9. Length:")
print("Length:", len(ll))
