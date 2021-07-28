def foo(number, pow):
    number = str(number)
    result = 0
    for digit in number:
        result += int(digit) ** pow
    return result

numbers = list()
pow = 5
number = 2

while True:
    if number > 999999: break
    if number == foo(number, pow):
        numbers.append(number)
        #print(number)
    number += 1

print(sum(numbers))
