def euclidean_dist(p_1, p_2):
    assert len(p_1) == len(p_2)

    dist = 0
    num_elems = len(p_1)

    for i in range(num_elems):
        dist += (p_1[i] - p_2[i])**2

    dist = dist**0.5
    return dist


def brute_force(p):
    assert len(p) > 1
    len_p = len(p)
    min_dist = float("inf")

    for i in range(len_p):
        for j in range(i + 1, len_p):
            dist = euclidean_dist(p[i], p[j])
            if dist < min_dist:
                closest_pair = (p[i], p[j])
                min_dist = dist
    return closest_pair


def sort_and_find_closest_pair(p):
    p_x = sorted(p, key=lambda x: x[0])  # check the algorithm
    p_y = sorted(p, key=lambda x: x[0])  # check the algorithm

    p_1, p_2 = closest_pair(p_x, p_y)
    return p_1, p_2


def closest_pair(p_x, p_y):
    # base case
    if len(p_x) <= 3:
        return brute_force(p_x)

    len_p = len(p_x)
    x_mid_idx = len_p // 2
    x_mid = p_x[x_mid_idx][0]

    q_x = p_x[:x_mid_idx]
    r_x = p_x[x_mid_idx:]
    q_y = []
    r_y = []

    for (x, y) in p_y:
        if x < x_mid:
            q_y.append([x, y])
        else:
            r_y.append([x, y])

    p_1, q_1 = closest_pair(q_x, q_y)
    p_2, q_2 = closest_pair(r_x, r_y)

    pair = None
    dist_1 = euclidean_dist(p_1, q_1)
    dist_2 = euclidean_dist(p_2, q_2)

    if dist_1 < dist_2:
        pair = (p_1, q_1)
        delta = dist_1
    else:
        pair = (p_2, q_2)
        delta = dist_2

    p_3, q_3 = closest_split_pair(p_x, p_y, delta)
    dist_3 = euclidean_dist(p_3, q_3)

    if dist_3 < delta:
        pair = (p_3, q_3)
        delta = dist_3
    return pair


def closest_split_pair(p_x, p_y, delta):
    len_p = len(p_x)
    x_bar = p_x[len_p // 2][0]
    s_y = []

    for (x, y) in p_y:
        if x_bar - delta <= x <= x_bar + delta:
            s_y.append([x, y])

    len_s_y = len(s_y)
    best_delta = float("inf")
    best_pair = ([float("inf"), float("inf")], [float("inf"), float("inf")])

    for i in range(len_s_y - 1):
        p_1 = s_y[i]
        for j in range(i + 1, min(i + 7, len_s_y)):
            p_2 = s_y[j]
            dist = euclidean_dist(p_1, p_2)
            if dist < best_delta:
                best_delta = dist
                best_pair = (p_1, p_2)
    return best_pair


def test_brute_force():
    p = [[1, 1], [2, 1], [5, 1]]
    assert brute_force(p) == ([1, 1], [2, 1])


def test_closest_split_pair():
    delta = 3
    p_x = [[1, 2], [2, 5], [3, 1], [4, 7], [5, 3]]
    p_y = [[3, 1], [1, 2], [5, 3], [2, 5], [4, 7]]
    assert sorted(closest_split_pair(p_x, p_y,
                                     delta)) == sorted(brute_force(p_y))


def test_closest_pair():
    import random
    randint_generator = lambda: random.randint(1, 1000)
    p = [[randint_generator(), randint_generator()] for _ in range(100)]
    assert sorted(sort_and_find_closest_pair(p)) == sorted(brute_force(p))


def main():
    test_brute_force()
    test_closest_split_pair()
    test_closest_pair()


if __name__ == "__main__":
    main()
