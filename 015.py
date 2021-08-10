def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


def lattice(n):
    # nC2
    return factorial(2 * n) // (factorial(n) ** 2)


print(lattice(20))
