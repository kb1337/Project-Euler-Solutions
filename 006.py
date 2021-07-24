def sumSquare(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum ** 2

def squareSum(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i ** 2 
    return sum 

print(sumSquare(100) - squareSum(100))
