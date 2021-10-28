def distinctPrimeFactorCount(n):
    count = 0
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    return count


i = 1
while True:
    if (
        distinctPrimeFactorCount(i) == 4
        and distinctPrimeFactorCount(i + 1) == 4
        and distinctPrimeFactorCount(i + 2) == 4
        and distinctPrimeFactorCount(i + 3) == 4
    ):
        print(i, i + 1, i + 2, i + 3)
        break
    i += 1
