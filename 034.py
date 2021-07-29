def curious_number(number):
    sum = 0
    for i in str(number):
        sum += factorial(int(i))
    return sum


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


sum = 0
for i in range(3, 1000000):
    if i == curious_number(i):
        print(i)
        sum += i
print("result", sum)
