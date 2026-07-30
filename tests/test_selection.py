"""Unit tests for deterministic and randomized selection algorithms."""

import unittest

from part1_selection.deterministic_select import deterministic_select
from part1_selection.randomized_select import randomized_select


class SelectionAlgorithmTests(unittest.TestCase):
    """Test both selection algorithm implementations."""

    def setUp(self):
        self.algorithms = [
            deterministic_select,
            randomized_select,
        ]

    def test_single_element(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([7], 0), 7)

    def test_unsorted_array(self):
        values = [5, 1, 3, 2, 4]

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(values, 0), 1)
                self.assertEqual(algorithm(values, 2), 3)
                self.assertEqual(algorithm(values, 4), 5)

    def test_duplicate_values(self):
        values = [8, 2, 8, 1, 5, 2, 9]

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(values, 0), 1)
                self.assertEqual(algorithm(values, 1), 2)
                self.assertEqual(algorithm(values, 2), 2)
                self.assertEqual(algorithm(values, 3), 5)
                self.assertEqual(algorithm(values, 5), 8)

    def test_all_values_equal(self):
        values = [4, 4, 4, 4]

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                for k in range(len(values)):
                    self.assertEqual(algorithm(values, k), 4)

    def test_sorted_array(self):
        values = [1, 2, 3, 4, 5]

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(values, 2), 3)

    def test_reverse_sorted_array(self):
        values = [5, 4, 3, 2, 1]

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(values, 2), 3)

    def test_original_array_is_not_modified(self):
        values = [5, 1, 3, 2, 4]
        original = values.copy()

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                algorithm(values, 2)
                self.assertEqual(values, original)

    def test_empty_array(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(ValueError):
                    algorithm([], 0)

    def test_negative_k(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(IndexError):
                    algorithm([1, 2, 3], -1)

    def test_k_out_of_range(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(IndexError):
                    algorithm([1, 2, 3], 3)

    def test_invalid_values_type(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(TypeError):
                    algorithm((1, 2, 3), 1)

    def test_invalid_k_type(self):
        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                with self.assertRaises(TypeError):
                    algorithm([1, 2, 3], 1.5)


if __name__ == "__main__":
    unittest.main()