def single_digit_mul(x, y):
    assert isinstance(x, int), isinstance(y, int)
    assert x < 10, y < 10
    return x * y


def divmod10(x, y):
    assert isinstance(x, int), isinstance(y, int)
    num_digits = len(str(x))
    if num_digits <= y:
        return 0
    else:
        return int(str(x)[:-y])


def remainder10(x, y):
    assert isinstance(x, int), isinstance(y, int)
    num_digits = len(str(x))
    if num_digits < y:
        return x
    else:
        return int(str(x)[-y:])


def karatsuba_mul(x, y):
    num_x_digits = len(str(x))
    num_y_digits = len(str(y))

    if num_x_digits < 2 and num_y_digits < 2:
        return x * y

    num_digits_div = max(num_x_digits, num_y_digits) // 2

    a = divmod10(x, num_digits_div)
    b = remainder10(x, num_digits_div)

    c = divmod10(y, num_digits_div)
    d = remainder10(y, num_digits_div)

    ad_bc = karatsuba_mul(a + b, c + d) - karatsuba_mul(b, d) - karatsuba_mul(
        a, c)
    result = 10**(num_digits_div * 2) * karatsuba_mul(
        a, c) + 10**num_digits_div * ad_bc + karatsuba_mul(b, d)
    return result


def test_karatsuba_mul():
    x = 567129831893729
    y = 123419312314
    assert karatsuba_mul(x, y) == x * y


def main():
    test_karatsuba_mul()


if __name__ == "__main__":
    main()
