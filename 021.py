def d(n):
    divs = list()
    for i in range(1, int(n // 2) + 1):
        if(n % i == 0):
            divs.append(i)
    return sum(divs)

res = list()
for i in range(1, 10000):
    if (i != d(i)):
        if(i == d(d(i))):
            res.append(i)

print(sum(res))
