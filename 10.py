def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if(number % i == 0):
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if(isPrime(i)):
        sum += i
print(sum)
