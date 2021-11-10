def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_primes(n):
    primes = list()
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)

    return primes


def isGoldbach(n):
    primes = generate_primes(n)
    goldbach = 0
    for prime in primes:
        for i in range(n - prime):
            goldbach = prime + 2 * i ** 2
            if n == goldbach:
                return True

    return False


# odd composite numbers
for i in range(3, 6000, 2):
    if not isPrime(i):
        if not isGoldbach(i):
            print(i)
            exit()
