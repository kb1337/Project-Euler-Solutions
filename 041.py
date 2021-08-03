def crate_n_digit_number(number):
    num = ""
    for i in range(1, len(str(number)) + 1):
        num += str(i)
    return num


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


panList = list()
for i in range(10, 10000000):
    x = [int(a) for a in str(i)]
    if max(x) != len(x):
        continue
    if isPrime(i):
        if "".join(sorted(str(i))) == crate_n_digit_number(i):
            panList.append(i)

# print(panList)
print(max(panList))
