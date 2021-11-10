# run with pypy3


def pentagon(n):
    return n * (3 * n - 1) // 2


penList = list()
for i in range(1, 2400):
    penList.append(pentagon(i))

print(penList)

penMin = 999999999
for i in penList:
    for j in penList:
        if i != j:
            if (i + j) in penList and abs(i - j) in penList:
                diff = abs(i - j)
                if diff < penMin:
                    penMin = diff
print(penMin)
