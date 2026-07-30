"""Randomized selection using the Quickselect algorithm."""

import random


def randomized_select(values: list[int], k: int) -> int:
    """
    Return the element at index k in sorted order.

    The value of k is zero-based. For example, k=0 returns the
    smallest element.

    Args:
        values: A list of integers.
        k: The zero-based order statistic.

    Returns:
        The kth smallest value.

    Raises:
        ValueError: If values is empty.
        IndexError: If k is outside the valid range.
        TypeError: If values is not a list or k is not an integer.
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list")

    if not isinstance(k, int):
        raise TypeError("k must be an integer")

    if not values:
        raise ValueError("values cannot be empty")

    if k < 0 or k >= len(values):
        raise IndexError("k is outside the valid range")

    return _randomized_select(values.copy(), k)


def _randomized_select(values: list[int], k: int) -> int:
    """Recursively select the kth smallest element."""
    if len(values) == 1:
        return values[0]

    pivot = random.choice(values)

    lower = []
    equal = []
    higher = []

    for value in values:
        if value < pivot:
            lower.append(value)
        elif value > pivot:
            higher.append(value)
        else:
            equal.append(value)

    if k < len(lower):
        return _randomized_select(lower, k)

    if k < len(lower) + len(equal):
        return pivot

    adjusted_k = k - len(lower) - len(equal)
    return _randomized_select(higher, adjusted_k)


if __name__ == "__main__":
    sample_values = [8, 2, 8, 1, 5, 2, 9]
    k = 3

    result = randomized_select(sample_values, k)

    print("Original values:", sample_values)
    print(f"Element at sorted index {k}:", result)