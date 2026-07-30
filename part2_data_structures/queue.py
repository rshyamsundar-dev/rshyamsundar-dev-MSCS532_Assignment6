"""Queue implementation using a circular array."""


class Queue:
    """A first-in, first-out queue."""

    def __init__(self, capacity: int = 5):
        """Initialize an empty queue."""
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Return True if the queue is full."""
        return self.size == self.capacity

    def enqueue(self, value):
        """Insert an element at the rear."""
        if self.is_full():
            raise OverflowError("Queue is full")

        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty")

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return value

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.data[self.front]

    def display(self):
        """Return queue contents from front to rear."""
        items = []

        index = self.front

        for _ in range(self.size):
            items.append(self.data[index])
            index = (index + 1) % self.capacity

        return items


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue after enqueue:")
    print(queue.display())

    print("\nFront element:", queue.peek())

    print("Dequeued:", queue.dequeue())

    print("\nQueue after dequeue:")
    print(queue.display())

    queue.enqueue(40)
    queue.enqueue(50)

    print("\nQueue after additional enqueue:")
    print(queue.display())

    print("\nQueue empty?", queue.is_empty())