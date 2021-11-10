def divideBelow20(number):
    for i in range(1, 20):
        if(number % i != 0):
            return False
    return True

i = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
while(True):
    if(divideBelow20(i)):
        print(i)
        break
    i += 1
