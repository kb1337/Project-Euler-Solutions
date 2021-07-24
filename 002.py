a = 1
b = 1

sum = 0
print(a)
while (b < 4000000):
    
    a, b = b, a + b
    if(b % 2 == 0):
        sum += b
print(sum)
