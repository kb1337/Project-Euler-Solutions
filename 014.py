def even(number):
    return int(number / 2)


def odd(number):
    return 3 * number + 1


greatestCounter = 0
greatestNumber = 0

for number in range(830000, 900000):
    counter = 1
    tempNumber = number
    while number != 1:
        counter += 1
        if number % 2 == 0:
            number = even(number)
        else:
            number = odd(number)
    if counter > greatestCounter:
        greatestCounter = counter
        greatestNumber = tempNumber

print("Start Point: {}\nCounter:{}".format(greatestNumber, greatestCounter))
