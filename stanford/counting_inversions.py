def sort_and_count(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        num_arr = len(arr)
        left_half = arr[:num_arr // 2]
        right_half = arr[num_arr // 2:]

        sorted_left_half, x = sort_and_count(left_half)
        sorted_right_half, y = sort_and_count(right_half)
        sorted_arr, z = merge_and_count_split_inv(left_half, right_half)
        return sorted_arr, x + y + z


def merge_and_count_split_inv(arr1, arr2):
    count = 0
    sorted_arr = []

    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))
            count += len(arr1)

    if arr1:
        sorted_arr.extend(arr1)
    elif arr2:
        sorted_arr.extend(arr2)
    return sorted_arr, count


def test_counting_inv():
    arr = [1, 3, 5, 2, 4, 6]
    assert sort_and_count(arr) == ([1, 2, 3, 4, 5, 6], 3)


if __name__ == "__main__":
    test_counting_inv()
