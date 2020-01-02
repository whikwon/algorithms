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


def get_medians_of_sorted_5_elem_splits(arr):
    num_arr = len(arr)
    assert num_arr > 0

    i = 0
    medians = []

    while num_arr >= i + 5:
        sub_arr = sorted(arr[i:i + 5])
        medians.append(sub_arr[2])
        i += 5

    if num_arr - i:
        sub_arr = sorted(arr[i:num_arr])
        medians.append(sub_arr[(num_arr - i - 1) // 2])
    return medians


def median_of_medians(arr):
    medians = get_medians_of_sorted_5_elem_splits(arr)
    if len(medians) == 1:
        return medians[0]
    return median_of_medians(medians)


def deterministic_selection(arr, p, q, val):
    num_arr = len(arr[p:q + 1])
    if num_arr == 1:
        return p

    pivot = median_of_medians(arr[p:q + 1])

    r = partition(arr, p, q, pivot)

    if pivot == val:
        return r
    elif pivot < val:
        return deterministic_selection(arr, r + 1, q, val)
    elif pivot > val:
        return deterministic_selection(arr, p, r - 1, val)


def test_get_medians_of_sorted_5_elem_splits():
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert get_medians_of_sorted_5_elem_splits(arr) == [5, 14, 28]

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4]
    assert get_medians_of_sorted_5_elem_splits(arr) == [5, 14]

    arr = [1, 2]
    assert get_medians_of_sorted_5_elem_splits(arr) == [1]


def test_partition():
    # 1-item
    arr = [1]
    assert partition(arr, 0, len(arr) - 1, 1) == 0
    assert arr == [1]

    # all smaller values before pivot
    arr = [1, 2, 5, 4, 9, 7]
    assert partition(arr, 0, len(arr) - 1, 5) == 3
    assert arr == [1, 2, 4, 5, 9, 7]

    # all larger values before pivot
    arr = [3, 4, 5, 1, 2]
    assert partition(arr, 0, len(arr) - 1, 3) == 2
    assert arr == [1, 2, 3, 5, 4]

    # duplicated values: first one
    arr = [3, 4, 3, 3, 1, 2]
    assert partition(arr, 0, len(arr) - 1, 3) == 2
    assert arr == [1, 2, 3, 3, 3, 4]

    # start with large value
    arr = [5, 1, 2, 3, 4]
    assert partition(arr, 0, len(arr) - 1, 5) == 4
    assert arr == [1, 2, 3, 4, 5]

    # start with small value
    arr = [1, 2, 3, 4, 5]
    assert partition(arr, 0, len(arr) - 1, 1) == 0
    assert arr == [1, 2, 3, 4, 5]


def test_median_of_medians():
    # 1-elem
    arr = [1]
    assert median_of_medians(arr) == 1

    # less than 5-elem
    arr = [1, 3, 5]
    assert median_of_medians(arr) == 3

    # 10-elem
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4]
    assert median_of_medians(arr) == 5

    # 11-elem
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert median_of_medians(arr) == 14


def test_deterministic_selection():

    def assertion(arr, start, end, val):
        assert deterministic_selection(arr, start, end, val) == sorted(
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
    test_get_medians_of_sorted_5_elem_splits()
    test_median_of_medians()
    test_partition()
    test_deterministic_selection()


if __name__ == "__main__":
    main()
