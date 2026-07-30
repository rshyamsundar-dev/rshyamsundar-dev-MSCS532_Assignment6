"""Demonstration program for Assignment 6."""

from part1_selection.deterministic_select import deterministic_select
from part1_selection.randomized_select import randomized_select
from part2_data_structures.dynamic_array import DynamicArray
from part2_data_structures.matrix import Matrix
from part2_data_structures.stack import Stack
from part2_data_structures.queue import Queue
from part2_data_structures.linked_list import SinglyLinkedList


def demonstrate_selection_algorithms() -> None:
    """Demonstrate deterministic and randomized selection."""
    print("=" * 60)
    print("PART 1: SELECTION ALGORITHMS")
    print("=" * 60)

    values = [12, 3, 5, 7, 4, 19, 26, 5, 8]
    k = 4

    deterministic_result = deterministic_select(values, k)
    randomized_result = randomized_select(values, k)

    print("Original array:", values)
    print("Sorted array:", sorted(values))
    print(f"Selected index: {k}")
    print("Deterministic result:", deterministic_result)
    print("Randomized result:", randomized_result)


def demonstrate_dynamic_array() -> None:
    """Demonstrate dynamic-array operations."""
    print("\n" + "=" * 60)
    print("DYNAMIC ARRAY")
    print("=" * 60)

    array = DynamicArray()

    array.append(10)
    array.append(20)
    array.append(30)
    print("After append:", array.display())

    array.insert(1, 15)
    print("After inserting 15 at index 1:", array.display())

    array.delete(2)
    print("After deleting index 2:", array.display())

    array.set(1, 99)
    print("After setting index 1 to 99:", array.display())

    print("Value at index 1:", array.get(1))


def demonstrate_matrix() -> None:
    """Demonstrate matrix operations."""
    print("\n" + "=" * 60)
    print("MATRIX")
    print("=" * 60)

    matrix = Matrix(2, 3)

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("Original matrix:")
    matrix.display()

    matrix.insert_row(1, [7, 8, 9])

    print("After inserting a row:")
    matrix.display()

    matrix.delete_row(0)

    print("After deleting row 0:")
    matrix.display()


def demonstrate_stack() -> None:
    """Demonstrate stack operations."""
    print("\n" + "=" * 60)
    print("STACK")
    print("=" * 60)

    stack = Stack()

    stack.push("Task A")
    stack.push("Task B")
    stack.push("Task C")

    print("Stack contents:", stack.display())
    print("Top item:", stack.peek())
    print("Removed item:", stack.pop())
    print("Stack after pop:", stack.display())


def demonstrate_queue() -> None:
    """Demonstrate circular-queue operations."""
    print("\n" + "=" * 60)
    print("CIRCULAR QUEUE")
    print("=" * 60)

    queue = Queue(capacity=5)

    queue.enqueue("Request 1")
    queue.enqueue("Request 2")
    queue.enqueue("Request 3")

    print("Queue contents:", queue.display())
    print("Front item:", queue.peek())
    print("Removed item:", queue.dequeue())
    print("Queue after dequeue:", queue.display())

    queue.enqueue("Request 4")
    queue.enqueue("Request 5")

    print("Queue after additional enqueue:", queue.display())


def demonstrate_linked_list() -> None:
    """Demonstrate singly linked-list operations."""
    print("\n" + "=" * 60)
    print("SINGLY LINKED LIST")
    print("=" * 60)

    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_beginning(5)

    print("Linked-list contents:", linked_list.traverse())
    print("Contains 20:", linked_list.search(20))
    print("Contains 100:", linked_list.search(100))

    linked_list.delete(20)

    print("After deleting 20:", linked_list.traverse())


def main() -> None:
    """Run all Assignment 6 demonstrations."""
    print("\nMSCS 532 ASSIGNMENT 6 DEMONSTRATION\n")

    demonstrate_selection_algorithms()
    demonstrate_dynamic_array()
    demonstrate_matrix()
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_linked_list()

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()