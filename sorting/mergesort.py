"""
- https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort
"""


def split(arr):
    p, r = 0, len(arr)
    q = (r - p) // 2
    return q


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


def mergesort(arr):
    if len(arr) < 2:
        return arr

    p, r = 0, len(arr)
    q = split(arr)
    return merge(mergesort(arr[p:q]), mergesort(arr[q:r]))


def test_merge():
    assert merge([3, 7, 12, 14], [2, 6, 9, 11]) == [2, 3, 6, 7, 9, 11, 12, 14]


def test_mergesort():
    arr = [12, 7, 14, 9, 10, 11]
    assert mergesort(arr) == [7, 9, 10, 11, 12, 14]


if __name__ == "__main__":
    test_merge()
    test_mergesort()
