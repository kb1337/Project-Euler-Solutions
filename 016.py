def digitSum(number):
    summ = 0
    for i in str(number):
        summ += int(i)
    return summ

print(digitSum(2 ** 1000))
