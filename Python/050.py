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
    counter_max = 0
    result = 0
    my_list = list()

    for i in range(0, len(primes)):
        total = 0
        for j in range(2, len(primes) - i):
            total = sum(primes[i : i + j])
            if total < 1000000:
                my_list.append([total, j])
            else:
                break

    for total, prime_amount in my_list:
        if isPrime(total) and prime_amount > counter_max:
            counter_max = prime_amount
            result = total
            print(result, counter_max)

    return result


primes = generate_primes(1000000)

print("result:", consecutive_prime(primes))
