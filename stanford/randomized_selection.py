import random


def partition(arr, p, q):
    """Assume that pivot index is p"""
    pivot_idx = random.randint(p, q)
    if pivot_idx != p:
        arr[p], arr[pivot_idx] = arr[pivot_idx], arr[p]

    pivot = arr[p]
    r = p + 1

    for i in range(p + 1, q + 1):
        if arr[i] < pivot:
            arr[r], arr[i] = arr[i], arr[r]
            r += 1

    arr[r - 1], arr[p] = arr[p], arr[r - 1]
    return r - 1


def randomized_selection(arr, p, q, idx):
    num_arr = len(arr)
    assert idx < num_arr and num_arr >= 1

    if len(arr) == 1:
        return arr[0]

    pivot = partition(arr, p, q)
    if pivot == idx:
        return arr[pivot]
    elif pivot > idx:
        return randomized_selection(arr, p, pivot - 1, idx)
    elif pivot < idx:
        return randomized_selection(arr, pivot + 1, q, idx)


def test_randomized_selection():
    arr = [1, 5, 3, 2, 4, 9, 6, 7]
    idx = 5
    assert randomized_selection(arr, 0, len(arr) - 1, idx) == sorted(arr)[idx]

    arr = [1]
    idx = 0
    assert randomized_selection(arr, 0, len(arr) - 1, idx) == sorted(arr)[idx]


def main():
    test_randomized_selection()


if __name__ == "__main__":
    main()
