def isPalindrome(number):
    if (str(number) == str(number)[::-1]):
        return True
    return False

largestNum = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if(isPalindrome(i * j) and (i * j) > largestNum):
            largestNum = i * j

print(largestNum)
