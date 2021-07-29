def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


circular_primes = set()

for i in range(2, 1000000):
    if not isPrime(i):
        continue

    my_list = list()

    for n in range(1, len(str(i)) + 1):
        my_list.append(int(str(i)[-n:] + str(i)[:-n]))

    all_prime = 1
    for number in my_list:
        if not isPrime(number):
            all_prime = 0
            break

    if all_prime:
        [circular_primes.add(x) for x in my_list]

# print(sorted(circular_primes))
print(len(circular_primes))
