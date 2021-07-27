def fibonacci(count):
    a = 1
    b = 1
    i = 1
    while True:
        a, b = b, a + b
        #print(i + 2, b)
        if(len(str(b)) == 1000):
            print(i + 2, b)
            return 0
        i += 1
fibonacci(100000000)
