class DynamicArray:
    def init(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1

    def getitem(self, index):
        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.data[index]

    def setitem(self, index, value):
        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.data[index] = value

    def insert_at(self, index, value):
        if index < 0:
            index += self.size

        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def pop(self, index=-1):
        if self.size == 0:
            raise IndexError("Pop from empty array")

        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        value = self.data[index]

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1
        self.data[self.size] = None

        return value

    def str(self):
        return str(self.data[:self.size])


# Testing the Dynamic Array

arr = DynamicArray()

print("1. Append:")
arr.append(10)
arr.append(20)
arr.append(30)
print(arr)

print("\n2. Get Item:")
print(arr[1])

print("\n3. Set Item:")
arr[1] = 25
print(arr)

print("\n4. Insert:")
arr.insert_at(1, 15)
print(arr)

print("\n5. Pop from end:")
print("Removed:", arr.pop())
print(arr)

print("\n6. Pop from specific index:")
print("Removed:", arr.pop(0))
print(arr)

print("\n7. Resize:")
print("Capacity:", arr.capacity)
