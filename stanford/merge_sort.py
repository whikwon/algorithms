def merge(arr1, arr2):
    new_arr = []

    while len(arr1) and len(arr2):
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    while len(arr1):
        new_arr.append(arr1.pop(0))
    while len(arr2):
        new_arr.append(arr2.pop(0))
    return new_arr


def split(arr):
    middle_idx = len(arr) // 2
    arr1 = arr[:middle_idx]
    arr2 = arr[middle_idx:]
    return [arr1, arr2]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        arr1, arr2 = split(arr)
        return merge(merge_sort(arr1), merge_sort(arr2))


def test_merge():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([3], [1, 2, 4]) == [1, 2, 3, 4]
    assert merge([], [1]) == [1]


def test_split():
    assert split([1, 2, 4]) == [[1], [2, 4]]
    assert split([1]) == [[], [1]]
    assert split([1, 2, 3, 4]) == [[1, 2], [3, 4]]


def test_merge_sort():
    assert merge_sort([4, 2, 1, 5, 7, 6, 3]) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
