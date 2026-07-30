"""Deterministic selection using the Median of Medians algorithm."""


def deterministic_select(values: list[int], k: int) -> int:
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

    return _select(values.copy(), k)


def _select(values: list[int], k: int) -> int:
    """Recursively select the kth smallest element."""
    if len(values) <= 5:
        return sorted(values)[k]

    pivot = _median_of_medians(values)

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
        return _select(lower, k)

    if k < len(lower) + len(equal):
        return pivot

    adjusted_k = k - len(lower) - len(equal)
    return _select(higher, adjusted_k)


def _median_of_medians(values: list[int]) -> int:
    """Choose a pivot using medians of groups of five."""
    groups = [
        values[index:index + 5]
        for index in range(0, len(values), 5)
    ]

    medians = []

    for group in groups:
        sorted_group = sorted(group)
        median_index = len(sorted_group) // 2
        medians.append(sorted_group[median_index])

    if len(medians) <= 5:
        sorted_medians = sorted(medians)
        return sorted_medians[len(sorted_medians) // 2]

    middle_index = len(medians) // 2
    return _select(medians, middle_index)


if __name__ == "__main__":
    sample_values = [8, 2, 8, 1, 5, 2, 9]
    k = 3

    result = deterministic_select(sample_values, k)

    print("Original values:", sample_values)
    print(f"Element at sorted index {k}:", result)