from itertools import permutations


def d(number):
    if int(number[:3]) % 2 == 0:
        if int(number[2:5]) % 3 == 0:
            if int(number[3:6]) % 5 == 0:
                if int(number[4:7]) % 7 == 0:
                    if int(number[5:8]) % 11 == 0:
                        if int(number[6:9]) % 13 == 0:
                            if int(number[7:]) % 17 == 0:
                                return True
    return False


panList = ["".join(x) for x in list(permutations("0123456789"))]
result = [int(x) for x in panList if d(x)]

print(result)
print(sum(result))
