from itertools import combinations


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def checkArithmeticTriples(myList):
    comb = combinations(myList, 3)
    for c in comb:
        c = sorted(c)
        if abs(c[0] - c[1]) == abs(c[1] - c[2]):
            print(c)
            print("".join([str(x) for x in c]))


# 4-digit primes
primeList = list()
for i in range(1001, 10000, 2):
    if isPrime(i):
        primeList.append(i)


for i in range(len(primeList)):
    myList = [primeList[i]]
    for j in range(i + 1, len(primeList)):
        if "".join(sorted(str(primeList[i]))) == "".join(sorted(str(primeList[j]))):
            myList.append(primeList[j])
    if len(myList) > 2:
        checkArithmeticTriples(myList)
