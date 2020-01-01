def partition(arr, p, q, pivot):
    """Assume that pivot index is p"""
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


def deterministic_selection(arr, p, q, val):
    num_arr = len(arr[p: q + 1])
    if num_arr == 1:
        return p

    pivot = median_of_medians(arr[p: q + 1])

    r = partition(arr, p, q, pivot)

    if pivot == val:
        return r
    elif pivot < val:
        return deterministic_selection(arr, r + 1, q, val)
    elif pivot > val:
        return deterministic_selection(arr, p, r - 1, val)


def get_medians_of_sorted_5_elem_splits(arr):
    num_arr = len(arr)
    assert num_arr > 0

    i = 0
    medians = []

    while num_arr >= i + 5:
        sub_arr = sorted(arr[i: i + 5])
        medians.append(sub_arr[2])
        i += 5

    if num_arr - i:
        sub_arr = sorted(arr[i: num_arr])
        medians.append(sub_arr[(num_arr - i - 1) // 2])
    return medians


def median_of_medians(arr):
    medians = get_medians_of_sorted_5_elem_splits(arr)
    if len(medians) == 1:
        return medians[0]
    return median_of_medians(medians)


def test_get_medians_of_sorted_5_elem_splits():
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert get_medians_of_sorted_5_elem_splits(arr) == [5, 14, 28]

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4]
    assert get_medians_of_sorted_5_elem_splits(arr) == [5, 14]

    arr = [1, 2]
    assert get_medians_of_sorted_5_elem_splits(arr) == [1]


def test_median_of_medians():
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert median_of_medians(arr) == 14

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4]
    assert median_of_medians(arr) == 5


def test_deterministic_selection():
    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert deterministic_selection(arr, 0, 10, 20) == 9

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert deterministic_selection(arr, 0, 10, 15) == 8

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]
    assert deterministic_selection(arr, 0, 10, 9) == 5


def test_partition():
    arr = [1, 2, 9, 8, 4, 5, 6, 7, 10, 14, 11]
    assert partition(arr, 0, len(arr) - 1, 11) == 9
    assert arr == [1, 2, 9, 8, 4, 5, 6, 7, 10, 11, 14]

    arr = [1, 2, 9, 8, 4, 7, 10]
    assert partition(arr, 0, len(arr) - 1, 7) == 3
    assert arr == [1, 2, 4, 7, 9, 8, 10]

    arr = [1, 2]
    assert partition(arr, 0, len(arr) - 1, 2) == 1
    assert arr == [1, 2]

    arr = [1]
    assert partition(arr, 0, len(arr) - 1, 1) == 0
    assert arr == [1]

    arr = [1, 5, 3, 7, 9, 12, 14, 15, 20, 4, 28]


def main():
    test_get_medians_of_sorted_5_elem_splits()
    test_median_of_medians()
    test_partition()
    test_deterministic_selection()


if __name__ == "__main__":
    main()
