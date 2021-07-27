def factorial(number):
    if (number == 1):
        return 1
    return number * factorial(number - 1)

def sumDigits(number):
    number = str(number)
    sum = 0
    for i in number:
        sum += int(i)
    return sum

number = 100

print(sumDigits(factorial(number)))
