"""
- https://ko.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort
"""


def partition(arr, l, r):
    """
    Args:
        arr (list): list containing int items
        l (int): left start index
        r (int): right end index

    Returns:
        q (int): partitioned index
    """
    q = j = l
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] > pivot:
            continue
        elif arr[j] <= pivot:
            arr[j], arr[q] = arr[q], arr[j]
            q += 1
    arr[r], arr[q] = arr[q], arr[r]
    return q


def quicksort(arr, l, r):
    if r - l < 1:
        return
    q = partition(arr, l, r)
    quicksort(arr, l, q - 1)
    quicksort(arr, q + 1, r)


def test_partition():
    assert partition([12, 7, 14, 9, 10, 11], 0, 5) == 3
    assert partition([0, 1], 0, 1) == 1


def test_quicksort():
    arr = [12, 7, 14, 9, 10, 11]
    quicksort(arr, 0, 5)
    assert arr == [7, 9, 10, 11, 12, 14]


if __name__ == "__main__":
    test_partition()
    test_quicksort()
