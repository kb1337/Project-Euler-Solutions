def pandigital(number, n):
    pan = ""
    for i in range(1, n + 1):
        pan += str(number * i)

    if "".join(sorted(pan)) != "123456789":
        return 0

    return int(pan)


panList = list()
for i in range(1, 10000):
    for j in range(2, 11):
        n = pandigital(i, j)
        if n != 0:
            panList.append(n)

print(panList)
print(max(panList))
