def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def foo(number):
    if isPrime(number):
        for i in range(1, len(str(number))):
            if not isPrime(int(str(number)[i:])):
                return 0
            if not isPrime(int(str(number)[:i])):
                return 0
    else:
        return 0
    print(number)
    return number


summ = 0
for i in range(10, 1000000):
    summ += foo(i)

print("result:", summ)
