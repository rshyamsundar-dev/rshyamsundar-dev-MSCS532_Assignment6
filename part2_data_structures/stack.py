"""Stack implementation using an array."""


class Stack:
    """A last-in, first-out stack."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, value):
        """Add an item to the top of the stack."""
        self.items.append(value)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")

        return self.items[-1]

    def is_empty(self):
        """Return True when the stack has no elements."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements."""
        return len(self.items)

    def display(self):
        """Return the stack elements from bottom to top."""
        return self.items.copy()


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:")
    print(stack.display())

    print("\nTop element:", stack.peek())
    print("Removed element:", stack.pop())

    print("\nStack after pop:")
    print(stack.display())

    print("\nStack size:", stack.size())
    print("Is stack empty?", stack.is_empty())