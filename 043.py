from itertools import permutations


def d(number):
    if int(number[1] + number[2] + number[3]) % 2 == 0:
        if int(number[2] + number[3] + number[4]) % 3 == 0:
            if int(number[3] + number[4] + number[5]) % 5 == 0:
                if int(number[4] + number[5] + number[6]) % 7 == 0:
                    if int(number[5] + number[6] + number[7]) % 11 == 0:
                        if int(number[6] + number[7] + number[8]) % 13 == 0:
                            if int(number[7] + number[8] + number[9]) % 17 == 0:
                                return True
    return False


panList = ["".join(x) for x in list(permutations("0123456789"))]
result = [int(x) for x in panList if d(x)]

print(result)
print(sum(result))
