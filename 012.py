def findDivisors(number):
    prime_divosers = dict()

    count = 0
    while number % 2 == 0:
        number //= 2
        count += 1
    if count:
        prime_divosers[2] = count

    for i in range(3, int(number ** 0.5) + 1, 1):
        count = 0
        while number % i == 0:
            number //= i
            count += 1
        if count:
            prime_divosers[i] = count
    div_amount = 1
    for exp in prime_divosers.values():
        div_amount *= exp + 1

    return div_amount


i = 1
while True:
    triangle_number = i * (i + 1) // 2
    divisor_amount = findDivisors(triangle_number)
    if divisor_amount > 500:
        print("\n\n{} ---> {}".format(triangle_number, divisor_amount))
        break
    i += 1
