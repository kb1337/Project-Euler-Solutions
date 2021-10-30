def primeDivisorCount(number):
    prime_divisors = dict()

    count = 0
    while number % 2 == 0:
        count += 1
        prime_divisors[2] = count
        number //= 2

    for i in range(3, int(number ** 0.5) + 1, 2):
        count = 1
        while number % i == 0:
            prime_divisors[i] = count
            count += 1
            number //= i

    if number > 2:
        prime_divisors[number] = 1

    div_amount = 1
    for exp in prime_divisors.values():
        div_amount *= exp + 1

    return div_amount


i = 1
while True:
    triangle_number = i * (i + 1) // 2
    divisor_amount = primeDivisorCount(triangle_number)
    if divisor_amount > 500:
        print("{} ---> {}".format(triangle_number, divisor_amount))
        break
    i += 1
