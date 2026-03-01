"""Sorting utilities.

Provides a stable, simple `bubble_sort` implementation.
"""
from typing import Iterable, List, TypeVar

T = TypeVar("T")


def bubble_sort(values: Iterable[T]) -> List[T]:
    """Return a sorted list using the bubble sort algorithm.

    This function does not modify the input; it returns a new list.

    Args:
        values: An iterable of comparable items.

    Returns:
        A new list with the items sorted in non-decreasing order.
    """
    a = list(values)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Sorted:", bubble_sort(sample))
