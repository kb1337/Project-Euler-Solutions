def isPandigital(n, p):
    "Check if n is 1 through p pandigital."
    if len(str(n)) != p:
        return False
    pan = "".join([str(x) for x in range(1, p + 1)])

    if "".join(sorted(str(n))) != pan:
        return False
    return True


def strConcat(*args):
    return "".join([str(x) for x in args])


def getDivisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n


# print(isPandigital(strConcat(39, 186, 7254), 9)) # True

products = set()
for n in range(1000, 10000):
    for div in getDivisors(n):
        if isPandigital(strConcat(n, div, n // div), 9):
            products.add(n)
            print(n, div, n // div)
print(f"Result: {sum(products)}")
