def partition(arr, p, q):
    """Assume that pivot index is p"""
    pivot = arr[p]
    r = p + 1

    for i in range(p + 1, q + 1):
        if arr[i] < pivot:
            arr[r], arr[i] = arr[i], arr[r]
            r += 1

    arr[r - 1], arr[p] = arr[p], arr[r - 1]
    return r - 1


def quicksort(arr, p, q):
    if q - p < 1:
        return

    r = partition(arr, p, q)
    quicksort(arr, p, r - 1)
    quicksort(arr, r + 1, q)
    return arr


def test_partition():
    arr = [5, 6, 3, 4, 7, 9, 2, 1]
    assert partition(arr, 0, 4) == 2

    arr = [6, 5, 3, 4]
    assert partition(arr, 0, 1) == 1

    arr = [6, 5, 3, 4]
    assert partition(arr, 0, 2) == 2


def test_quicksort():
    arr = [5, 6, 3, 4, 7, 9, 2, 1]
    assert quicksort(arr, 0, 7) == [1, 2, 3, 4, 5, 6, 7, 9]

    arr = [1, 0]
    assert quicksort(arr, 0, 1) == [0, 1]

    arr = [1, 2, 3, 4, 5, 6]
    assert quicksort(arr, 0, 5) == [1, 2, 3, 4, 5, 6]

    import random
    arr = [random.randint(0, 1000) for _ in range(1000)]
    assert quicksort(arr, 0, len(arr) - 1) == sorted(arr)


def main():
    test_partition()
    test_quicksort()


if __name__ == "__main__":
    main()
