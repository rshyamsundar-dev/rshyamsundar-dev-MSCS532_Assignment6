"""Singly Linked List implementation."""


class Node:
    """Represents one node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Implementation of a singly linked list."""

    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert a node at the end."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_beginning(self, value):
        """Insert a node at the beginning."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Delete the first node containing the given value."""
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        previous = self.head
        current = self.head.next

        while current:
            if current.data == value:
                previous.next = current.next
                return

            previous = current
            current = current.next

    def search(self, value):
        """Return True if the value exists."""
        current = self.head

        while current:
            if current.data == value:
                return True

            current = current.next

        return False

    def traverse(self):
        """Return all elements as a list."""
        elements = []

        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return elements


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("After inserting at end:")
    print(linked_list.traverse())

    linked_list.insert_at_beginning(5)

    print("\nAfter inserting at beginning:")
    print(linked_list.traverse())

    print("\nSearch for 20:", linked_list.search(20))
    print("Search for 100:", linked_list.search(100))

    linked_list.delete(20)

    print("\nAfter deleting 20:")
    print(linked_list.traverse())