def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def formula(n, a, b):
    return n ** 2 + a * n + b


con_prime_count = 0
result = 1

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while isPrime(formula(n, a, b)):
            n += 1
        if n > con_prime_count:
            con_prime_count = n
            result = a * b
            print(con_prime_count, result)

print("Result:", result)
