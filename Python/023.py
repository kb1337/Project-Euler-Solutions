def d(n):
    divs = list()
    for i in range(1, (n // 2) + 1):
        if(n % i == 0):
            divs.append(i)
    return sum(divs)

def sum_of_2_abundants(abundants):
    result = list()
    for i in abundants:
        for j in abundants:
            result.append(i + j)
    return result

abundants = list()
for i in range(28123):
    if(i < d(i)):
        abundants.append(i)

print('abundants found!')

total = 0
my_list = list(set(range(1,28123)) - set(sum_of_2_abundants(abundants)))
print(sum(my_list))
