"""Dynamic Array implementation from scratch."""


class DynamicArray:
    """A simple dynamic array implementation."""

    def __init__(self, capacity: int = 4):
        """Initialize the array."""
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def __len__(self):
        """Return the number of stored elements."""
        return self.size

    def _resize(self):
        """Double the array capacity."""
        self.capacity *= 2

        new_data = [None] * self.capacity

        for index in range(self.size):
            new_data[index] = self.data[index]

        self.data = new_data

    def append(self, value):
        """Add an element to the end."""
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """Insert an element at a specific position."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if self.size == self.capacity:
            self._resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def delete(self, index):
        """Delete an element at a specific position."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

    def get(self, index):
        """Return the element at index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.data[index]

    def set(self, index, value):
        """Update an element."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.data[index] = value

    def display(self):
        """Return all stored elements."""
        return self.data[:self.size]


if __name__ == "__main__":
    array = DynamicArray()

    array.append(10)
    array.append(20)
    array.append(30)

    print("After append:")
    print(array.display())

    array.insert(1, 15)

    print("\nAfter insert:")
    print(array.display())

    array.delete(2)

    print("\nAfter delete:")
    print(array.display())

    print("\nElement at index 1:", array.get(1))

    array.set(1, 99)

    print("\nAfter update:")
    print(array.display())