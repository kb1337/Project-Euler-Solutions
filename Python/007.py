def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


i = 2
amount = 0

while True:
    if isPrime(i):
        amount += 1
        if amount == 10001:
            print(i)
            break
    i += 1
