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


def consecutive_prime(primes):
    counter_max = 2
    result = 0

    for i in range(0, len(primes)):
        total = 0

        for j in range(counter_max, len(primes) - i):
            # counter = len(primes[i : i + j])
            # if j > counter_max:
            total = sum(primes[i : i + j])

            # if total in primes:
            if isPrime(total) and total <= 1000000:
                counter_max = j
                result = total
                print(result, counter_max)

    return result


primes = generate_primes(1000000)
print("result:", consecutive_prime(primes))
