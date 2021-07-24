triplets = {(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17)}

def specialTriplet():
    i = 1
    while True:
        for t in triplets:
            if(t[0] * i + t[1] * i + t[2] * i == 1000):
                print(t[0], t[1], t[2])
                print(t[0] * i, t[1] * i, t[2] * i)
                return t[0] * i * t[1] * i * t[2] * i
        i += 1

print(specialTriplet())
