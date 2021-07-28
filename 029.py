numbers = set()
for i in range(2, 101):
    for j in range(2, 101):
        numbers.add(i ** j)

numbers = sorted(numbers)
print(len(numbers))
