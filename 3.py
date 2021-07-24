number = 600851475143 

def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if(number % i == 0):
            return False
    return True

def primeFactor(number):
    for i in range(2, int(number ** 0.5 + 1)):
        if(number % i == 0) and isPrime(i):
            while(number % i == 0):
                #print(i, number)
                number /=i
            print(i)

    if(number != 1):
        print(int(number))
                
primeFactor(number)
