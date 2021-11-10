# brute force solution


def find_triangle_count(p):
    count = 0
    for a in range(1, p // 3):
        for b in range(a, p - (2 * a)):
            c = (a ** 2 + b ** 2) ** 0.5
            if (a + b + c) == p:
                count += 1
                print(p, (a, b, c))
    return count


res_count = 0
res_p = 0

for p in range(1, 1001):
    count = find_triangle_count(p)
    if count > res_count:
        res_count = count
        res_p = p

print("p:", res_p, "\ncount:", res_count)
