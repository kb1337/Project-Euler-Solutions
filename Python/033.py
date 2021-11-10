def find_similar_digit(a, b):
    if a == b or a > b:
        return 1, 1
    # only non-trivial examples
    if a % 10 == 0 and b % 10 == 0:
        return 1, 1

    n1 = [x for x in str(a)]
    n2 = [y for y in str(b)]

    hasSimilar = 0
    for i in n1:
        for j in n2:
            if i == j:
                n1.remove(i)
                n2.remove(i)
                hasSimilar = 1

    if not hasSimilar:
        return 1, 1

    n1 = int("".join(n1))
    n2 = int("".join(n2))
    try:
        if (n1 / n2) == (a / b):
            # print("a: {} b: {}\nn1: {} n2: {}\n".format(a, b, n1, n2))
            return n1, n2
        else:
            return 1, 1
    except ZeroDivisionError:
        return 1, 1


# lowest common terms
def lct(n1, n2):
    for i in range(2, 100):
        while n1 % i == 0 and n2 % i == 0:
            n1 //= i
            n2 //= i
    return n1, n2


numerator = 1
denominator = 1
for i in range(10, 100):
    for j in range(10, 100):
        a, b = find_similar_digit(i, j)
        numerator *= a
        denominator *= b

numerator, denominator = lct(numerator, denominator)
print("{} / {}".format(numerator, denominator))
