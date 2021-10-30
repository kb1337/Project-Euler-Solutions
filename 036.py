def isPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def base2(n):
    return bin(n)[2:]


total = 0
for i in range(1000000):
    if isPalindrome(i) and isPalindrome(base2(i)):
        total += i
        # print(i, base2(i))

print("Total:", total)
