import random


def partition(arr, p, q, pivot):
    i = p
    r = None

    for j in range(p, q + 1):
        if arr[j] < pivot:
            if i != j:
                if i == r:
                    r = j
                arr[j], arr[i] = arr[i], arr[j]
            i += 1
        elif arr[j] == pivot:
            r = j

    arr[r], arr[i] = arr[i], arr[r]
    return i


def randomized_selection(arr, p, q, val):
    num_arr = len(arr[p:q + 1])

    if num_arr == 1:
        return p

    r = random.randint(p, q)
    pivot = arr[r]

    r = partition(arr, p, q, pivot)
    if pivot == val:
        return r
    elif pivot > val:
        return randomized_selection(arr, p, r - 1, val)
    elif pivot < val:
        return randomized_selection(arr, r + 1, q, val)


def test_randomized_selection():

    def assertion(arr, start, end, val):
        assert randomized_selection(arr, start, end, val) == sorted(
            arr[start:end + 1]).index(val)

    # 1-elem
    arr = [5, 3, 1]
    assertion(arr, 0, len(arr) - 3, 5)

    # 2-elem
    arr = [5, 3, 1]
    assertion(arr, 0, len(arr) - 2, 3)

    # 3-elem
    arr = [5, 3, 1]
    assertion(arr, 0, len(arr) - 1, 1)

    arr = [random.randint(0, 1000000) for i in range(1000)]
    for val in arr:
        arr_copy = arr.copy()
        assertion(arr_copy, 0, len(arr_copy) - 1, val)


def main():
    test_randomized_selection()


if __name__ == "__main__":
    main()
