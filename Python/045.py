def triangle(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


amount = 60000

t_list = [triangle(i) for i in range(285, amount)]
p_list = [pentagonal(i) for i in range(165, amount)]
h_list = [hexagonal(i) for i in range(143, amount)]

[print(t) for t in t_list if t in p_list and t in h_list]
