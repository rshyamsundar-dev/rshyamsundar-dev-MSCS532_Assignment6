"""Unit tests for elementary data structures."""

import unittest

from part2_data_structures.dynamic_array import DynamicArray
from part2_data_structures.stack import Stack
from part2_data_structures.queue import Queue
from part2_data_structures.linked_list import SinglyLinkedList
from part2_data_structures.matrix import Matrix


class TestDynamicArray(unittest.TestCase):

    def test_append_insert_delete(self):
        array = DynamicArray()

        array.append(10)
        array.append(20)
        array.insert(1, 15)

        self.assertEqual(array.display(), [10, 15, 20])

        array.delete(1)

        self.assertEqual(array.display(), [10, 20])


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()

        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue = Queue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.display(), [20, 30])


class TestLinkedList(unittest.TestCase):

    def test_insert_delete_search(self):
        linked = SinglyLinkedList()

        linked.insert_at_end(10)
        linked.insert_at_end(20)
        linked.insert_at_end(30)

        self.assertTrue(linked.search(20))

        linked.delete(20)

        self.assertFalse(linked.search(20))
        self.assertEqual(linked.traverse(), [10, 30])

class TestMatrix(unittest.TestCase):

    def test_access_update_insert_and_delete(self):
        matrix = Matrix(2, 2)

        matrix.set(0, 0, 10)
        matrix.set(1, 1, 20)

        self.assertEqual(matrix.get(0, 0), 10)
        self.assertEqual(matrix.get(1, 1), 20)

        matrix.insert_row(1, [30, 40])

        self.assertEqual(matrix.rows, 3)
        self.assertEqual(matrix.get(1, 0), 30)
        self.assertEqual(matrix.get(1, 1), 40)

        matrix.delete_row(0)

        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.get(0, 0), 30)

if __name__ == "__main__":
    unittest.main()