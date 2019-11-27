import numpy as np


def split_into_four_submatrices(arr):
    m, n = arr.shape
    c_m, c_n = m // 2, n // 2
    A, B, C, D = arr[:c_m, :c_n], arr[:c_m, c_n:], arr[c_m:, :c_n], arr[c_m:,
                                                                        c_n:]
    return A, B, C, D


def merge_four_submatrices(arr1, arr2, arr3, arr4):
    assert arr1.shape[0] == arr2.shape[0]
    assert arr1.shape[1] == arr3.shape[1]
    assert arr2.shape[1] == arr4.shape[1]
    assert arr3.shape[0] == arr4.shape[0]
    m, n = arr1.shape
    q, r = arr4.shape
    arr = np.zeros([m + q, n + r])

    arr[:m, :n] = arr1
    arr[:m, n:] = arr2
    arr[m:, :n] = arr3
    arr[m:, n:] = arr4
    return arr


def strassen_matrix_mul(arr1, arr2):
    """Consider only for the nxn matrices"""
    assert arr1.shape[1] == arr2.shape[0]

    if arr1.shape[0] <= 2:
        return np.dot(arr1, arr2)

    A, B, C, D = split_into_four_submatrices(arr1)
    E, F, G, H = split_into_four_submatrices(arr2)

    P1 = strassen_matrix_mul(A, F - H)
    P2 = strassen_matrix_mul(A + B, H)
    P3 = strassen_matrix_mul(C + D, E)
    P4 = strassen_matrix_mul(D, G - E)
    P5 = strassen_matrix_mul(A + D, E + H)
    P6 = strassen_matrix_mul(B - D, G + H)
    P7 = strassen_matrix_mul(A - C, E + F)

    mul_A = P5 + P4 - P2 + P6
    mul_B = P1 + P2
    mul_C = P3 + P4
    mul_D = P1 + P5 - P3 - P7
    return merge_four_submatrices(mul_A, mul_B, mul_C, mul_D)


def test_merge_four_submatrices():
    arr1 = np.array([[0, 0], [0, 0]])
    arr2 = np.array([[1, 1, 1], [1, 1, 1]])
    arr3 = np.array([[2, 2], [2, 2]])
    arr4 = np.array([[3, 3, 3], [3, 3, 3]])
    ans = np.array([[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [2, 2, 3, 3, 3],
                    [2, 2, 3, 3, 3]])
    assert (merge_four_submatrices(arr1, arr2, arr3, arr4) == ans).all()


def test_strassen_matrix_mul():
    arr1 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    arr2 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    assert (strassen_matrix_mul(arr1, arr2) == np.dot(arr1, arr2)).all()


def main():
    test_merge_four_submatrices()
    test_strassen_matrix_mul()


if __name__ == "__main__":
    main()
