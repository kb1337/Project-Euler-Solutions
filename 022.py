import string


def calculate(name):
    score = 0
    for letter in name:
        score += alpha.index(letter) + 1
    return score

alpha = list(string.ascii_uppercase)

# https://projecteuler.net/project/resources/p022_names.txt
with open('p022_names.txt', 'r') as f:
    content = f.read()
    names = content.split(',')
    names = [name.replace('"', '') for name in names]
    names.sort()

counter = 1
total = 0
for name in names:
    total += calculate(name) * counter
    counter += 1

print(total)
