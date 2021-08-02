def findDivisors(number):
    div_amount = 0
    print("\n{} ---> ".format(number), end="")
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            div_amount += 1
    div_amount += 1
    print(div_amount)
    return div_amount


# starts with 12373rd triangle number
# 12375th gives answer
i = 12373
while True:
    triangle_number = i * (i + 1) // 2
    divisor_amount = findDivisors(triangle_number)
    if divisor_amount > 500:
        print("\n\nResult: {} ---> {}".format(triangle_number, divisor_amount))
        break
    i += 1
