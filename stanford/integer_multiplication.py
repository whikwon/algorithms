def add(x, y):
    return x + y


def single_digit_mul(x, y):
    assert isinstance(x, int), isinstance(y, int)
    assert x < 10, y < 10
    result = 0
    for _ in range(x):
        result += y
    return result


def integer_mul(x, y):
    assert isinstance(x, int), isinstance(y, int)
    x_str = str(x)
    y_str = str(y)

    num_x_digits = len(x_str)
    num_y_digits = len(y_str)

    result = 0
    for j in range(num_y_digits):
        for i in range(num_x_digits):
            powers_of_ten = 10**(i + j)
            result += single_digit_mul(int(y_str[-j - 1]), int(
                x_str[-i - 1])) * powers_of_ten
    return result


def test_integer_mul():
    x = 5678
    y = 1234
    assert integer_mul(x, y) == 7006652


def main():
    test_integer_mul()


if __name__ == "__main__":
    main()
