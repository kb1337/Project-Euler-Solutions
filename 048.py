def self_power(n):
    total = 0
    counter = 1
    for i in range(1, n + 1):
        total += i ** counter
        counter += 1
    return total


print(str(self_power(1000))[-10::])
